from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('club_squad/', views.club_directory, name='club_squad'),
    path('result/', views.result, name='result'),
    path('point_table/', views.point_table, name='point_table'),
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fan_club/login/', LoginView.as_view(), name='login'),
    path('fan_club/logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]
