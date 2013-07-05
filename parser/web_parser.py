from bs4 import BeautifulSoup as BS


def css_select(content, selector):
    bs = BS(content)
    return bs.select(selector)


def get_name(content):
    welcome_tag = content.select('.uportal-label')[0].text
    name = welcome_tag.split(' ')
    first_name = name[1]
    last_name = name[2]
    full_name = first_name + ' ' + last_name
    return first_name, last_name, full_name

def get_table_content(table):
    rows = table.select('tr')[1:]
    result = []
    for row in rows:
        row_content = []
        for cell in row.select('td'):
            row_content.append(cell.text)
        result.append(row_content)
    return result

def parse_regis_status(content):
    table = css_select(content, 'table.datadisplaytable')[0]
    cells = get_table_content(table)
    return cells
