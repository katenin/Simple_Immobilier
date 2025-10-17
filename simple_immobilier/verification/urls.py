from django.urls import path
from . import views

urlpatterns = [
    path('', views.verification_view, name='verification_view'),
    path('success/', views.verification_success_view, name='verification_success'),
]
