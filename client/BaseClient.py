import os
import time
import urllib2
import cookielib

from settings import (
    COOKIE_PATH,
)
from network import (
    HEADERS,
    LOGIN_URL,
    REGIS_CHECK_URL,
    REGIS_STATUS_CHECK_URL,
    MAIN_URL,
)
from network.url import read_url, read_url_and_read
from util import save_tmp_file


class Client:
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
        self.save_cookies()
        return resp.code == 200

    def reg_check(self):
        read_url(self, REGIS_CHECK_URL)
        self.save_cookies()
        content = read_url_and_read(self, REGIS_STATUS_CHECK_URL)
        if 'Registration' in content:
            return True
        else:
            raise ClientException('Registration Check Error')

    def regis_status_check(self):
        resp = self.opener.open(REGIS_STATUS_CHECK_URL, 'term_in=201410')
        return resp

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
            resp = read_url(self, MAIN_URL)
        except ClientException as e:
            print e.message
            return False
        return resp.code == 200


class ClientException(Exception):
    pass
