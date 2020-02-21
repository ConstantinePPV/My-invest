from django.urls import path
from . import views


urlpatterns = [
    path('', views.deal_table, name='deal_table'),
]