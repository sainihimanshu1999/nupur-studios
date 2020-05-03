from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('aboutus/', views.Aboutus, name ='aboutus'),
    path('login/', views.userLogin, name ='login'),
    path('register/', views.register, name = "register"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('profile/', views.profile, name = "profile"),
    path('dashboard-messages/', views.dashboard_messages, name = "dashboard-meassages"),
    path('dashboard-bookings/', views.dashboard_bookings, name = "dashboard-bookings"),
    path('dashboard-wallet/', views.dashboard_wallet, name = "dashboard-wallet"),
    path('dashboard-listing/', views.dashboard_listing, name = "dashboard-listing"),
    path('dashboard-reviews/', views.dashboard_reviews, name = "dashboard-reviews"),
    path('dashboard-bookmarks/', views.dashboard_bookmarks, name = "dashboard-bookmarks"),
    path('dashboard-addlisting/', views.dashboardAddlist , name = "dashboard-addlisting"),
    path('dashboard-myprofile/', views.dashboard_profile , name = "dashboard-myprofile"),


]