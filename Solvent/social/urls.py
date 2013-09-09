from django.conf.urls import patterns, include, url
from Solvent.social import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'), 
                       url(r'^users/$', views.users, name='users'),
                       url(r'^users/(?P<user_id>\d+)$', views.userDetail, name='userDetail'),
                       url(r'^projects/$', views.projects, name='projects'),
                       url(r'^projects/(?P<project_id>\d+)$', views.projectDetail, name='projectDetail'),
                       url(r'^attachments/(?P<attachment_id>\d+)$', views.attachmentDetail, name='attachmentDetail'),
)
