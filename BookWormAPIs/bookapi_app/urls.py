from django.urls import path
from bookapi_app import views
from django.conf.urls.static import static
from BookWormAPIs import settings

urlpatterns = [
    path('api/books/', views.AllBooksAPIView.as_view(), name='all-books'),
    path('api/books/<int:book_id>/', views.BookDetailsAPIView.as_view(), name='book-details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)