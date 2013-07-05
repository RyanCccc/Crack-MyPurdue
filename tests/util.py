import os
from subprocess import Popen
from tests import TEST_HTML_PATH


def save_test_file(str_, filename):
    path = get_file_path(filename)
    with open(path, 'w') as f:
        f.write(str_)


def load_test_file(filename):
    path = get_file_path(filename)
    with open(path, 'r') as f:
        content = f.read()
    return content


def get_file_path(filename):
    return os.path.join(TEST_HTML_PATH, filename)


def open_test_html_file(filename):
    path = get_file_path(filename)
    commands = ['firefox', path]
    return Popen(commands)
