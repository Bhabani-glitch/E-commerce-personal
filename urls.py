from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('track/<int:order_id>/', views.track_order, name='track_order'),
    # More URLs...
]