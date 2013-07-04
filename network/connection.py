from urllib import urlencode as parse


def read_url(client, url, method='GET', data=None):
    if data:
        data = parse(data)
    if method == 'GET' and data:
        url += '?' + data
        resp = client.opener.open(url)
    elif method == 'POST':
        resp = client.opener.open(url, data)
    else:
        resp = client.opener.open(url)
    return resp


def read_url_and_read(client, url, method='GET', data=None):
    resp = read_url(client, url, method, data)
    content = resp.read()
    resp.close()
    return content
