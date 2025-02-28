from django.urls import path
from .views import login, logout, payment, main

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('main/', main, name='main'),
    path('payment/<int:order_id>/', payment, name='payment'),
]
