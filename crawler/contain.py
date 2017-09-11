#coding=utf-8
from  crawler.URL import  URL

def is_contain_list(lista, listb):
    if not isinstance(lista, list) or not isinstance(listb, list):
        return  False

    a_len = len(lista)
    b_len = len(listb)

    if a_len != b_len:
        return False

    if a_len >=  b_len:
        tmp = lista
        lista  = listb
        listb = tmp

    count = 0

    for item in lista:
        if item in listb:
            count += 1
    if count == a_len and count <= b_len:
        return True
    else:
        return False


def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

def is_similar_url(urla1, urlb2):

    urla = URL(urla1)
    urlb = URL(urlb2)


    hosta = urla.get_host()
    hostb = urlb.get_host()

    porta = urla.get_port()
    portb = urlb.get_port()

    patha = urla.get_path()
    pathb = urlb.get_path()

    if patha.count('/') < 2:
        return True

    patha1 = txt_wrap_by('/', '/', patha)
    pathb1 = txt_wrap_by('/', '/', pathb)

    if  hosta == hostb and porta == portb and patha1 == pathb1:
        return True
    else:
        return False
