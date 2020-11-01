from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    
    path('',views.indexView, name="homeboi"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/',LoginView.as_view(), name="login"), 
    path('register/',views.registerView, name="register_url"), 
    # path('logout/',), 
]
