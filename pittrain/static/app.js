const barCtx = document.getElementById('myBarChart');

new Chart(barCtx, {
    type: 'bar',
    data: {
        labels: dateLabels, 
        datasets: [{
            label: "Facts Added Per Day",
            data: countData, 
            borderWidth: 1,
        }]
    },
    options: {
        responsive: true,
    }
});
