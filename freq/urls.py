from django.urls import path
from . import views

urlpatterns = [
    path('frequency/', views.frequency, name='Frequency-home'),
    path('result/', views.result, name='Frequency-result'),
]
