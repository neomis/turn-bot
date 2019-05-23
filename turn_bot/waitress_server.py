from turn_bot.config_local import URL_PREFIX, HOST, PORT
from waitress import serve
from turn_bot.webhooks import app
from loguru import logger


def main():
    logger.debug("HOST: " + HOST)
    logger.debug("PORT: " + str(PORT))
    logger.debug("PREFIX: " + str(URL_PREFIX))
    serve(app, host=HOST, port=PORT, url_prefix=URL_PREFIX)
