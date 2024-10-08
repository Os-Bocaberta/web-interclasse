"""interclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.index),
    path("game/<int:id>/", views.game),
    path("futsal/games/", views.list_futsal),
    path("volleyball/games/", views.list_volleyball),
    path("futsal/dashboard/", views.futsal_dashboard),
    path("volleyball/dashboard/", views.volleyball_dashboard),
    path("games/review/", views.games_review),
    path("volleySets/<int:id>/", views.volley_sets_review),
    path("alfredo_ama_o_pe_da_serra/", views.admin_page),
]
