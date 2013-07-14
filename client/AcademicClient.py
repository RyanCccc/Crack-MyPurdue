from network.connection import read_url, read_url_and_read
from network.urls import (
    REGIS_STATUS_CHECK_URL,
)
from parser.web_parser import parse_regis_status
from BaseClient import BaseClient
from client.Exceptions import *


class RegistrationCheckClient:
    RET_CODE = {
        'regis_status_check': 'STU_REGSTAT',
    }

    def __init__(self, client):
        self.client = client

    def regis_status_check(self):
        self.client.get_reg_session(self.RET_CODE['regis_status_check'])
        param = {'term_in': '201410'}
        resp = read_url(self.client, REGIS_STATUS_CHECK_URL, 'POST', param)
        content = resp.read()
        try:
            result = parse_regis_status(content)
        except:
            raise RegisCheckClientException('Regis Status Check Failed')
        return result

    def regis_history_check(self):
        pass

    def regis_classes_check(self):
        #check current regis classes
        pass

    def regis_pin_check(self):
        pass

    def save_pin(self):
        pass

    def load_pin(self):
        pass


# Add and drop class
class ClassControlClient:
    pass


class ClassSearchClient:
    pass


class ScheduleClient:
    pass


class GradeClient:
    pass
