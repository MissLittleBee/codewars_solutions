import itertools
import logging
import textwrap

from requests_html import HTMLSession

from config import CONFIG
from config import OUTPUT_DIR
from config import USER_URL
from config import setup_logging

setup_logging()

log = logging.getLogger(__name__)


def get_user_data(session):
    log.debug('getting user data')
    r = session.get(USER_URL)
    return r.json()


def show_user_info(user_data):
    log.info(
        textwrap.dedent(
            f"""Hi {user_data['name']},
           you are currently at {user_data['ranks']['overall']['name']} 
           with {user_data['codeChallenges']['totalCompleted']} completed katas."""
        )
    )


def get_completed_katas_info(session):
    log.debug('loading katas data')
    url = fr"{USER_URL}/code-challenges/completed"
    katas_data = []
    for page_num in itertools.count():
        resp_json = session.get(url, params={'page': page_num}).json()
        katas_data.extend(resp_json['data'])
        if page_num == resp_json['totalPages'] - 1:
            log.debug(f'loaded {len(katas_data)} katas')
            return katas_data


def parse_description(response):
    element = response.html.find('#description', first=True)
    return element.text


def parse_code(response):
    element = response.html.find('#solutions_list code', first=True)
    return element.text


def prepare_text_to_write(kata_data, description, code):
    return ''


def get_kata_data(session, kata_data):
    url = fr'https://www.codewars.com/kata/{kata_data["id"]}/solutions/python'
    params = {'filter': 'me', 'sort': 'best_practice', 'invalids': 'false'}
    r = session.get(url=url, params=params)

    description = parse_description(r)
    code = parse_code(r)

    return description, code


def save_kata(session, kata_data):
    description, code = get_kata_data(session, kata_data)
    text_to_write = prepare_text_to_write(kata_data, description, code)
    with open(OUTPUT_DIR / f"{kata_data['name']}.md", 'w', encoding='utf8') as f:
        f.write(text_to_write)


if __name__ == '__main__':
    log.info(' START '.center(80, '='))

    # prepare and auth session
    session = HTMLSession()
    session.auth = (CONFIG['CW_USERNAME'], CONFIG['CW_PWD'])

    user_data = get_user_data(session)
    show_user_info(user_data)

    # get katas info from public api
    all_katas = get_completed_katas_info(session)

    # TODO: use threading to download the data
    save_kata(session, all_katas[0])
