import os

import sentry_sdk

from bottle import run, route, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn='https://e6095e423d5b4d80bf7dc7f4a044a171@o504246.ingest.sentry.io/5591127',
    integrations=[BottleIntegration()]
)


@route("/")
def hello_page():
    return HTTPResponse(status=200, body="Приветик!")


@route('/fail')
def index_fail():
    raise RuntimeError("Ошибка!")


@route('/success')
def index_success():
    return HTTPResponse(status=200, body="200 OK")


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)