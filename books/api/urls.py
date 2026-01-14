from django.urls import path, include

from .views import BookArchiveView

urlpatterns = [
    path('books/', BookArchiveView.as_view(), name='book-archive'),
]
