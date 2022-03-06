from datetime import datetime

from django.shortcuts import render, redirect

from ibm.nlu import get_anger
from ibm.speech_to_text import convert_speech_to_text
from posts import models
from posts.forms import CommentForm
from simple_imdb import settings


def main_view(request):
    """A view of all bands."""
    movies = models.Movie.objects.all()
    form = CommentForm()
    return render(request, 'index.html', {'movies': movies, 'form': form})


def handle_uploaded_file(f):
    path = settings.MEDIA_ROOT.joinpath(f.name)
    with open(path, 'wb+') as destination:
        destination.write(f.read())


def insert_comment(request,movie_id):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            handle_uploaded_file(request.FILES['voice'])
            text = convert_speech_to_text(request.FILES['voice'])
            anger = get_anger(text)
            if anger > 0.5:
                text = f'WARNING: anger is more than 0.5 |anger={anger}'
            else:
                text =f'{text} |anger={anger}'
            models.Comments(voice=request.FILES['voice'], date=datetime.now(), text=text, movie=models.Movie.objects.get(id=movie_id)).save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return {"message": "bad request"}
