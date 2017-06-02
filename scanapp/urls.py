from django.conf.urls import url

from . import views
# from .views import StudentList, StudentDetail

app_name = 'scanapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_all/$', views.student_list, name='student_list'),
    url(r'^bus/(?P<bus_pk>[0-9]+)/student/(?P<student_id>[0-9]+)$', views.student_detail, name='student_detail'),
    url(r'^bus_all/$', views.bus_list, name='bus_list'),
    url(r'^bus/(?P<bus_pk>[0-9]+)$', views.bus_detail, name='bus_detail'),
    # url(r'^sign_up/$', views.RegistrationView.as_view(), name="sign_up"),
    # url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^sms/$', views.Msg91SmsBackend, name = 'awesome_method'),
]