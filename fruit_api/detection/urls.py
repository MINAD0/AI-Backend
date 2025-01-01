# detection/urls.py

from django.urls import path
from .views import predict_fruit

urlpatterns = [
    path('api/predict/', predict_fruit, name='predict_fruit'),
]
