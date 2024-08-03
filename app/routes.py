from flask import (
    Flask,
    request,
    render_template #help with render all of our HTML files thru python
)
import requests as pyrequests #changes the name requests to pyrequests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")