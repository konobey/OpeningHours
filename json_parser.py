import logging
from datetime import datetime
from collections import defaultdict

logging.basicConfig(level=logging.INFO,
                    format=u'%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s')


class JsonParserException(Exception):
    """Generic exception class for json parsing functionality"""
    pass


def json_parser(rest_schedule_json):
    """
    Parsing JSON string with the opening hours info. Input JSON string consist of keys
    indicating days of a week and corresponding opening hours as values.
    One JSON file includes data for one restaurant.
        {
        'dayofweek': 'opening hours'
        'dayofweek': 'opening hours'
        ...
        }
    <dayofweek> : monday / tuesday / wednesday / thursday / friday / saturday / sunday
    <opening hours> : an array of objects containing opening hours. Each object consist of
    two keys:
        * type : open or close
        * value : opening / closing time as UNIX time

    :param rest_schedule_json: input json in the dict form

    :returns: Restaurant opening hours
    :rtype: dict
    """
    result_schedule = defaultdict(list)

    hours_stack = []
    prev_type = None
    for weekday, opening_hours in rest_schedule_json.items():
        is_open = False
        for hour in opening_hours:
            if prev_type == hour["type"]:
                # Types "open"/"close" should not repeat
                raise JsonParserException("Types open/close should not repeat")
            if hour["type"] == "open":
                # Put the open hour to the stack
                hours_stack.append({"weekday": weekday, "value": hour["value"]})
                is_open = True
            else:
                if len(hours_stack) > 0:
                    # If we found close hour type - pop corresponding open hour from the stack
                    open_hour = hours_stack.pop()
                    close_hour_val = hour['value']
                    result_schedule[open_hour['weekday']].append(
                        f"{datetime.utcfromtimestamp(open_hour['value']).strftime('%-I %p')} - "
                        f"{datetime.utcfromtimestamp(close_hour_val).strftime('%-I %p')}")
                else:
                    hours_stack.append({"weekday": weekday, "value": hour["value"]})

            prev_type = hour["type"]

        # Check if the restaurant haven't had any "open" hours
        if not is_open:
            result_schedule[weekday].append("Closed")

    if len(hours_stack) > 0:
        if len(hours_stack) == 2:
            # Processing the case Sunday-close / Monday-open
            open_hour = hours_stack.pop()
            close_hour = hours_stack.pop()
            result_schedule[open_hour['weekday']].append(
                f"{datetime.utcfromtimestamp(open_hour['value']).strftime('%-I %p')} - "
                f"{datetime.utcfromtimestamp(close_hour['value']).strftime('%-I %p')}")

        else:
            raise JsonParserException("No corresponding open type in Sunday")

    return result_schedule


def get_formatted_str(result_schedule):
    """
    Format dictionary with the parsed restaurant schedule into human readable string

    :param result_schedule:
    :return: formatted string
    """
    return "\n".join([f"{weekday.title()}: {', '.join(hours)}"
                      for weekday, hours in result_schedule.items()])
