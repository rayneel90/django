from django.urls import path
from .views import Home

app_name = 'backend'
urlpatterns = [
        path('', Home, name='home'),
]
