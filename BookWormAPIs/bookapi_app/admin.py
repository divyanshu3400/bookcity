from django.contrib import admin
from .models import Book, Category, Rating, Comment
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'book_author', 'price', 'language']
    
admin.site.register(Book, BookAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_name']
    
admin.site.register(Category, CategoryAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating']
    
admin.site.register(Rating, RatingAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at']
    
admin.site.register(Comment, CommentAdmin)