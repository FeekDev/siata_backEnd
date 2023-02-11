from django.contrib import admin
from django.urls import path, include
from restaurante import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/pagos', views.api_pagos),
    path('api/pagos', views.api_pagos)
]
