from django.conf.urls import url
from . import views
from django.conf import settings 
from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', views.subject_list, name='subject_list'),
    url(r'^subject/new/$', views.subject_new, name='subject_new'),
    url(r'^subject/(?P<pk>\d+)/$', views.subject_detail, name='subject_detail'),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^sign_up/$', views.CreateUserView.as_view(), name="user"),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),


]
