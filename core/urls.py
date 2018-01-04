from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.subject_list, name='subject_list'),
    url(r'^subject/new/$', views.subject_new, name='subject_new'),
    url(r'^subject/(?P<pk>\d+)/$', views.subject_detail, name='subject_detail'),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    url(r'^sign_in/$', views.SignIn.as_view(), name="sign_in"),

]
