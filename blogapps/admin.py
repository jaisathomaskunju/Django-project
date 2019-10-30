from django.contrib import admin
from .models import Author, Comment
from .models import Blogs

admin.site.register(Blogs)
admin.site.register(Author)
admin.site.register(Comment)
