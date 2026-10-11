from book import Book

library = [
     Book("The Witcher", "Andjey Sapkowsky"),
     Book("Shadow in Paradise", "Erich-Maria Remark"),
     Book("Idiot", "Fedor Dostoevskiy")
    ]

for book in library:
    print(f"{book.tittle} - {book.author}")
