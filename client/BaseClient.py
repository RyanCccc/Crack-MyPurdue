import os
import time
import urllib2
import cookielib

from decorators import retry
from settings import (
    COOKIE_PATH,
)
from network.urls import (
    HEADERS,
    LOGIN_URL,
    LOGIN_OK,
    LOGIN_NEXT,
    REGIS_CHECK_URL,
    REGIS_STATUS_CHECK_URL,
    MAIN_URL,
)
from parser.web_parser import css_select
from network.connection import read_url, read_url_and_read
#from util import save_tmp_file


class BaseClient:
    REG_SESSION_COOKIE_NAME = 'CPSESSID'

    def __init__(self, cookie_path=COOKIE_PATH):
        self.cookie_path = cookie_path
        self.cookiejar = cookielib.LWPCookieJar()
        if os.path.exists(self.cookie_path):
            self.load_cookies()
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self.cookiejar)
        )
        self.opener.addheaders = HEADERS

    def _get_uuid(self):
        curr_time = time.time()
        uuid = repr(curr_time).replace('.', '')[:13]
        return uuid

    def login(self, user, pass_):
        if self.check_logged_in():
            print 'You already logged in'
            return True
        uuid = self._get_uuid()
        params = {'user': user, 'pass': pass_, 'uuid': uuid}
        resp = read_url(self, LOGIN_URL, 'POST', params)
        if resp.code != 200:
            raise ClientException('Login Error')
        read_url(self, LOGIN_OK)
        content = read_url_and_read(self, LOGIN_NEXT)
        self.save_cookies()
        welcome_tag = css_select(content, '#welcome')
        return welcome_tag

    @retry(10)
    def get_reg_session(self, ret_code):
        url = REGIS_CHECK_URL + ('?ret_code=%s' % ret_code)
        read_url(self, url)
        self.save_cookies()
        return self.reg_check()

    def reg_check(self):
        content = read_url_and_read(self, REGIS_STATUS_CHECK_URL)
        if 'Registration' in content:
            return True
        else:
            raise ClientException('Registration Check Error')

    def save_cookies(self):
        self.cookiejar.save(
            self.cookie_path,
            ignore_discard=True,
        )

    def load_cookies(self):
        self.cookiejar.load(
            self.cookie_path,
            ignore_discard=True,
            ignore_expires=True
        )

    def check_logged_in(self):
        try:
            content = read_url_and_read(self, MAIN_URL)
        except ClientException as e:
            print e.message
            return False
        welcome_tag = css_select(content, '#welcome')
        return welcome_tag

    def get_cookie(self):
        pass


class ClientException(Exception):
    pass
