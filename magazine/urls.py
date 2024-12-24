from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('service/', views.ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
    path('search_result/', views.search_result, name='search_result'),
]


