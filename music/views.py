from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except(KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', { 
			'album': album,
			'error_message': 'You did not select any song.',
		})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', { 'album': album})



class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'album_list'
	def get_queryset(self):
		return Album.objects.all()

class DetailView233(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']