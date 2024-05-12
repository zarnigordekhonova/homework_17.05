from django.contrib import admin
from .models import Books, BookCategory, Language, Author, BookAuthor, Reviews
# Register your models here.
admin.site.register(Books)
admin.site.register(BookCategory)
admin.site.register(BookAuthor)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Reviews)