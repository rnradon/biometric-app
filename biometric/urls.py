"""biometric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from scanapp import views

from django.conf import settings
from django.conf.urls.static import  static


urlpatterns = [
    
    url(r'^$', views.index),    
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^api/', include('api.urls')),
    # url(r'^student/', views.ListCreateStudents.as_view()),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2')),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^scanapp/', include('scanapp.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    # url(r'^sms/$', include('djtwilio.views.sms')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)