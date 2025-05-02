from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main_view, name='main'),
    path('landing/', views.landing_view, name='landing'),
]