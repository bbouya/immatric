from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.homeFn, name="home"),
    path('login/', views.loginFn, name="login"),
    path('register/', views.registerFn, name = "register"),
    path('logout/', views.logoutFn, name = "logout"),

    #access the laptop camera
    path('video_feed', views.video_feed, name='video_feed'),
    path('select', views.select, name='select'),
    path('select', views.tasks, name='tasks'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/reset_Password.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/sent_reset_Email.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_Confirmation.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_Complete.html"),
         name="password_reset_complete"),

    path('dashboard/', views.dashboardFn, name="dashboard"),

    

]