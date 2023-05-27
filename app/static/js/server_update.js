var just_toggled = false;

setInterval(async function () {
    if (just_toggled) {
        just_toggled = false;
        return;
    }

    const response = await fetch("/server/raw");
    if (!response.ok) return;

    const json_data = await response.json();
    
    for (let i=0; i<json_data.length; i++) {
        const current_server = json_data[i];

        const elm = document.querySelector(`#card-list>article[data-id="${current_server['id']}"]`);
        if (!elm) continue;

        if (elm.classList.contains('cancellable') || elm.classList.contains('processing')) continue;
        
        elm.classList.toggle('active', current_server['status']);
    }
}, 8000)
