from decorator import decorator

from client.BaseClient import ClientException


@decorator
def retry(f, *args):
    success = False
    while not success:
        try:
            return f(*args)
            success = True
        except ClientException as e:
            print e.message
            success = False
