from django.urls import path
from api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('test/', views.test_api, name='test'),
]