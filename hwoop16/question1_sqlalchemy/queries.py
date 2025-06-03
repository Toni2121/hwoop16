from db import Session, engine
from models import Book, Base

Base.metadata.create_all(bind=engine)


def insert_books():
    session = Session()
    books = [
        Book(title="Harry Potter and the Sorcerer's Stone", price=89.90),
        Book(title="The Little Prince", price=45.50),
        Book(title="1984", price=79.90),
        Book(title="Les Misérables", price=99.00),
        Book(title="Crime and Punishment", price=69.90),
    ]
    session.add_all(books)
    session.commit()
    session.close()


def print_all_books():
    session = Session()
    books = session.query(Book).all()
    for book in books:
        print(book.id, book.title, float(book.price))
    session.close()
