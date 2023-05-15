from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('' , include('carrito_app.urls'))
]
