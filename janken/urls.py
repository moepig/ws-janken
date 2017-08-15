from django.conf.urls import url

from janken import views

app_name = 'janken'

urlpatterns = [
    url(r'^lobby$', views.LobbyView.as_view(), name='lobby'),
    url(r'^room/(?P<room_id>[0-9]+)$', views.MatchView.as_view(), name='room'),
    url(r'^publish$', views.publish, name='publish'),
]