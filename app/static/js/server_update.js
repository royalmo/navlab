setInterval(async function () {
    const response = await fetch('/server/raw');
    if (!response.ok) return;

    const json_data = await response.json();
    
    for (let i=0; i<json_data.length; i++) {
        const current_server = json_data[i];

        const elm = document.querySelector(`#card-list>article[data-id="${current_server['id']}"]`);
        if (!elm) continue;
        
        elm.classList.toggle('active', current_server['status']);
    }
}, 8000)
