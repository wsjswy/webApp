
from  urllib import parse


DEFAULT_ENCODING = "utf-8"

class URL:
    def __init__(self, url, encoding = DEFAULT_ENCODING):
        self._unicode_url = None
        self._change = False
        self._encoding = encoding

        if not url.startswith("https://") and not url.startswith("http://"):
            url = "http://" + url

        urlres = parse.urlparse(url)
        self.scheme = urlres.scheme

        if urlres.port is None:
            self.port = 80
        else:
            self.port = urlres.port

        if urlres.netloc.find(":") > -1:
            self.netloc = urlres.netloc
        else:
            self.netloc = urlres.netloc + ":" + str(self.port)

        self.path = urlres.path
        self.params = urlres.params
        self.qs = urlres.query
        self.fragment = urlres.fragment

    def get_domain(self):
        return  self.netloc.split(':')[0]

    def get_host(self):
        return  self.netloc.split(':')[0]

    def get_port(self):
        return self.port

    def get_path(self):
        return self.path

    def get_filename(self):
        return self.path[self.path.rfind('/') + 1:]

    def get_ext(self):
        fname = self.get_filename()
        ext = fname[fname.rfind('.') + 1:]
        if ext == fname:
            return ''
        else:
            return ext

    def get_query(self):
        return self.qs


    def get_fragment(self):
        return self.fragment

    @property
    def url_string(self):
        u_url = self._unicode_url
        if not self._change or u_url is None:
            data = (self.scheme, self.netloc, self.path, self.params, self.qs, self.fragment)
            dataurl = parse.urlunparse(data)
            try:
                u_url = str(dataurl)
            except UnicodeDecodeError:
                u_url = str(dataurl, self._encoding, 'replace')
            self._unicode_url = u_url
            self._change = True

        return  u_url   #fix me  this line

    def __str__(self):
        return "%s" % (self.url_string.encode(self._encoding))

    def __repr__(self):
        return '<URL FOR "%s">' % self.url_string.encode(self._encoding)


if __name__ == '__main__':

    urlStr = "http://www.anquanbao.com/book/index.php?id=1#top"

    url = URL(urlStr)

    print(url.get_host())

    print(url.get_port())

    print(url.get_path())

    print(url.get_filename())

    print(url.get_ext())

    print(url.get_query())

    print(url.fragment)

    print(url.url_string)