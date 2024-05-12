from django.db import models
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'book_category'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=64)


    class Meta:
        db_table = 'books_language'

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    ISBN = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='users_images/', blank=True, null=True, default='default_book_img.png')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    pages = models.IntegerField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        db_table = 'books'

    def __str__(self):
        return f'{self.title} - {self.category}'


class Author(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class BookAuthor(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f'{self.book.title} - {self.author.firstname} {self.author.lastname}'


class Reviews(models.Model):
    comment = models.TextField()
    star_given = models.IntegerField(
        default=0,
        validators= [
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'


    def __str__(self):
        return f'{self.comment} {self.book}'