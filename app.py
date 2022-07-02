from flask import Flask
import flask
from dotenv import load_dotenv
from TranslateService import TranslateService
from flask import request
load_dotenv()

app = Flask(__name__)


@app.route('/')
def getTranslation():
    from_language = request.args.get('from')
    to = request.args.get('to')
    value_to_translate = request.args.get('value_to_translate')

    if value_to_translate and to and from_language:
        values = TranslateService().translate(from_language, to, value_to_translate)
        return flask.jsonify(values)

    return flask.jsonify('You should send three query params', {"value_to_translate": 'string', "to": 'string', "from_language": 'string' })
