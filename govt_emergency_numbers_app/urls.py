from django.conf.urls import url

from . import views
# from .views import StudentList, StudentDetail

app_name = 'govt_emergency_numbers_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts_list/$', views.govt_emergency_contact_list, name='govt_emergency_contact_list'),
]