from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Author(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name
        )

    @classmethod
    def from_dict(cls, author_data):
        new_author = cls(name=author_data["name"])
        return new_author
