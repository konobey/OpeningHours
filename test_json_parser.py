import json
from unittest import TestCase
from json_parser import json_parser, get_formatted_str, JsonParserException


def get_result(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        parsed_json = json.load(file)
        result = json_parser(parsed_json)

    return get_formatted_str(result)


class TestJsonParser(TestCase):

    def test_json_parser(self):
        result = get_result('data/testcase1.json')
        valid_result = ("Monday: Closed\n"
                        "Tuesday: 10 AM - 6 PM\n"
                        "Wednesday: Closed\n"
                        "Thursday: 10 AM - 6 PM\n"
                        "Friday: 10 AM - 1 AM\n"
                        "Saturday: 10 AM - 1 AM\n"
                        "Sunday: 12 PM - 9 PM")

        self.assertEqual(result, valid_result)

    def test_sunday_monday(self):
        result = get_result('data/testcase2.json')
        valid_result = ("Monday: Closed\n"
                        "Tuesday: Closed\n"
                        "Wednesday: Closed\n"
                        "Thursday: Closed\n"
                        "Friday: Closed\n"
                        "Saturday: Closed\n"
                        "Sunday: 12 PM - 1 AM")

        self.assertEqual(result, valid_result)

    def test_double_open_hours(self):
        result = get_result('data/testcase3.json')
        valid_result = ("Friday: 6 PM - 1 AM\n"
                        "Saturday: 9 AM - 11 AM, 4 PM - 11 PM")

        self.assertEqual(result, valid_result)

    def test_invalid_input_raise_exception(self):
        with open('data/testcase4.json', 'r', encoding='utf-8') as file:
            parsed_json = json.load(file)

        self.assertRaises(JsonParserException, json_parser, parsed_json)