# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse




class BookDetailsAPIView(APIView):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)
        
        
class AllBooksAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)
    

def filtered_books_view(request):
    category = request.data.get('category', None)

    if category:
        books = Book.objects.filter(categories__name=category)
    else:
        books = Book.objects.all()

    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

