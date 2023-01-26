from django.urls import path
from . views import register_request

app_name = 'user'
urlpatterns = [
    path('signup/',register_request,name='signup')
]