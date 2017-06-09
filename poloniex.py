import logging
import os
import re
from six.moves.urllib.request import urlopen


from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

# Constant defining number of events to be read at one time.
PAGINATION_SIZE = 3

# Length of the delimiter between individual events.
DELIMITER_SIZE = 2

# Size of events from Wikipedia response.
SIZE_OF_EVENTS = 10

# Constant defining session attribute key for the event index
SESSION_INDEX = 'index'

# Constant defining session attribute key for the event text key for date of events.
SESSION_TEXT = 'text'


@ask.launch
def launch():
    return None


@ask.intent('GetFirstEventIntent', convert={ 'day': 'date' })
def get_first_event():
    return None


@ask.intent('GetNextEventIntent')
def get_next_event():
    return None


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")


@ask.session_ended
def session_ended():
    return "{}", 200


def _get_json_events_from_poloniex():
    return None


def _parse_json(text):
    return None


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
