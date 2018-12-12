from django.conf.urls import url
from . import views
from . import myown
app_name = 'music'
urlpatterns = [
				    url(r'^$', views.IndexView.as_view(), name='index'),
				    url(r'^(?P<pk>[0-9]+)/$', views.DetailView233.as_view(), name='detail'),
				    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
				    url(r'album/add/$', views.AlbumCreate.as_view(), name = 'album-add'),

				    url(r'^myown/', myown.index, name='myown'),
			  ]