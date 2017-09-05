import  socket

_dnscaache = {}

def _setDNSCache():
    def _getaddrinfo(*args, **kwargs):
        global  _dnscaache
        if args in _dnscaache:
            return  _dnscaache[args]
        else:
            _dnscaache[args] = socket._getaddrinfo(*args, **kwargs)
            return  _dnscaache[args]

    if not hasattr(socket, '_getaddrinfo'):
        socket._getaddrinfo = socket.getaddrinfo
        socket.getaddrinfo = _getaddrinfo

def test():
    _setDNSCache()

    import  requests

    urlStr  = 'https://www.baidu.com'
    r1 = requests.get(urlStr)
    print('第一次命中缓存时间: ' + str(r1.elapsed.microseconds))
    r2 = requests.get(urlStr)
    print('第二次命中缓存时间: ' + str(r2.elapsed.microseconds))

test()