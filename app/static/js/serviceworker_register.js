if('serviceWorker' in navigator) {
    // Registering Service Worker
    navigator.serviceWorker.register('serviceworker.js', { scope: '/' });
};
