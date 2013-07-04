#!/usr/bin/env python
import getpass

from client.BaseClient import BaseClient
from client.BaseClient import ClientException
from decorators import retry

def main():
    client = BaseClient()
    if not client.check_logged_in():
        promp_login(client)


@retry
def promp_login(client):
    user = raw_input('Your username:')
    pass_ = getpass.getpass('Your password:')
    if not client.login(user, pass_):
        raise ClientException('Login failed')
    else:
        print 'Successfully log in!!'
