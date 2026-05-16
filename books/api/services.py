from books.models import Book

from .utils import calculate_book_age, is_archive_book


def get_books_grouped_by_age():
	books = Book.objects.all()

	archiv_liste = []
	aktuelle_liste = []

	for book in books:
		book_age = calculate_book_age(book.published_year)
		book_data = {
			"id": book.id,
			"title": book.title,
			"author": book.author,
			"age": book_age,
		}

		if book_age >= 50:
			archiv_liste.append(book_data)
		else:
			aktuelle_liste.append(book_data)

	return {
		"archiv": archiv_liste,
		"aktuell": aktuelle_liste,
	}


def create_book_with_archive_target(title, author, published_year):
	parsed_year = int(published_year)

	if is_archive_book(parsed_year):
		target_list = "archiv_liste"
		final_title = f"[Archiv] {title}"
	else:
		target_list = "aktuelle_liste"
		final_title = title

	book = Book.objects.create(
		title=final_title,
		author=author,
		published_year=parsed_year,
	)

	return {
		"target_list": target_list,
		"book": {
			"id": book.id,
			"title": book.title,
		},
	}
