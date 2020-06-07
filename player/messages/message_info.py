

class SpyReport():
    def __init__(self, msg_id):
        self._msg_id = msg_id
        self._msg_detail = None

    def _get_detail(self):

        return True

    def set_detail(self, detail):
        self._msg_detail = detail

    @property
    def msg_id(self):
        return self._msg_id

    @property
    def msg_detail(self):
        if self._msg_detail is None:
            self._msg_detail = self._get_detail()
        return