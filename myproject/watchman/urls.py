"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.w_index, name='w_index'),
    path('w_logout', views.w_logout, name='w_logout'),
    path('login-page', views.w_login_page, name='login-page'),
    path('w_view_member/', views.w_view_member, name='w_view_member'),
    path('w_view_notice/', views.w_view_notice, name='w_view_notice'),
    path('w_view_event/', views.w_view_event, name='w_view_event'),
    path('w_view_complaint/', views.w_view_complaint, name='w_view_complaint'),
    path('w_view_suggestions/', views.w_view_suggestions, name='w_view_suggestions'),
    path('w_profile', views.w_profile, name='w_profile'),
    path('w_profile_update/', views.w_profile_update, name='w_profile_update'),
    path('add_visitor_page/', views.add_visitor_page, name='add_visitor_page'),
    path('add_visitor/', views.add_visitor, name='add_visitor'),
    path('view_visitor/', views.view_visitor, name='view_visitor'),
]
