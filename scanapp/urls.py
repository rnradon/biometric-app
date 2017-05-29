from django.conf.urls import url

from . import views

app_name = 'scanapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_all/$', views.student_list, name='student_list'),
    url(r'^bus/(?P<bus_pk>[0-9]+)/student/(?P<student_id>[0-9]+)$', views.student_detail, name='student_detail'),
    url(r'^bus_all/$', views.bus_list, name='bus_list'),
    url(r'^bus/(?P<bus_pk>[0-9]+)$', views.bus_detail, name='bus_detail'),
]