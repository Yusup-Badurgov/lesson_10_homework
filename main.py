from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route('/')
def get_all_candidates():
    candidates = get_all()
    result = "<br>"

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f"<pre> {result} </pre>"


@app.route('/candidates/<int:pk>')
def get_candidate(pk):
    candidate = get_by_pk(pk)
    result = "<br>"

    if candidate == None:
        return f'<h1>А вот нету такого кондитата<h1>'

    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    return f"""
    <img src={candidate['picture']}>
    <pre>{result}</pre>
    """


@app.route('/skills/<skill_name>')
def get_candidate_by_skill(skill_name):
    candidates = get_by_skill(skill_name)
    result = "<br>"

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f"<pre> {result} </pre>"

app.run()

