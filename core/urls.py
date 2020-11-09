from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),#127.0.0.1:post

]
