from bs4 import BeautifulSoup as BS


def css_select(content, selector):
    bs = BS(content)
    return bs.select(selector)
