#coding=utf-8

import  re

from  lxml import  etree
from crawler.URL import  URL
from crawler.WSResponse import WSResponse
from crawler.WSRequest import  WSRequest
from crawler.WSCurl import wCurl


DEFAULT_ENCODING = 'utf-8'

class HtmlParser:

    URL_HEADERS = ('location')
    URL_TAGS = ('a','img','link','script','iframe','frame','form','object')
    URL_ATTRS = ('href', 'src', 'data', 'action')
    URL_RE = re.compile('((http|https)://([\w:@\-\./]*?)[^ \n\r\t"\'<>]\s)') #fix me this line


    def __init__(self, response):

        self._encoding = DEFAULT_ENCODING
        self._base_url = response.get_url()
        self._inside_form = False


        self._emails = []
        self._form_reqs = []
        self._re_urls = set()
        self._tag_urls = set()

        self._pre_parse(response)
        self._parse(response)


    def start(self, tag, attrs):

        try:
            meth = getattr(self, '__handle__' + tag + '_tag_start', lambda *args: None)
            meth(tag, attrs)
            if tag.lower() in self.URL_TAGS:
                self._find_tag_urls(tag, attrs)


        except Exception, ex:
            pass


    def end(self, tag):
        getattr(self, '_handle_' + tag + '_tag_end', lambda arg: None)(tag)


    def _find_header_urls(self, headers):

        for key, value in headers.items():
            if key in self.URL_HEADERS:
                if value.startwith('http'):
                    url = URL(value, encoding=self._encoding)
                else:
                    url = self._base_url.urljoin(value).url_string
                    url = URL(url, encoding=self._encoding)
            self._tag_urls.add(url)

    #获取内容标签中的URL

    def _find_tag_urls(self, tag, attrs):

        for attr_name, attr_value in attrs.iteritems():

            if attr_name in self.URL_ATTRS and attr_value and not attr_value.startwith('#'):

                try:

                    if attr_value.startwith('http'):
                        url = URL(attr_value, encoding=self._encoding)
                    else:
                        url = self._base_url.urljoin(attr_value).url_string
                        url = URL(url, encoding=self._encoding)
                except ValueError:
                    pass

                else:
                    self._tag_urls.add(url)

    # 获取满足URL形式的数据： 如文本或者标签以外的URL
    def _find_regex_urls(self, doc_str):

        re_urls = set()

        for url in re.findall(HtmlParser.URL_RE, doc_str):

            try:
                url = URL(url[0], encoding = self._encoding)
            except ValueError:
                pass
            else:
                re_urls.add(url)

        def find_relative(doc_str):
            res = set()
            regex = '' #fix me this line

            relative_regex = re.compile(regex, re.U | re.I)

            for match_truple in relative_regex.findall(doc_str):

                match_str = match_truple[0]
                url = self._base_url.join_url(match_str).url_string
                url = URL(url, encoding=self._encoding)
                res.add(url)
            return res

        re_urls.update(find_relative(doc_str))
        self._re_urls.update(re_urls)


    def _pre_parse(self, response):

        str_headers = ""
        for key, val in response.headers.items():
            str_headers += key + ":" + val + "\r\n"

        self._regex_url_parse(str_headers)
        self._find_header_urls(str_headers) #fix me this line

        #利用正则获取响应体中的URL
        self._regex_url_parse(response.body)

    def _parse(self, response):

        parser = etree.HTMLParser(target=self, recover=True)
        try:
            etree.fromstring(response.body, parser)
        except ValueError:
            pass

    @property
    def forms(self):

        return  self._forms;


