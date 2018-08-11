from django.urls import path
from .views import myview

app_name = 'calculator'
urlpatterns = [
    path('', myview, name='calc_form'),
]
