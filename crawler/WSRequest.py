from  crawler.URL import  URL
import copy

class WSRequest:
    def __init__(self, url, method='GET',headers=None,cookies=None,refer=None, data=None, user_agent=None, **kwargs):
        if isinstance(url, URL):
            self._url = url
        else:
            self._url = URL(url)

        self._method = method.upper()
        self._headers = {}
        self._cookies = cookies
        self._refer = refer
        self._user_agent = user_agent
        if self._cookies:
            headers.update({"Cookie": self._cookies})
        if self._refer:
            self._headers.update({"Referer": self._refer})
        if self._user_agent:
            self._headers.update({"User-Agent": self._user_agent})
        self._get_date = self._url.get_querystring()

        if data:
            self._post_data = data

    def get_get_param(self):
        " ' "
        " ' "

        return self._get_date

    def get_post_parm(self):

        return self._post_data

    def get_url(self):

        return self._url

    def get_method(self):

        return self._method

    def  get_headers(self):

        return self._headers

    def get_cookies(self):

        return self._cookies

    def set_post_data(self, postdata):

        self._post_data = postdata

    def set_get_data(self, getdata):

        self._get_date = getdata

    def set_refer(self, refer):

        self._refer = refer

    def set_cookies(self, cookies):

        self._cookies = cookies

    def __str__(self):

        result_string = self._method

        result_string += " " + self._url.url_string + " HTTP/1.1\r\n"

        headers = copy.deepcopy(self._headers)  #fix me this line

        headers.update({"Host":self._url.get_host()})

        for key, value in headers.items():
            result_string += key + ": " + value
            result_string += "\r\n"
        result_string += "\r\n"

        if self._method == "POST":
            result_string += str(self._post_data)

        result_string = result_string.encode("utf-8")

        return result_string

    def __repr__(self):

        vals = {'method':self.get_method(), 'url':str(self.get_url()),'id':self.get_id()}

        return '<Request | %(method)s | %(url)s + %(id)s>' % vals



