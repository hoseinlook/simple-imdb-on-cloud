from django.contrib import admin
from posts.models import Movie, Comments

admin.site.register(Comments)
admin.site.register(Movie)
# Register your models here.
