from django.conf.urls import url

from . import views
# from .views import StudentList, StudentDetail

app_name = 'scanapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_all/$', views.student_list, name='student_list'),
    url(r'^bus_route_number/(?P<bus_route_number>[0-9]+)/student_biometric_id/(?P<student_biometric_id>[0-9]+)$', views.student_detail, name='student_detail'),
    url(r'^bus_all/$', views.bus_list, name='bus_list'),
    url(r'^bus_route_number/(?P<bus_route_number>[0-9]+)$', views.bus_app_detail, name='bus_app_detail'),
    url(r'^bus_primary_key/(?P<bus_id>[0-9]+)$', views.student_bus_detail, name='student_bus_detail'),
    url(r'^parent_student_admission_number/(?P<admission_number>[0-9]+)$', views.parent_view, name='parent_view'),
    

    url(r'^sign_up_student/$', views.register_student, name="register_student"),
    url(r'^sign_up_bus/$', views.register_bus, name="register_bus"),
    # url(r'^sms/$', views.Msg91SmsBackend, name = 'awesome_method'),
    url(r'^email/(?P<admission_number>[0-9]+)/message/(?P<message>[\w\-]+)$', views.email, name='email'),
    url(r'^password/change$', views.callback, name='callback'),
    url(r'^delete_user$', views.delete_user, name='delete_user'),
    url(r'^delete_user_model$', views.delete_user_model, name='delete_user_model'),
    # url(r'^send/(?P<phone_number>[0-9]+)/message/(?P<message>[\w\-]+)$', views.awesome_method, name='email'),

]