import lxml


def remove_all_whitespace(text):
    '''
    Given text, remove all whitespace
    >>> remove_all_whitespace('   foo   bar   ')
    'foo bar'
    '''
    return ' '.join(text.split())


def css_select(content, selector):
    '''
    Search HTML `content` for the given css `selector` and return the matching
    elements.
    '''
    cache_attr = '_lxml'
    doc = getattr(content, cache_attr, None)
    if doc is None:
        doc = lxml.html.fromstring(str(content))
    return doc.cssselect(selector)


def css_select_get_table(
        content, selector, row_selector='tbody tr', only_text=True):
    '''
    Given HTML `content`, return the text associated with the table `selector`.

    For example:
    >>> content = """
    ...  <table>
    ...     <tbody>
    ...         <tr>
    ...             <td>Foo</td>
    ...             <td>bar</td>
    ...         </tr>
    ...         <tr>
    ...             <td>Moo</td>
    ...             <td>cow</td>
    ...         </tr>
    ...     </tbody>
    ... </table>"""
    >>> css_select_get_table(content, 'table')
    [['Foo', 'bar'], ['Moo', 'cow']]
    >>> css_select_get_table('', 'table')
    >>> css_select_get_table('<b>foo</b>', 'table')
    '''
    if not content:
        return None
    result = css_select(content, selector)
    if not result:
        return None
    table = result[0]
    rows = []
    for tr in table.cssselect(row_selector):
        row = [
            remove_all_whitespace(cell.text_content()) if only_text else cell
            for cell in tr
        ]
        rows.append(row)
    return rows


def css_select_get_text(content, selector, strip_ws=True):
    '''
    Search HTML `content` for the given css `selector` and return only the
    text. If `strip_ws` is True, then the text will be stripped of whitespace,
    otherwise whitespace is preserved.
    >>> content = "Foo bar <b>Moo</b> cow"
    >>> css_select_get_text('<div>' + content + '</div>', 'div')
    ['Foo bar Moo cow']
    >>> content = """
    ...  <table>
    ...     <tbody>
    ...         <tr>
    ...             <td>Foo</td>
    ...             <td>bar</td>
    ...         </tr>
    ...         <tr>
    ...             <td>Moo</td>
    ...             <td>cow</td>
    ...         </tr>
    ...     </tbody>
    ... </table>"""
    >>> css_select_get_text(content, 'td')
    ['Foo', 'bar', 'Moo', 'cow']
    >>> css_select_get_text(content, 'tr')
    ['Foo bar', 'Moo cow']
    >>> css_select_get_text(content, 'table')
    ['Foo bar Moo cow']
    '''
    result = css_select(content, selector)
    func = lambda x: x
    if strip_ws:
        func = remove_all_whitespace
    return [func(el.text_content()) for el in result]
