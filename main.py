import logging

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


if __name__ == '__main__':
    log.info(' START '.center(80, '='))
    user_data = get_user_data(CONFIG['CW_USERNAME'])
    log.info(user_data)
