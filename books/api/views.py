from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from books.models import Book
from datetime import datetime

class BookArchiveView(APIView):
    def get(self, request):
        books = Book.objects.all()
        current_year = datetime.now().year
        
        archiv_liste = []
        aktuelle_liste = []

        for book in books:
            age = current_year - book.published_year
            book_data = {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "age": age
            }
            
            if age >= 50:
                archiv_liste.append(book_data)
            else:
                aktuelle_liste.append(book_data)

        return Response({
            "archiv": archiv_liste,
            "aktuell": aktuelle_liste
        })

    def post(self, request):
        title = request.data.get('title')
        author = request.data.get('author')
        published_year = request.data.get('published_year')

        if not all([title, author, published_year]):
            return Response({"error": "Daten unvollständig"}, status=400)

        current_year = datetime.now().year
        age = current_year - int(published_year)

        if age >= 50:
            target_list = "archiv_liste"
            final_title = f"[Archiv] {title}"
        else:
            target_list = "aktuelle_liste"
            final_title = title

        book = Book.objects.create(
            title=final_title,
            author=author,
            published_year=published_year
        )

        return Response({
            "target_list": target_list,
            "book": {"id": book.id, "title": book.title}
        }, status=status.HTTP_201_CREATED)