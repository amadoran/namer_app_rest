from config import app, db, ma


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(45))
    second = db.Column(db.String(45))


with app.app_context():
    db.create_all()


class FavoritesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Favorites

    id = ma.auto_field()
    first = ma.auto_field()
    second = ma.auto_field()


favorite_schema = FavoritesSchema()
favorites_schema = FavoritesSchema(many=True)
