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
    # path("mdisplay",views.display_soc,name="display_soc"),
    path('', views.m_index, name='m_index'),
    path('login-page/', views.loginpage, name='login-page'),
    path('m_logout/', views.m_logout, name='m_logout'),
    path('sm_profile/',views.sm_profile, name='sm_profile'),
    path('m-profile-update/', views.m_profile_update, name='m-profile-update'),
    path('m-view-notice/', views.m_view_notice, name='m-view-notice'),
    path('m-view-event/', views.m_view_event, name='m-view-event'),
    path('m-view-member/', views.m_view_member, name='m-view-member'),
    path('m_add_complaint_page/', views.m_add_complaint_page, name='m_add_complaint_page'),
    path('m_add_complaint/', views.m_add_complaint, name='m_add_complaint'),
    path('m_view_complaint/', views.m_view_complaint, name='m_view_complaint'),
    path('m_del_complaint/<int:pk>', views.m_del_complaint, name='m_del_complaint'),
    path('add_suggestion_page/', views.add_suggestion_page, name='add_suggestion_page'),
    path('add_suggestion/', views.add_suggestion, name='add_suggestion'),
    path('view_suggestions/', views.view_suggestions, name='view_suggestions'),
    path('del-suggestion/<int:pk>', views.del_suggestion, name='del-suggestion'),
    path('m-member-profile/<int:pk>', views.m_member_profile, name='m-member-profile'),
    path('m_view_images/', views.m_view_images, name='m_view_images'),
    path('m_view_videos/', views.m_view_videos, name='m_view_videos'),
    path('m_view_maintenance/', views.m_view_maintenance, name='m_view_maintenance'),
    path('m_pay_maintenance/', views.m_pay_maintenance, name='m_pay_maintenance'),
    path('m_view_visitors/', views.m_view_visitors, name='m_view_visitors'),
    path('m_watchman_list/', views.m_watchman_list, name='m_watchman_list'),
]
