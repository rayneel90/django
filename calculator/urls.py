from django.urls import path
from .views import myview, abc

app_name = 'calculator'
urlpatterns = [
    path('', myview, name='calc_form'),
    path('abc', abc, name='abc'),
]
