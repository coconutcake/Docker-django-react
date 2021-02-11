from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",include('core.urls')),
    path('admin/', admin.site.urls),
    path('api/user/',include('user.urls'))
]