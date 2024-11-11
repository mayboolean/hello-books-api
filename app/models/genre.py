from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Genre(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    books: Mapped[list["Genre"]] = relationship(secondary="book_genres", back_populates="genres")

    # instance to dict representation
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
    # dict to instance
    @classmethod
    def from_dict(cls, genre_data):
        new_genre = cls(name=genre_data["name"])
        return new_genre