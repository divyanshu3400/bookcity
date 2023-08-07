from rest_framework import serializers
from .models import Book, Category, Rating

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    cate_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        exclude = ('categories',)

    def get_rating(self, obj):
        ratings = Rating.objects.filter(book=obj)
        if ratings.exists():
            total_ratings = sum(rating.rating for rating in ratings)
            avg_rating = total_ratings / ratings.count()
            return round(avg_rating, 2)
        return None

    def get_cate_name(self, obj):
        return obj.categories.first().cate_name if obj.categories.exists() else None
