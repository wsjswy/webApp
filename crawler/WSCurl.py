import  time
import  socket
import  httplib2
import  requests

from  crawler.URL import URL
from  crawler.WSRequest import WSRequest
from  crawler.WSResponse import  WSResponse, from_requests_response


timeout = 60
socket.setdefaulttimeout(60)

class wCurl:
     def __init__(self):
        #fix me
        self._scan_signature = ''
        self._scan_cookies = ''
        self._scan_proxies = ''


     def get_default_headers(self, headers):

         default_headers = {"User-Agent": self._scan_signature}
         default_headers.update(headers)

         return default_headers

     def get(self, url, headers = {}, **kwargs):

         default_headers= self.get_default_headers(headers)
         if not isinstance(url, URL):
             url = URL(url)
         requests_response = None
         try:
             requests_response = requests.get(url.url_string, headers = default_headers, **kwargs)
         except:
             return self._make_response(requests_response, url)
         response = self._make_response(requests_response, url)
         return response

     def post(self, url, headers = {}, data = None, **kwargs):
         default_headers = self.get_default_headers(headers)
         if not isinstance(url, URL):
             url = URL(url)
         requests_response = None
         try:
             requests_response = requests.post(url.url_string, headers=default_headers, **kwargs)
         except:
             return self._make_response(requests_response, url)
         response = self._make_response(requests_response, url)
         return response

     def _send_req(self, req):

         method = req.get_method()

         #不带查询参数和信息片段的URL

         uri = req.get_url().get_uri_string()
         getdata = req.get_get_param()
         postdata = req.get_post_param()
         headers = req.get_headers()
         cookies = self._scan_cookies
         proxies = self._scan_proxies
         send = getattr(requests, method, method.lower())
         requests_response = None
         try:
             requests_response = send(uri, parms = getdata, headers = headers, cookies = cookies, proxies = proxies)

         except:
             return self._make_response(requests_response, req.get_url())

         else:
             response = self._make_response(requests_response, req.get_url())
             return response

     def _make_response(self, resp_from_requests, req_url):

         if resp_from_requests is None:
             response = WSResponse(req_url=req_url)
         else:
             response = from_requests_response(resp_from_requests, req_url)

         return response


if __name__ == '__main__':
    print("curl test")

    curl = wCurl()

    urlStr = "http://www.baidu.com"

    res = curl.get(urlStr)

    print(res)