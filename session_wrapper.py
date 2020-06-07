import requests

class SesstionWrapper(object):
    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update({"X-Requested-With": "XMLHttpRequest"})

    def get(self, url, params=None):
        if params is None:
            params = {}
        res = self._session.get(url, params=params)
        return res.content.decode("utf8")

    def post(self, url,  data=None, json=None, params=None):
        if params is None:
            params = {}
        res = self._session.post(url, params=params, json=json, data=data)
        return res.content.decode("utf8")

    def update_header(self, key, value):
        self._session.headers.update({key: value})

    def update_cookie(self, name, value, domain, path="/"):
        my_cookie = {
            "version": 0,
            "name": name,
            "value": value,
            "port": None,
            # "port_specified":False,
            "domain": domain,
            # "domain_specified":False,
            # "domain_initial_dot":False,
            "path": path,
            # "path_specified":True,
            "secure": False,
            "expires": None,
            "discard": True,
            "comment": None,
            "comment_url": None,
            "rest": {},
            "rfc2109": False
        }
        self._session.cookies.set(**my_cookie)
        pass