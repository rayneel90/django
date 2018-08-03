from django.urls import path
from django.views.generic import TemplateView
from .views import Home

app_name = 'log'
urlpatterns = [
        path('', Home, name='home'),
]
