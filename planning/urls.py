from django.conf.urls import url

from planning import views


urlpatterns = [
    url(r'^room/$', views.RoomList.as_view(), name='list-rooms'),
    url(r'^room/add/$', views.RoomCreate.as_view(), name='add-room'),
    url(r'^room/(?P<slug>[-\w]+)/$', views.RoomDetail.as_view(), name='show-room'),
    url(r'^room/(?P<slug>[-\w]+)/edit/$', views.RoomUpdate.as_view(), name='edit-room'),
    url(r'^schedule/$', views.program_pending, name='show-schedule'),
    url(r'^schedule/public/$', views.program_public, name='public-schedule'),
    url(r'^planning/program/public/$', views.program_public),
]
