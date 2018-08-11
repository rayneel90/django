from django.urls import path
from .views import print

app_name = 'print'
urlpatterns = [
        path('', print, name='print'),
]
