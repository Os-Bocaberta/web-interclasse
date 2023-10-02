from django.urls import path
from .consumers import DashboardConsumer

websocket_urlpatterns = [
    path('ws/football/', DashboardConsumer.as_asgi(), name='dashboard')
]