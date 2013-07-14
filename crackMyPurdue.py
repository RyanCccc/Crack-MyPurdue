#!/usr/bin/env python
import time
import getpass

from client.Exceptions import ClientException
from client.AcademicClient import RegistrationCheckClient
from client.BaseClient import BaseClient
from decorators import retry
from parser.console_parser import parse_opt
from util import bcolors

def main():
    print bcolors.HEADER + 'Hello, this is a myPurdue client' + bcolors.ENDC
    print bcolors.HEADER + 'Notice, when necessary, we need your username' + \
        ' and password to login, I promise that I will never keep ' + \
        'your information' + bcolors.ENDC
    client = BaseClient()
    promp_login(client)
    print bcolors.HEADER + 'Now, there are following' + \
        ' options for you to choose:' + bcolors.ENDC
    print bcolors.OKBLUE + '#1 Academic Client' + bcolors.ENDC
    promp_input(Academic, client=client)


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
            print bcolors.OKGREEN + 'Successfully log in!!' + bcolors.ENDC
            print bcolors.OKGREEN + 'Welcome, %s' % name[2] + bcolors.ENDC
    else:
        print bcolors.OKGREEN + 'Welcome back, %s' % name[2] + bcolors.ENDC


def promp_input(*args, **kwargs):
    opt = raw_input(bcolors.OKBLUE + '#Please choose: ' + bcolors.ENDC)
    opt = parse_opt(opt)
    execute(opt, *args, **kwargs)


def execute(opt, *args, **kwargs):
    exe_dict = {}
    for i, command in enumerate(args):
        exe_dict[str(i+1)] = command
    try:
        exe = exe_dict.get(opt)
    except:
        exe = None
    if not exe:
        print bcolors.WARNING + 'Please enter right command' + bcolors.ENDC
        main()
    process = exe(**kwargs)
    return process


class Academic:
    def __init__(self, client=None):
        print bcolors.HEADER + 'Hi, welcome to academic tag' + bcolors.ENDC
        print bcolors.HEADER + 'Please choose following options:' + bcolors.ENDC
        print bcolors.OKBLUE + '#1 Check your registration status' + bcolors.ENDC
        if client:
            self.client = RegistrationCheckClient(client=client)
        promp_input(self.regis_check)

    def regis_check(self):
        print bcolors.OKGREEN + 'We are checking your account' + bcolors.ENDC
        result = self.client.regis_status_check()
        for i in range(3):
            print '...'
            time.sleep(1)
        print bcolors.OKGREEN + 'Here is your result:' + bcolors.ENDC
        print result
        self.__init__()

main()
