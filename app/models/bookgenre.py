from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class BookGenre(db.Model):
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), primary_key=True)
    