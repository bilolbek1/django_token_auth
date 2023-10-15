from django.urls import path
from .views import GamesListApiView, GamesDetailView



urlpatterns = [
    path("", GamesListApiView.as_view(), name="games_list"),
    path("<int:id>", GamesDetailView.as_view(), name="games_detail"),
]