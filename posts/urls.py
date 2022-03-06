from django.urls import path, include

from posts import views

urlpatterns = [
    path('', views.main_view),
    path('movies/<int:movie_id>/comments', views.comments),
]
