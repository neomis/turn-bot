from loguru import logger
import requests as req
from flask import Flask, request, jsonify
from turn_bot.config_local import WEBHOOK_TOKEN, DISCORD_SERVER, USER_LIST, HOST, PORT


app = Flask(__name__)


@app.route('/new_turn', methods=['POST'])
def new_turn():
    verify_token = request.args.get('verify_token')
    if(verify_token != WEBHOOK_TOKEN):
        return jsonify({'status': 'bad token'}), 401
    try:
        # content = request.json
        steam_name = request['value2']
        turn_number = request['value3']
        game_name = request['value1']
        discord_name = steam_name
        if(steam_name in USER_LIST):
            discord_name = '<@' + USER_LIST[steam_name] + '>'
        msg = "Hey " + discord_name + ", it's your turn in game: " + game_name + " (turn # " + str(turn_number) + ")."
        r = req.post(DISCORD_SERVER, data={"content": msg})
        logger.debug(r.status_code)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'content': 'Python Error Contact Justin'}), 400


def main():
    logger.debug("HOST: " + HOST)
    logger.debug("PORT: " + str(PORT))
    logger.debug("TOKEN: " + WEBHOOK_TOKEN)
    app.run(host=HOST, port=PORT)
