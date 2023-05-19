from flask import Flask
import flask
from dotenv import load_dotenv
from TranslateService import TranslateService
from flask import request
load_dotenv()

app = Flask(__name__)


@app.get("/")
def getTranslation():
    from_language = request.args.get('from')
    to = request.args.get('to')
    value_to_translate = request.args.get('text')
    if value_to_translate and to and from_language:
        values = TranslateService.translate(from_language, to, value_to_translate)
        return flask.jsonify(values)

    return flask.jsonify('You should send three query params', {"translate": 'string', "to": 'string', "from": 'string' })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
