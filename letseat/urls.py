"""letseat URL Configuration

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
from django.conf.urls import include
from rest_framework import routers
from letseatapi.views import register_user, check_user, RestaurantViews, SpinnerViews, CategoryViews, UserViews, SelectedRestaurantViews

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'restaurants', RestaurantViews, 'restaurant')
router.register(r'spinners', SpinnerViews, 'spinner')
router.register(r'categories', CategoryViews, 'category')
router.register(r'users', UserViews, 'user')
router.register(r'selected_restaurants', SelectedRestaurantViews, 'selected_restaurant')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user, name='register_user'),
    path('checkuser', check_user, name='check_user'),
    path('', include(router.urls)),
]
