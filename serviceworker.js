var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilos.css',
    '/static/core/img/floreria.png',
    '/static/core/img/banner1.png',
    'galeria/',
    'registro/',
    'accounts/login/',

];

self.addEventListener('install', function (event) {

    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function (event) {
    event.respondWith(

        fetch(event.request)
            .then(function (result) {
                return caches.open(CACHE_NAME)
                    .then(function (c) {
                        c.put(event.request.url, result.clone());
                        return result;
                    })
            })

            .catch(function (e) {
                return caches.match(event.request)
            })


    );
});


//codigo para notificaciones push
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyBYdNgB6IL05qJIOI7T7eQCfETWeaR8-5Q",
    authDomain: "floreria-534f0.firebaseapp.com",
    databaseURL: "https://floreria-534f0.firebaseio.com",
    projectId: "floreria-534f0",
    storageBucket: "floreria-534f0.appspot.com",
    messagingSenderId: "370082663539",
    appId: "1:370082663539:web:d15339c234de0c07c56e06"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
    let title = "titulo de la notificacion";

    let options = {
        body: 'este es el mensaje',
        icon: '/static/core/img/icono.png',
    }

    self.registration.showNotification(title, options);
});