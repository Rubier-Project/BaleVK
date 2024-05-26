import httpx
import requests
from fileio import FileIO

class NetworkHandler(object):
    print("connecting to api server ...")

    def __init__(self,
                 _auth_token: str,
                 _header: dict,
                 _proxy: dict,
                 _con_method: str = "GET"
                 ):
        self._auth = _auth_token
        self._header = _header
        self._proxy = _proxy
        self._con_method = _con_method.lower()
        self.api_url = "https://tapi.bale.ai/bot{}".format(self._auth)

    def makeMethod(self, method: str = "getMe"):
        return f"{self.api_url}/{method}"

    def create(self, method: str, params = None):
        app = httpx.Client(headers=self._header,
                           proxies=self._proxy,
                           params=params)
        
        if self._con_method == "get":
            data = app.get(self.makeMethod(method))
            if data.status_code == 200:
                if data.text.startswith("{") and data.text.endswith("}"):
                    return data.json()
                else:
                    return data.text
            else:
                if data.text.startswith("{") and data.text.endswith("}"):
                    return data.json()
                else:
                    return data.text

        elif self._con_method == "post":
            data = app.post(self.makeMethod(method))
            if data.status_code == 200:
                if data.text.startswith("{") and data.text.endswith("}"):
                    return data.json()
                else:
                    return data.text
            else:
                if data.text.startswith("{") and data.text.endswith("}"):
                    return data.json()
                else:
                    return data.text
                
    def upload(self, typeFile: str, filePath: str, chatid, caption, message_id):
        fio = FileIO(filePath)

        if not fio.existsStat():
            raise FileNotFoundError("Cannot Found file to send")
        
        if not fio.isFile():
            raise ValueError("Path is not File")
        
        params = {
            'chat_id': chatid,
            "caption": caption,
            "reply_to_message_id": message_id
        }

        file = {
            typeFile: fio.readStream()
        }

        try:
            return requests.get(self.makeMethod("sendPhoto"), params=params, files=file).json()
        except Exception as ER:
            return str(ER)