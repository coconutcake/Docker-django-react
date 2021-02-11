from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import reverse
from django.views.generic.base import RedirectView



urlpatterns = [
    path('',RedirectView.as_view(url="/core/main")),
    
    path('core/',include('core.urls')),
    path('admin/', admin.site.urls),
    path('api/user/',include('user.urls')),
    
    
]