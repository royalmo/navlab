setInterval(async function () {
    const response = await fetch("/monitoring/raw");
    if (!response.ok) return;

    const json_data = await response.json();
    
    for (let i=0; i<json_data.length; i++) {
        const current_monitor = json_data[i];

        const elm = document.querySelector(`#monitor_frame_${current_monitor['id']}`);
        if (!elm) continue;

        elm.querySelector('.last_sample_time').innerText = current_monitor['last_sample']['time'];
        elm.querySelector('.last_sample_value').innerText = current_monitor['last_sample']['value'];

        const chart = charts[current_monitor['key']];

        chart.data.datasets[0].data = current_monitor['y_axis'];
        chart.data.labels = current_monitor['x_axis'];
        chart.update();
    }
}, 8000)
