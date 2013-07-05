#!/usr/bin/env python
import time
import getpass

from client.Exceptions import ClientException
from client.AcademicClient import RegistrationCheckClient
from decorators import retry
from parser.console_parser import parse_opt


def main():
    print 'Hello, this is a myPurdue client'
    print 'Notice, when necessary, we need your username and' + \
          ' password to login, I promise that I will never keep ' + \
          'your information'
    print 'Now, there are following options for you to choose:'
    print '#1 Academic Client\n\n'
    promp_input(Academic)


@retry(3)
def promp_login(client):
    name = client.check_logged_in()
    if not name:
        user = raw_input('Your username:')
        pass_ = getpass.getpass('Your password:')
        name = client.login(user, pass_)
        if not name:
            raise ClientException('Login failed')
        else:
            print 'Successfully log in!!\n'
            print 'Welcome, %s\n' % name[2]
    else:
        print 'Welcome back, %s\n' % name[2]


def promp_input(*args):
    opt = raw_input('#Please choose: ')
    opt = parse_opt(opt)
    execute(opt, *args)


def execute(opt, *args):
    exe_dict = {}
    for i, command in enumerate(args):
        exe_dict[str(i+1)] = command
    exe = exe_dict.get(opt)
    if not exe:
        print 'Please enter right command'
        main()
    process = exe()
    return process


class Academic:
    def __init__(self):
        print 'Hi, welcome to academic tag'
        print 'Please choose following options:'
        print '#1 Check your registration status\n\n'
        promp_input(self.regis_check) 

    def regis_check(self):
        self.client = RegistrationCheckClient()
        promp_login(self.client)
        print 'We are checking your account'
        result = self.client.regis_status_check()
        for i in range(3):
            print '...'
            time.sleep(1)
        print 'Here is your result:'
        print result
