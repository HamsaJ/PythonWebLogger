from quart import Blueprint, request, jsonify
import sys
import logging
import logging.handlers

routesBlueprint = Blueprint("routes", __name__)


def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


@routesBlueprint.route("/", methods=["GET"])
async def index():
    result = jsonify({"greetings": "Welcome"})
    logging.debug("route1()")
    return result


@routesBlueprint.route("/logs", methods=["GET"])
async def logs():
    r = open("src/logs/requests.log")
    logs = list()
    for piece in read_in_chunks(r):
        logs.append(piece)

    return jsonify({"logs": logs})
