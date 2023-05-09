import itertools
import logging
import textwrap

import requests
from requests_html import HTMLSession

from config import CONFIG
from config import OUTPUT_DIR
from config import USER_URL
from config import setup_logging

setup_logging()

log = logging.getLogger(__name__)


class CodewarsAgent:

    def __init__(self):
        self.session = HTMLSession()
        cookies = parse_cookie_env(CONFIG['CW_COOKIE'])
        self.session.cookies = requests.utils.cookiejar_from_dict(cookies)
        log.debug('Codewars agent prepared')

    def get_user_data(self, url):
        """Fetch user info json from public API."""
        log.debug('getting user data')
        r = self.session.get(url)
        return r.json()

    @staticmethod
    def parse_user_info(user_data):
        """Parse the provided user info into a readable paragraph."""
        return textwrap.dedent(
            f"""Hi {user_data['name']},
           you are currently at {user_data['ranks']['overall']['name']} 
           with {user_data['codeChallenges']['totalCompleted']} completed katas."""
        )

    def get_completed_katas_info(self):
        """Fetch all completed katas info jsons.

        Save it internally for later use.
        """

        log.debug('loading katas data')
        url = fr"{USER_URL}/code-challenges/completed"

        completed_katas = []

        for page_num in itertools.count():
            resp_json = self.session.get(url, params={'page': page_num}).json()
            completed_katas.extend(resp_json['data'])

            if page_num == resp_json['totalPages'] - 1:
                log.debug(f'loaded {len(completed_katas)} katas')
                return completed_katas

    def get_kata_data(self, kata_id):
        """Get description and code for given kata_id."""

        url = fr'https://www.codewars.com/kata/{kata_id}/solutions/python'
        params = {'filter': 'me', 'sort': 'best_practice', 'invalids': 'false'}
        r = self.session.get(url=url, params=params)

        r.html.render(reload=False)

        description = self.parse_description(r)
        code = self.parse_code(r)

        return description, code

    @staticmethod
    def parse_description(response):
        element = response.html.find('#description', first=True)
        return element.text

    @staticmethod
    def parse_code(response):
        element = response.html.find('#solutions_list code', first=True)
        return element.text


def prepare_text_to_write(kata_data, description, code):
    return ''


def save_kata(cw_agent, kata_data):

    description, code = cw_agent.get_kata_data(kata_data['id'])
    text_to_write = prepare_text_to_write(kata_data, description, code)

    with open(OUTPUT_DIR / f"{kata_data['name']}.md", 'w', encoding='utf8') as f:
        f.write(text_to_write)


def parse_cookie_env(cookie):
    return dict(
        element.split('=', maxsplit=1)
        for element in cookie.split('; ')
    )


if __name__ == '__main__':
    log.info(' START '.center(80, '='))

    # prepare online agent
    cw = CodewarsAgent()

    user_data = cw.get_user_data(USER_URL)
    log.info(cw.parse_user_info(user_data))

    # load completed katas info from public api
    completed_katas_info = cw.get_completed_katas_info()

    # TODO: use threading to download the data
    save_kata(cw_agent=cw, kata_data=completed_katas_info[0])
