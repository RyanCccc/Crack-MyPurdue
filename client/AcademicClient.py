from network import (
    REGIS_STATUS_CHECK_URL,
)
from BaseClient import BaseClient


# Registration status check
class RegistrationCheckClient(BaseClient):
    RET_CODE = {
        'regis_status_check': 'STU_REGSTAT',
    }

    def regis_status_check(self):
        self.get_reg_session(self.RET_CODE['regis_status_check'])
        resp = self.opener.open(REGIS_STATUS_CHECK_URL, 'term_in=201410')
        return resp

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
class ClassControlClient(BaseClient):
    pass


class ClassSearchClient(BaseClient):
    pass


class ScheduleClient(BaseClient):
    pass


class GradeClient(BaseClient):
    pass
