from config import app
from routers.favorites_router import favorite


@app.route("/")
def home():
    return "Hello World"


app.register_blueprint(favorite, url_prefix='/favorite')

if __name__ == "__main__":
    app.run(debug=True)
