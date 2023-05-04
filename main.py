import logging
import textwrap

import requests

from config import CONFIG
from config import setup_logging

setup_logging()

log = logging.getLogger(__name__)


def get_user_data(username):
    log.debug('getting user data')
    user_url = fr"{CONFIG['API_URL']}users/{username}"
    r = requests.get(user_url)
    return r.json()


def show_user_info(user_data):
    log.info(textwrap.dedent(f"""
        Hi {user_data['name']},
        you are currently at {user_data['ranks']['overall']['name']} 
        with {user_data['codeChallenges']['totalCompleted']} completed katas.
    """))


if __name__ == '__main__':
    log.info(' START '.center(80, '='))
    user_data = get_user_data(CONFIG['CW_USERNAME'])
    show_user_info(user_data)
