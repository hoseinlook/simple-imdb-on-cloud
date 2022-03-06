from django.urls import path, include

from posts import views

urlpatterns = [
    path('', views.main_view),
    path('comment/<int:movie_id>', views.insert_comment),
]
