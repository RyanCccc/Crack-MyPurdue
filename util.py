def save_tmp_file(str_, path):
    with open(path, 'w') as f:
        f.write(str_)


def load_tmp_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return content


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
