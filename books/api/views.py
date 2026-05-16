from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import get_books_grouped_by_age, create_book_with_archive_target

class BookArchiveView(APIView):
    def get(self, request):
        grouped_books = get_books_grouped_by_age()
        return Response(grouped_books)

    def post(self, request):
        title = request.data.get('title')
        author = request.data.get('author')
        published_year = request.data.get('published_year')

        if any(value in (None, '') for value in [title, author, published_year]):
            return Response({"error": "Daten unvollständig"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = create_book_with_archive_target(
                title=title,
                author=author,
                published_year=published_year,
            )
        except ValueError:
            return Response(
                {"error": "published_year muss eine Zahl sein"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(result, status=status.HTTP_201_CREATED)