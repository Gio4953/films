"""
URL configuration for films_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from films.views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView

urlpatterns = [
    path('', FilmListView.as_view(), name='film_list'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('film/create/', FilmCreateView.as_view(), name='film_create'),
    path('film/update/<int:pk>/', FilmUpdateView.as_view(), name='film_update'),
    path('film/delete/<int:pk>/', FilmDeleteView.as_view(), name='film_delete'),
]
