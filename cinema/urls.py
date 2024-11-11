from django.urls import path

from cinema.views import genre_list, genre_detail, ActorList, ActorDetail, CinemaHallDetail, CinemaHallList, MovieViewSet

movie_list = MovieViewSet.as_view(actions={
            "get": "list",
            "post": "create",
        })

movie_detail = MovieViewSet.as_view(actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        })

urlpatterns = [
    path("api/cinema/genres/", genre_list, name="genre-list"),
    path("api/cinema/genres/", genre_detail, name="genre-detail"),
    path("api/cinema/actors/", ActorList.as_view(), name="actor-list"),
    path("api/cinema/actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("api/cinema/cinamehalls/<int:pk>/", CinemaHallDetail.as_view(), name="cinemahall-detail"),
    path("api/cinema/cinemahalls/", CinemaHallList.as_view(), name="cinemahall-list"),
    path("api/cinema/movies/", movie_list, name="movie-list"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
