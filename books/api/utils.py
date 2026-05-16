from datetime import datetime


def calculate_book_age(published_year):
	current_year = datetime.now().year
	return current_year - int(published_year)


def is_archive_book(published_year, threshold=50):
	return calculate_book_age(published_year) >= threshold