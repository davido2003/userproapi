"""mainfile URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

<<<<<<< HEAD
schema_view = get_schema_view(
   openapi.Info(
      title="News Api",
      default_version='v1',
      description="News Api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="davidoiwajomo@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
=======
>>>>>>> d9076ffac8f4b376932b155bde6b345978a15bf6

urlpatterns = [
    path('', include('folder.urls')),
    path('admin/', admin.site.urls),
]
