from django.conf.urls import url

from . import views
# from .views import StudentList, StudentDetail

app_name = 'scanapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_all/$', views.student_list, name='student_list'),
    url(r'^bus/(?P<bus_pk>[0-9]+)/student/(?P<student_biometric_id>[0-9]+)$', views.student_detail, name='student_detail'),
    url(r'^bus_all/$', views.bus_list, name='bus_list'),
    url(r'^bus/(?P<bus_number>[0-9]+)$', views.bus_detail, name='bus_detail'),
    url(r'^parent/(?P<admission_number>[0-9]+)$', views.parent_view, name='parent_view'),
    

    url(r'^sign_up_student/$', views.register_student, name="register_student"),
    url(r'^sign_up_bus/$', views.register_bus, name="register_bus"),
    # url(r'^sms/$', views.Msg91SmsBackend, name = 'awesome_method'),
    url(r'^email/(?P<admission_number>[0-9]+)/message/(?P<message>[\w\-]+)$', views.email, name='email'),
    url(r'^password/change$', views.callback, name='callback'),
    # url(r'^send/(?P<phone_number>[0-9]+)/message/(?P<message>[\w\-]+)$', views.awesome_method, name='email'),

]