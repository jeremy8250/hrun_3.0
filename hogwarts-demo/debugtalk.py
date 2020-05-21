import re
import time

import requests
from bs4 import BeautifulSoup
from httprunner import __version__


def get_httprunner_version():
    return __version__


def sleep(n_secs):
    time.sleep(n_secs)


def get_chartId(html):
    soup = BeautifulSoup(html, 'html.parser')
    pattern = re.compile(r'var chartId = "(.*?)";$')
    script = soup.find("script", text=pattern)
    print(pattern.search(script.text).group(1))
