import re

def parse_opt(opt):
    r = re.compile('[0-9]+')
    m = r.search(opt)
    return m.group()
