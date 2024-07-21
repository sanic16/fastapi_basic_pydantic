class Book:
    id: int
    title: str 
    author: str
    description: str
    rating: int
    published_year: int 

    def __init__(self, id, title, author, description, rating, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year

BOOKS = [
    Book(1, 'Amor en tiempos de pandemia', 'Gabi Martínez', 'Una historia de amor en tiempos de pandemia', 5, 2020),
    Book(2, 'El arte de la guerra', 'Sun Tzu', 'Un tratado militar escrito por Sun Tzu', 5, 2021),
    Book(3, 'El principito', 'Antoine de Saint-Exupéry', 'Un cuento infantil con muchas enseñanzas', 5, 1954),
    Book(4, 'La hija del puma', 'Monica Zak', 'Una historia de drama en Guatemala', 5, 2004),
    Book(5, 'Python Crash Course', 'Eric Matthes', 'Un libro para aprender Python', 5, 2015),
    Book(6, 'El código Da Vinci', 'Dan Brown', 'Una novela de misterio y suspenso', 3, 1999),
    Book(7, 'El alquimista', 'Paulo Coelho', 'Una novela de aventuras y misterio', 4, 1995),
    Book(8, 'El amor en los tiempos del cólera', 'Gabriel García Márquez', 'Una historia de amor en Colombia', 2, 1985),
]

def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    
    return book

def find_book_index(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book 