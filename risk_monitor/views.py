from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Risk, RiskMetric, RiskMetricValue, RiskSubscription
from django.http import JsonResponse
from django import forms
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def home(request):
    all_risks = Risk.objects.all()

    high_risk = Risk.objects.filter(score='High')
    medium_risk = Risk.objects.filter(score='Medium')
    low_risk = Risk.objects.filter(score='Low')

    high_risk_sum = sum(1.5 if risk.trend == 'Increasing' else 0.5 if risk.trend == 'Decreasing' else 1 for risk in high_risk)
    medium_risk_sum = sum(1.5 if risk.trend == 'Increasing' else 0.5 if risk.trend == 'Decreasing' else 1 for risk in medium_risk)
    low_risk_sum = sum(1.5 if risk.trend == 'Increasing' else 0.5 if risk.trend == 'Decreasing' else 1 for risk in low_risk)

    high_risk_count = high_risk.count()
    medium_risk_count = medium_risk.count()
    low_risk_count = low_risk.count()

    best_case = (high_risk_count * 3 + medium_risk_count * 2 + low_risk_count) * 0.5 #all risks are decreasing

    total_risk = high_risk_sum * 3 + medium_risk_sum * 2 + low_risk_sum # weighted sum of all risks

    worst_case = (high_risk_count * 3 + medium_risk_count * 2 + low_risk_count) * 1.5 #all risks are increasing

    #subtract best case from total risk to get the risk relative to the best case

    total_risk -= best_case

    worst_case -= best_case

    if worst_case != 0:
        relative_risk = round(total_risk / worst_case * 100) #risk in regards to the worst case
    else:
        relative_risk = 0  #no risks

    user = str(request.user)


    if user == 'sales_user':
        risk_category = 'Sales'
    elif user == 'marketing_user':
        risk_category = 'Marketing'
    elif user == 'operations_user':
        risk_category = 'Operations'
    elif user == 'supply_chain_user':
        risk_category = 'Supply'
    else:
        risk_category = 'all'

        
    context = {
        'all_risks': all_risks,
        'total_risk': relative_risk,
        'risk_category': risk_category,
    }
    return render(request, 'home.html', context)

@login_required()
def settings(request):
    all_risk_metrics = RiskMetric.objects.all()
    context = {
        'all_risk_metrics': all_risk_metrics,
    }
    return render(request, 'settings.html', context)

@login_required()
@require_http_methods(["GET", "POST"])
def risk(request, risk_id):
    risk = Risk.objects.get(id=risk_id)
    risk_metric = RiskMetric.objects.get(risk=risk)
    risk_metric_values = RiskMetricValue.objects.filter(risk_metric=risk_metric).all()

    context = {
        'risk': risk,
        'risk_metric': risk_metric,
        'risk_metric_values': risk_metric_values,
    }

    if request.method == 'POST':
        # Get values from POST data
        risk_score = request.POST.get('score')
        risk_metric_setpoint = request.POST.get('setpoint')

        # Update the risk object
        risk.score = risk_score
        risk_metric.setpoint = float(risk_metric_setpoint)
        risk.save()
    
    return render(request, 'risk.html', context)
    
@login_required()
def get_risk_data(request, risk_id):

    risk = Risk.objects.get(pk=risk_id)
    risk_metric = RiskMetric.objects.get(risk=risk)
    risk_metric_values = RiskMetricValue.objects.filter(risk_metric=risk_metric).all()
    setpoint = risk_metric.setpoint
    data = {
    "labels": [],
    "datasets": [
            {
                "label": risk_metric.name,
                "data": [],
                "backgroundColor": 'rgba(255, 99, 132, 0.2)',
                "borderColor": 'rgba(255, 99, 132, 1)',
                "borderWidth": 1
            },
            {
                "label": 'Setpoint',
                "data": [],
                "fill": False,  # In Python, use True and False for boolean values
                "borderColor": 'rgb(255, 99, 132)',
                "borderWidth": 2,
                "borderDash": [5, 5],  # This creates a dashed line
                "pointRadius": 0  # No points are shown
            }
        ]
    }

    for risk_metric_value in risk_metric_values:
        data["labels"].append(risk_metric_value.timestamp)  
        data["datasets"][0]["data"].append(risk_metric_value.value)
        data["datasets"][1]["data"].append(setpoint)

    return JsonResponse(data, safe=False)


@login_required()
def subscribe(request, risk_id):
    risk = Risk.objects.get(pk=risk_id)
    user = request.user
    if RiskSubscription.objects.filter(risk=risk).filter(user = user).exists() == False:
        RiskSubscription.objects.create(user = user, risk=risk)
        messages.success(request, 'You have successfully subscribed to this risk.')
    else:
        messages.error(request, 'You are already subscribed to this risk.')

    return redirect('risk', risk_id=risk_id)