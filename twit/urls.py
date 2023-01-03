"""twit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from tweet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('add_tweet/', views.add_tweet, name='add_tweet_new'),
    path('add_tweet/<int:replied_to>/', views.add_tweet, name='add_tweet_reply'),
    path('retweet/<int:tweet_id>/', views.retweet, name='retweet'),
    path('notifications/', views.notifications, name='notifications'),
    path('register/', views.register, name='register'),
#    path('search/', views.search, name='search'),
    path('search/', include('haystack.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
