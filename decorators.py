import time
from decorator import decorator


@decorator
def retry(f, *args, **kwargs):
    success = False
    while not success:
        try:
            return f(*args, **kwargs)
            success = True
        except Exception as e:
            print e.message
            success = False
            print 'Retrying'
            time.sleep(10)
