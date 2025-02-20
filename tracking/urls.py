from django.urls import path
from .views import track_activity

urlpatterns = [
    path('track/', track_activity, name='track_activity'),
]
