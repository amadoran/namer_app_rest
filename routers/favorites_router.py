from models.favorites import Favorites, favorites_schema, favorite_schema
from flask import Blueprint, request, jsonify
from config import db

favorite = Blueprint("favorite", __name__)


@favorite.route("/save", methods=["POST"])
def create_favorite():
    first = request.json['first']
    second = request.json['second']
    new_pair = Favorites(first=first, second=second)
    db.session.add(new_pair)
    db.session.commit()

    return favorite_schema.jsonify(new_pair), 201


@favorite.route("/get")
def get_favorites():
    favorites = db.session.execute(db.select(Favorites)).scalars().all()
    result = favorites_schema.dump(favorites)
    return jsonify(result)


@favorite.route("/get/<int:id>")
def get_favorite(id):
    favorite_select = db.get_or_404(Favorites, id)
    result = favorite_schema.dump(favorite_select)
    return jsonify(result)


@favorite.route("/delete/<int:id>", methods=["DELETE"])
def delete_favorite(id):
    deleted = db.get_or_404(Favorites, id)
    db.session.delete(deleted)
    db.session.commit()
    return favorite_schema.jsonify(deleted), 200

