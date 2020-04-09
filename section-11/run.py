from app import app
from db import db

db.init_app(app)


@app.before_first_request
def before_first_request():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
