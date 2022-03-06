from datetime import datetime

from django.shortcuts import render, redirect

from ibm.nlu import get_anger
from ibm.speech_to_text import convert_speech_to_text
from ibm.translate import translate
from posts import models
from posts.forms import InsertCommentForm, GetCommentForm
from simple_imdb import settings


def main_view(request):
    """A view of all bands."""
    movies = models.Movie.objects.all()
    insert_comment_form = InsertCommentForm()
    get_comment_form = GetCommentForm()
    return render(request, 'index.html', {
        'movies': movies,
        'insert_comment_form': insert_comment_form,
        "get_comment_form": get_comment_form
    })


def handle_uploaded_file(f):
    path = settings.MEDIA_ROOT.joinpath(f.name)
    with open(path, 'wb+') as destination:
        destination.write(f.read())


def comments(request, movie_id):
    if request.method == 'POST':
        form = InsertCommentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            handle_uploaded_file(request.FILES['voice'])
            text = convert_speech_to_text(request.FILES['voice'])
            anger = get_anger(text)
            if anger > 0.5:
                text = f'WARNING!: anger is more than 0.5 |anger={anger}'
            else:
                text = f'{text} |anger={anger}'
            models.Comments(voice=request.FILES['voice'], date=datetime.now(), text=text, movie=models.Movie.objects.get(id=movie_id)).save()
            return redirect('/')
        else:
            return redirect('/')

    else:
        form = GetCommentForm(request.GET, request.FILES)
        lang = 'en'
        if form.is_valid():
            lang = request.GET["lang"]

        comments = models.Movie.objects.get(id=movie_id).related_comments
        if lang != 'en':
            for cm in comments:
                text: str = cm.text
                if text.startswith('WARNING!:'):
                    pass
                else:
                    cm.text = translate(text, to_lang=lang)
        return render(request, 'comment.html', {
            'comments': comments,
        })
