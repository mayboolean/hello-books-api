from flask import Blueprint, request
from ..db import db
from ..models.genre import Genre
from .route_utilities import get_models_with_filters, create_model


bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

@bp.get("")
def get_all_genres():
    return get_models_with_filters(Genre, request.args)

@bp.post("")
def create_genre():
    request_body = request.get_json()
    return create_model(Genre, request_body)