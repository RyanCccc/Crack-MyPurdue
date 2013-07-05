import time
from client.Exceptions import *
from decorator import decorator

def retry(wait=3):
    @decorator
    def with_retry(f, *args, **kwargs):
        success = False
        while not success:
            try:
                return f(*args, **kwargs)
                success = True
            except LogInException as e:
                print e.message
                success = False
                print 'Retrying'
                time.sleep(wait)
    return with_retry
