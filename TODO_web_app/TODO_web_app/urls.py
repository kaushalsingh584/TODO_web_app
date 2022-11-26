"""TODO_web_app URL Configuration

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
from django.urls import path
from todo_app import views
from authentication import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = "home"),
    #todo_app
    path('task/', views.task.as_view(),name = "task"),
    path('completed_task/', views.completed_task.as_view(),name = "completed_task"),
    path('pending_task/', views.pending_task.as_view(),name = "pending_task"),
     # authentication
    path('register/', auth_views.RegisterView.as_view(),name = "RegisterView"),
    path('login/', auth_views.LoginView.as_view(),name = "login"),
     # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    
]
