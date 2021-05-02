"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from frame import views
from frame.views import index
from frame.views import registeration
from frame.views import navbar
from frame.views import navbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
     path('', views.index, name="index"),
     path('registeration.html',views.registeration,),
     path('navbar.html',views.navbar,),
     path('login.html',views.login,),
    path('admin/', admin.site.urls),

  
]
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)

urlpatterns += staticfiles_urlpatterns()


