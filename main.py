import json
import logging
from json_parser import json_parser, get_formatted_str, JsonParserException

logging.basicConfig(level=logging.INFO,
                    format=u'%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s')

if __name__ == '__main__':
    with open('data/testcase4.json', 'r', encoding='utf-8') as file:
        parsed_json = json.load(file)
        try:
            result = json_parser(parsed_json)
            print(get_formatted_str(result))
        except JsonParserException as error:
            logging.error("JSON content is not valid: %s", error)

