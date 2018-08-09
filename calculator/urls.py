from django.urls import path
from .views import CalculatorView, temp

app_name = 'calculator'
urlpatterns = [
    path('', CalculatorView.as_view(), name='calculator'),
    path('abc/', temp, name='abc'),
]
