from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # '/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # '/music/id'
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name ='detail'),
    # 'album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name ='album-add'),
    # 'album/2
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name ='album-update'),

    # 'album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name ='album-delete'),


]
