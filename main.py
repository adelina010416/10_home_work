from flask import Flask
from functions import get_all, get_by_pk, get_by_skill


app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_all()
    result = "<br>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += '<br>'
    return f"<pre> {result} </pre>"


@app.route("/candidates/<int:pk>")
def profile(pk):
    candidate = get_by_pk(pk)
    picture = f"<img src='{candidate['picture']}'>"
    result = "<br>" + candidate["name"] + "<br>" + candidate['position'] + "<br>" + candidate['skills'] + "<br>"
    return f"{picture} <pre> {result} </pre>"


@app.route("/skills/<skill>")
def skills(skill):
    candidates = get_by_skill(skill)
    result = "<br>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += '<br>'
    return f"<pre> {result} </pre>"


if __name__ == "__main__":
    app.run(debug=True)
