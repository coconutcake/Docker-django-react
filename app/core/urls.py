from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
    
    
urlpatterns = [    
    re_path("", views.MainView.as_view()),
]