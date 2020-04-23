from quart import Quart

from routes import routesBlueprint
import logging
import logging.handlers

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    "src/logs/requests.log", maxBytes=3000000, backupCount=2
)
formatter = logging.Formatter(
    "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logging.getLogger().addHandler(logging.StreamHandler())

logging.debug("started app")

server = Quart(__name__)
server.register_blueprint(routesBlueprint)
server.run(debug=True)
