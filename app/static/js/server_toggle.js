if (typeof host === 'undefined') host = '';

document.querySelectorAll('.start-button').forEach(button => {
    button.addEventListener('click', async (e) => {
        e.preventDefault(); // Prevent the <a> tag from redirecting
        const article = e.target.closest('article');
        article.classList.add('active', 'cancellable', 'starting');
        setTimeout(async () => {
            if (article.classList.contains('cancellable')) {
                article.classList.remove('cancellable', 'starting');
                article.classList.add('processing');

                const id = article.dataset.id;
                const response = await fetch(`${host}/server/${id}/start`);

                article.classList.remove('processing');
                if (!response.ok) {
                    article.classList.remove('active');
                }
            }
        }, 3000);
    });
});

document.querySelectorAll('.stop-button').forEach(button => {
    button.addEventListener('click', async (e) => {
        e.preventDefault(); // Prevent the <a> tag from redirecting
        const article = e.target.closest('article');
        article.classList.add('cancellable', 'stopping');
        setTimeout(async () => {
            if (article.classList.contains('cancellable')) {
                article.classList.remove('cancellable', 'stopping');
                article.classList.add('processing');

                const id = article.dataset.id;
                const response = await fetch(`${host}/server/${id}/stop`);

                article.classList.remove('processing');
                if (response.ok) {
                    article.classList.remove('active');
                }
            }
        }, 3000);
    });
});

document.querySelectorAll('.cancel-button').forEach(button => {
    button.addEventListener('click', async (e) => {
        e.preventDefault(); // Prevent the <a> tag from redirecting
        const article = e.target.closest('article');
        if (article.classList.contains('starting')) {
            article.classList.remove('cancellable', 'active', 'starting');
        }
        else {
            article.classList.remove('cancellable', 'stopping');
        }
    });
});
