from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Genre(db.model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

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