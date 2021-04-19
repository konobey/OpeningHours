from flask import Flask, request
from json_parser import json_parser, get_formatted_str, JsonParserException

app = Flask(__name__)


@app.route('/check-health', methods=['GET'])
def check_health():
    return {"health_status": "running"}, 200


@app.route('/open-hours', methods=['POST'])
def open_hours():
    try:
        request_data = request.get_json()
        result = json_parser(request_data)
    except JsonParserException as error:
        app.logger.error("JSON content is not valid: %s", error)
        return "JSON content is invalid", 400
    else:
        return get_formatted_str(result), 200
