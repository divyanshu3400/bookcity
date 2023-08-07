from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Category(models.Model):
    cate_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cate_name


class Book(models.Model):
    LANGUAGE_CHOICES = (
        ('Hindi', 'Hindi'),
        ('English', 'English'),
    )

    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name='books')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='English')
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return self.book_title


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('book', 'user',)

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
