# imports app from app.__init__
# app declared in __init__  as app = Flask(__name__)
from app import app

if __name__ == "__main__":
    app.run(debug=True)