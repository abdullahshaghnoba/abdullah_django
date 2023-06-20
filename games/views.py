from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Game


class GameListView(ListView):
    template_name = "games/game-list.html"
    model = Game
    context_object_name = "Game"

class GameDetailView(DetailView):
    template_name = "games/game-detail.html"
    model = Game


class GameCreateView(CreateView):
    template_name = "games/game-create.html"
    model = Game
    fields = ['name','purchaser','genre']


class GameUpdateView(UpdateView):
    template_name = "games/game-update.html"
    model = Game
    fields = ['name','purchaser','genre']


class GameDeleteView(DeleteView):
    template_name = "games/game-delete.html"
    model = Game
    success_url = reverse_lazy("Game_list")