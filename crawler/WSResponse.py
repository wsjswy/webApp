from  crawler.WSRequest import WSRequest
from  crawler.URL import  URL


import  uuid
import  copy
import  re


DEFAULT_ENCODING = "utf-8"
DEFAULT_CHARSET = DEFAULT_ENCODING

def from_requests_response(res, req_url):

    print("fix me ")



class WSResponse:

    def __init__(self, status_code = None, headers = None, body = None,
                 req_url = None, msg = 'OK', id = None, time = 0.2, charset = None):

        self._code = status_code
        self._headers = headers
        self._req_url = req_url
        self._body = None
        self._raw_body = body
        self._msg = msg
        self._time = time
        self._charset = charset

        #response 对象的唯一标识属性
        self.id = id if id else  uuid.uuid1()

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return  self.id

    def set_code(self, code):
        self._code = code

    def get_code(self):
        return self._code

    def set_url(self, url):
        self._req_url = url

    def get_url(self):
        return  self._req_url

    def set_body(self, body):
        self._body = body

    def get_body(self):
        return  self._body

    def get_cookies(self):

        if "set-cookie" in self._headers.keys():
            return self._headers["set-cookie"]

        else:
            return  None
    def get_headers(self):
        return  self._headers

    @property
    def headers(self):
        return self._headers

    @property
    def body(self):
        if self._code is None:
            return self._body
        if self._body is None:
            self._body, self._charset = self._charset_handing()

        return self._body

    @property
    def charset(self):

        if self._code is None:
            return self._charset

        if self._charset is None:
            self.body, self._charset = self._charset_handing()

        return self._charset

    def set_charset(self, charset):
        self._charset = charset

    def get_charset(self):
        return  self._charset

    def get_lowercase_headers(self):
        return dict((k.lower(), v) for k, v in self._headers.iteritems())

    def _charset_handing(self):
        lowercase_headers = self.get_lowercase_headers()
        #Request 默认的编码
        charset = self._charset
        #原始的body数据， 需要进行编码处理
        rawbody = self._raw_body

        if charset != DEFAULT_CHARSET and lowercase_headers.has_key('content-type'):
            charset_mo = re.search('charset = \s*?([\w-]+)', lowercase_headers['content-type'])
            if charset_mo:
                charset = charset_mo.group()[0].lower().strip()
            else:
                try:
                    raise Exception
                except:
                    charset = DEFAULT_CHARSET

            try:
                _body = str(rawbody, charset)

            except:
                charset = 'gbk'
                try:
                    _body = str(rawbody, charset)
                except:
                    _body = rawbody
                    charset = 'UNKNOWN'
        else:
            _body = str(rawbody, "utf-8", errors='ignore')


        return  _body, charset


    def __str__(self):

        result_string = 'HTTP/1.1 ' + str(self._code) + ' ' + self._msg + '\r\n'

        if self.headers:
            result_string += '\r\n'.join(h + ':' + hv for h, hv in self.headers.items()) + '\r\n'

        if self.body:
            result_string += '\r\n' + self.body.encode("utf-8")

        return result_string


    def __repr__(self):
        vals = {'code': self.get_code(), 'url': str(self.get_url()), 'id': self.id}

        return '<Reponse | %(code)s | %(url)s | %(id)s>' % vals

