"""prototype_drf_dss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers
from prova import views
from django.urls import include, re_path

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'province', views.ProvinciaDetail)
#router.register(r'province2', views.Provincia2DetailView.as_view())
router.register(r'province3', views.Provincia3Detail)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^province2/(?P<id>[0-9a-f-]+)/$', view=views.Provincia2DetailView.as_view(), name='province2'),
]
