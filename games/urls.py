from django.urls import path
from .views import GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

urlpatterns = [
    path('Game/', GameListView.as_view(), name='Game_list'),
    path('Game/<int:pk>/', GameDetailView.as_view(), name='Game_detail'),
    path('Game/create/', GameCreateView.as_view(), name='Game_create'),
    path('Game/<int:pk>/update/', GameUpdateView.as_view(), name='Game_update'),
    path('Game/<int:pk>/delete/', GameDeleteView.as_view(), name='Game_delete'),
]