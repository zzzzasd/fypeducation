from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.subject_list, name='subject_detail'),
]