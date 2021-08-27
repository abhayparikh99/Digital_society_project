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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login-page/', views.login_page, name='login-page'),
    path('login-evalute/', views.login_evalute, name='login-evalute'),
    path('logout/', views.logout, name='logout'),
    path('forgot-password-page/', views.forgot_password_page, name='forgot-password-page'),
    path('send-otp/', views.send_otp, name='send-otp'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('add-notice-page/', views.add_notice_page, name='add-notice-page'),
    path('add-notice/', views.add_notice, name='add-notice'),
    path('view-notice/', views.view_notice, name='view-notice'),
    path('del-notice/<int:pk>', views.del_notice, name='del-notice'),
    path('profile/', views.profile, name='profile'),
    path('profile-update/', views.profile_update, name='profile-update'),
    path('view-member/', views.view_member, name='view-member'),
    path('member-profile/<int:pk>', views.member_profile, name='member-profile'),
    path('add-event-page/', views.add_event_page, name='add-event-page'),
    path('add-event/', views.add_event, name='add-event'),
    path('view-event/', views.view_event, name='view-event'),
    path('del-event/<int:pk>', views.del_event, name='del-event'),
    path('add-member-page/', views.add_member_page, name='add-member-page'),
    path('add-member/', views.add_member, name='add-member'),
    path('view_complaint/', views.view_complaint, name='view_complaint'),
    path('del-complaint/<int:pk>', views.del_complaint, name='del-complaint'),
    path('c_view_suggestions/', views.c_view_suggestions, name='c_view_suggestions'),
    path('upload_page/', views.upload_page, name='upload_page'),
    path('add_image/', views.add_image, name='add_image'),
    path('add_video/', views.add_video, name='add_video'),
    path('view_images/', views.view_images, name='view_images'),
    path('view_videos/', views.view_videos, name='view_videos'),
    path('del_video/<int:pk>', views.del_video, name='del_video'),
    path('del_image/<int:pk>', views.del_image, name='del_image'),
    path('add_maintenance_page/', views.add_maintenance_page, name='add_maintenance_page'),
    path('add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('view_maintenance/', views.view_maintenance, name='view_maintenance'),
    path('w_registration_page/', views.w_registration_page, name='w_registration_page'),
    path('send_approval/', views.send_approval, name='send_approval'),
    path('watchman_list/', views.watchman_list, name='watchman_list'),
    path('watchman_status/<int:pk>/<slug:status>', views.watchman_status, name='watchman_status'),
    path('c_view_visitors/', views.c_view_visitors, name='c_view_visitors'),
    path('pay_maintenance/', views.pay_maintenance, name='pay_maintenance'),
    path('initiate_payment/<int:pk>', views.initiate_payment, name='initiate_payment'),
    path('callback/', views.callback, name='callback'),
]
