from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . views import register_request,CustomLoginView

app_name = 'user'
urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/',register_request,name='signup'),
    path('login/', CustomLoginView.as_view(), name='login')
]