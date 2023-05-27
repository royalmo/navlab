// Service Worker version
const version = 'v1';

// Files to cache
const cacheFiles = [
  '/login',
  // Add other files to cache as needed
];

// Install event
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(version).then((cache) => {
      return cache.addAll(cacheFiles);
    })
  );
});

// Activate event
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== version) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Fetch event
self.addEventListener('fetch', (event) => {
  event.respondWith(
    // Try to fetch from network first
    fetch(event.request)
      .then((response) => {
        // Clone the response
        const responseClone = response.clone();

        // Update cache with the latest response
        caches.open(version).then((cache) => {
          cache.put(event.request, responseClone);
        });

        return response;
      })
      .catch(() => {
        // If network fetch fails, serve from cache
        return caches.match(event.request).then((response) => {
          if (response) {
            return response;
          }
        });
      })
  );
});
