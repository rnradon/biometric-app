from django.conf.urls import url

from . import views
# from .views import StudentList, StudentDetail

app_name = 'emergencycapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^emergency_contacts/$', views.emergency_contact_list, name='emergency_contact_list'),
]