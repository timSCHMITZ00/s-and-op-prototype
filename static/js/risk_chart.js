// Processing the risk metric object
let times = riskMetricValues.map(obj => obj.time).reverse();
let data = riskMetricValues.map(obj => obj.value).reverse();
let setpointData = times.map(() => riskMetricSetpoint); // array of the same setpoint value

// Creating the graph
let ctx = document.getElementById('canvas').getContext('2d');

let myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: times,
        datasets: [{
            label: riskMetricName,
            data: data,
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1,
            pointRadius: 5,
            pointBackgroundColor: 'rgb(75, 192, 192)'
        },
        {
            label: 'Setpoint',
            data: setpointData,
            fill: false,
            borderColor: 'rgb(255, 99, 132)',
            borderWidth: 2,
            borderDash: [5, 5], // This creates a dashed line
            pointRadius: 0 // No points are shown
        }]
    },
    options: {
        animation: {
            duration: 1000, // general animation time
            onComplete: function () {
                this.options.animation.duration = 0; // set animation duration to 0 after first render to disable it
            }
        },
        scales: {
            y: {
                beginAtZero: false
            }
        },
        plugins: {
            title: {
                display: true,
                text: heading
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        var label = context.dataset.label || '';
                        if (label) {
                            label += ': ';
                        }
                        if (context.parsed.y !== null) {
                            label += new Number(context.parsed.y).toFixed(2);
                        }
                        return label + ' ' + riskMetricUnit;
                    }
                }
            }
        }
    }
});

function updateChart() {
    fetch('/get-risk-data/' + riskId)
        .then(response => response.json())
        .then(data => {
            myLineChart.data.labels = data.labels;
            myLineChart.data.datasets[0].data = data.datasets[0].data.reverse();
            myLineChart.data.datasets[1].data = data.datasets[1].data.reverse();
            myLineChart.update();
        });
}

// Call updateChart at regular intervals, or in response to user actions
setInterval(updateChart, 10000);  // updates every 10 seconds