from django.urls import path
from . import views


urlpatterns = [
    path('', views.deal_table, name='deal_table'),
    path('deal/<int:pk>', views.deal_detail, name='deal_detail'),
]