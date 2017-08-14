from django.conf.urls import url

from janken import views

app_name = 'janken'

urlpatterns = [
    url(r'^lobby$', views.LobbyView.as_view(), name='lobby')
]