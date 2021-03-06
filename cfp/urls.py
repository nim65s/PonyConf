from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cfp/$', views.talk_proposal, name='talk-proposal'),
    url(r'^cfp/(?P<talk_id>[\w\-]+)/speaker/add/$', views.talk_proposal_speaker_edit, name='talk-proposal-speaker-add'),
    url(r'^cfp/(?P<talk_id>[\w\-]+)/speaker/(?P<participant_id>[\w\-]+)/$', views.talk_proposal_speaker_edit, name='talk-proposal-speaker-edit'),
    url(r'^cfp/(?P<talk_id>[\w\-]+)/(?P<participant_id>[\w\-]+)/$', views.talk_proposal, name='talk-proposal-edit'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^staff/conference/$', views.conference, name='conference'),
    url(r'^staff/talks/$', views.talk_list, name='talk-list'),
    url(r'^staff/talks/(?P<talk_id>[\w\-]+)/$', views.talk_details, name='talk-details'),
    url(r'^staff/talks/(?P<talk_id>[\w\-]+)/vote/(?P<score>[-+0-2]+)/$', views.talk_vote, name='talk-vote'),
    url(r'^staff/talks/(?P<talk_id>[\w\-]+)/accept/$', views.talk_decide, {'accept': True}, name='talk-accept'),
    url(r'^staff/talks/(?P<talk_id>[\w\-]+)/decline/$', views.talk_decide, {'accept': False}, name='talk-decline'),
    url(r'^staff/talks/(?P<talk_id>[\w\-]+)/edit/$', views.TalkUpdate.as_view(), name='talk-edit'),
    url(r'^staff/speakers/$', views.participant_list, name='participant-list'),
    url(r'^staff/speakers/(?P<participant_id>[\w\-]+)/$', views.participant_details, name='participant-details'),
    url(r'^staff/speakers/(?P<participant_id>[\w\-]+)/edit/$', views.ParticipantUpdate.as_view(), name='participant-edit'),
    url(r'^staff/tracks/$', views.TrackList.as_view(), name='track-list'),
    url(r'^staff/tracks/add/$', views.TrackCreate.as_view(), name='track-add'),
    url(r'^staff/tracks/(?P<slug>[-\w]+)/edit/$', views.TrackUpdate.as_view(), name='track-edit'),
    url(r'^staff/rooms/$', views.RoomList.as_view(), name='room-list'),
    url(r'^staff/rooms/add/$', views.RoomCreate.as_view(), name='room-add'),
    url(r'^staff/rooms/(?P<slug>[-\w]+)/$', views.RoomDetail.as_view(), name='room-details'),
    url(r'^staff/rooms/(?P<slug>[-\w]+)/edit/$', views.RoomUpdate.as_view(), name='room-edit'),
    url(r'^staff/add-user/$', views.create_user, name='create-user'),
    url(r'^staff/schedule/((?P<program_format>[\w]+)/)?$', views.staff_schedule, name='staff-schedule'),
    url(r'^staff/select2/$', views.Select2View.as_view(), name='django_select2-json'),
    url(r'^schedule/((?P<program_format>[\w]+)/)?$', views.public_schedule, name='public-schedule'),
    #url(r'^markdown/$', views.markdown_preview, name='markdown'),
]
