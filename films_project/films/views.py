from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Film


class FilmListView(ListView):
    model = Film
    template_name = 'films/film_list.html'
    context_object_name = 'films'


class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/film_detail.html'
    context_object_name = 'film'


class FilmCreateView(CreateView):
    model = Film
    template_name = 'films/film_create.html'
    fields = ['name', 'year_of_release', 'length']
    success_url = reverse_lazy('film_list')


class FilmUpdateView(UpdateView):
    model = Film
    template_name = 'films/film_update.html'
    fields = ['name', 'year_of_release', 'length']
    context_object_name = 'film'
    success_url = reverse_lazy('film_list')


class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'films/film_delete.html'
    context_object_name = 'film'
    success_url = reverse_lazy('film_list')
