"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.authtoken import views

from artist.views import WorkViewSet, UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/works/', WorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='work-list-create'),
    path('api/works/<int:pk>/', WorkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='work-detail'),
    path('api/works?work_type=<str:work_type>/', WorkViewSet.as_view({'get': 'list'}), name='work-list-filter'),
    path('api/works?artist=<str:artist_name>/', WorkViewSet.as_view({'get': 'list'}), name='work-list-search'),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', CustomAuthToken.as_view()),
]