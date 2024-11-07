from flask import Blueprint, request, abort, make_response
from ..models.author import Author
from ..models.book import Book
from ..db import db
from ..routes.route_utilities import validate_model, create_model

bp = Blueprint("authors_bp", __name__, url_prefix='/authors')

@bp.post("")
def create_author():
    request_body = request.get_json()
    return create_model(Author, request_body)

@bp.post("/<author_id>/books")
def create_book_with_author(author_id):
    author = validate_model(Author, author_id)

    request_body = request.get_json()
    request_body["author_id"] = author.id
    return create_model(Book, request_body)



@bp.get("")
def get_all_authors():
    query = db.select(Author)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Author.name.ilike(f"%{name_param}%"))
    
    authors = db.session.scalars(query.order_by(Author.id))
    authors_response = [author.to_dict() for author in authors]

    return authors_response

