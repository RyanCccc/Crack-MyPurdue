#!/usr/bin/env python
import time
from urllib import urlencode as parse
import urllib2
import cookielib
import json,os,sys,re,hashlib

HEADERS = [
           ('Content-Type', 'application/x-www-form-urlencoded'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'wl.mypurdue.purdue.edu'),
           ('Referer', 'https://wl.mypurdue.purdue.edu/cp/home/displaylogin'),
           ('User-Agent', 'Mozilla/5.0'),
          ]
NEXT_URL = "https://wl.mypurdue.purdue.edu/cp/home/next"
LOG_OK_URL = "https://wl.mypurdue.purdue.edu/cps/welcome/loginok.html"
LOGIN_URL = 'https://wl.mypurdue.purdue.edu/cp/home/login'
ACADEMIC_URL = 'https://wl.mypurdue.purdue.edu/tag.f8306bcb89e9dacf.render.userLayoutRootNode.uP?uP_root=root&uP_sparam=activeTab&activeTab=u12l1s2&uP_tparam=frm&frm'
REGIS_TERM_URL = 'https://wl.mypurdue.purdue.edu/cp/ip/login?sys=sctssb&url=https://selfservice.mypurdue.purdue.edu/prod/tzwkwbis.P_CheckAgreeAndRedir?ret_code=STU_REGSTAT'
REGIS_STATUS_CHECK_URL = 'https://selfservice.mypurdue.purdue.edu/prod/bwskrsta.P_RegsStatusDisp'
class Client:
    def __init__(self):
        self.cookiejar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiejar))
        self.opener.addheaders = HEADERS
    def _get_uuid(self):
        curr_time = time.time()
        uuid = repr(curr_time).replace('.','')[:13]
        return uuid
    def login(self, user, pass_):
        uuid = self._get_uuid()
        data = parse({'user':user, 'pass':pass_, 'uuid':uuid})
        fp = self.opener.open(LOGIN_URL, data) 
        resp = fp.read()
        fp.close()
        if LOG_OK_URL in resp:
            fp = self.opener.open(LOG_OK_URL) 
            resp = fp.read()
            fp.close()
        else:
            print "failed to login"
            return False
        if NEXT_URL in resp:
            fp = self.opener.open(NEXT_URL) 
        return fp.code
    def goto_Academic(self):
        resp = self.opener.open(ACADEMIC_URL)
        content = resp.read()
        if 'Academic' in content:
            return True
        else:
            return content
    def goto_Reg_check(self):
        resp = self.opener.open(REGIS_TERM_URL)
        content = resp.read()
        resp = self.opener.open(REGIS_STATUS_CHECK_URL)
        content = resp.read()
        if 'Registration' in content:
            return True
        else:
            return content
    def regis_status_check(self):
        resp = self.opener.open(REGIS_STATUS_CHECK_URL, 'term_in=201410')
        return resp
