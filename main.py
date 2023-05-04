import itertools
import logging
import textwrap

import requests

from config import CONFIG
from config import USER_URL
from config import setup_logging

setup_logging()

log = logging.getLogger(__name__)


def get_user_data():
    log.debug('getting user data')
    r = requests.get(USER_URL)
    return r.json()


def show_user_info(user_data):
    log.info(
        textwrap.dedent(
            f"""Hi {user_data['name']},
           you are currently at {user_data['ranks']['overall']['name']} 
           with {user_data['codeChallenges']['totalCompleted']} completed katas."""
        )
    )


def get_completed_katas_info():
    log.debug('loading katas data')
    url = fr"{USER_URL}/code-challenges/completed"
    katas_data = []
    for page_num in itertools.count():
        resp_json = requests.get(url, params={'page': page_num}).json()
        katas_data.extend(resp_json['data'])
        if page_num == resp_json['totalPages'] - 1:
            log.debug(f'loaded {len(katas_data)} katas')
            return katas_data


def get_kata_data(session, kata_id):
    url = fr'https://www.codewars.com/kata/{kata_id}/solutions/python'
    params = {'filter': 'me', 'sort': 'best_practice', 'invalids': 'false'}
    r = session.get(url=url, params=params)
    print(r.headers)


if __name__ == '__main__':
    log.info(' START '.center(80, '='))

    user_data = get_user_data()
    show_user_info(user_data)

    # get katas info from public api
    all_katas = get_completed_katas_info()

    # prepare and auth session
    session = requests.Session()
    session.auth = (CONFIG['CW_USERNAME'], CONFIG['CW_PWD'])

    # TODO: use threading to download the data
    data = get_kata_data(session, 'asdf')
