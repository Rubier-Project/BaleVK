import httpx

class Updater(object):
    def __init__(self, token, result: dict):
        self.token = token
        self.results = result

    @property
    def result(self):
        return self.results['result']
    
    @property
    def last_result(self):
        try:
            return self.result[-1]
        except:
            return "Not Exists"
    
    @property
    def update_id(self):
        try:
            return self.last_result['update_id']
        except:
            return "Not Exists"
    
    @property
    def message(self):
        try:
            return self.last_result['message']
        except:
            return "Not Exists"
    
    @property
    def message_id(self):
        try:
            return self.message['message_id']
        except:
            return "Not Exists"
    
    @property
    def from_chat(self):
        try:
            return self.message['from']
        except:
            return "Not Exists"
    
    @property
    def from_id(self):
        try:
            return self.message['from']['id']
        except:
            return "Not Exists"
        
    @property
    def from_is_bot(self):
        try:
            return self.message['from']['is_bot']
        except:
            return "Not Exists"
        
    @property
    def from_first_name(self):
        try:
            return self.message['from']['first_name']
        except:
            return "Not Exists"
        
    @property
    def from_last_name(self):
        try:
            return self.message['from']['last_name']
        except:
            return "Not Exists"
        
    @property
    def date(self):
        try:
            return self.message['date']
        except:
            return "Not Exists"
        
    @property
    def chat(self):
        try:
            return self.message['chat']
        except:
            return "Not Exists"
        
    @property
    def chat_id(self):
        try:
            return self.message['chat']['id']
        except:
            return "Not Exists"
        
    @property
    def chat_type(self):
        try:
            return self.message['chat']['type']
        except:
            return "Not Exists"
        
    @property
    def chat_first_name(self):
        try:
            if 'first_name' in self.message.keys():
                return self.message['chat']['first_name']
            else:
                return ""
        except:
            return "Not Exists"
        
    @property 
    def chat_last_name(self):
        try:
            if 'last_name' in self.message.keys():
                return self.message['chat']['last_name']
            else:
                return ""
        except:
            return "Not Exists"
        
    @property
    def chat_photo(self):
        try:
            return self.message['chat']['photo']
        except:
            return "Not Exists"
        
    @property
    def chat_photo_small_file_id(self):
        try:
            return self.message['chat']['photo']['small_file_id']
        except:
            return "Not Exists"
        
    @property
    def chat_photo_small_file_unique_id(self):
        try:
            return self.message['chat']['photo']['small_file_unique_id']
        except:
            return "Not Exists"
        
    @property
    def chat_photo_big_file_id(self):
        try:
            return self.message['chat']['photo']['big_file_id']
        except:
            return "Not Exists"
        
    @property
    def chat_photo_big_file_unique_id(self):
        try:
            return self.message['chat']['photo']['big_file_unique_id']
        except:
            return "Not Exists"
        
    @property
    def text(self):
        try:
            return self.message['text']
        except:
            return "Not Exists"
        
    @property
    def document(self):
        try:
            return self.message['document']
        except:
            return "Not Exists"
    
    @property
    def document_file_id(self):
        try:
            return self.message['document']['file_id']
        except:
            return "Not Exists"
        
    @property
    def document_mime_type(self):
        try:
            return self.message['document']['mime_type']
        except:
            return "Not Exists"
        
    @property
    def document_file_size(self):
        try:
            return self.message['document']['file_size']
        except:
            return "Not Exists"
        
    @property
    def document_unique_id(self):
        try:
            return self.message['document']['file_unique_id']
        except:
            return "Not Exists"
        
    @property
    def document_caption(self):
        try:
            return self.message['caption']
        except:
            return "Not Exists"
        
    @property
    def photo(self):
        try:
            return self.message['photo']
        except:
            return "Not Exists"
        
    @property
    def video(self):
        try:
            return self.message['video']
        except:
            return "Not Exists"
        
    @property
    def video_width(self):
        try:
            return self.message['video']['width']
        except:
            return "Not Exists"
        
    @property
    def video_height(self):
        try:
            return self.message['video']['height']
        except:
            return "Not Exists"
        
    @property
    def video_duration(self):
        try:
            return self.message['video']['duration']
        except:
            return "Not Exists"
        
    @property
    def audio(self):
        try:
            return self.message['audio']
        except:
            return "Not Exists"
        
    @property
    def voice(self):
        try:
            return self.message['voice']
        except:
            return "Not Exists"
        
    @property
    def voice_duration(self):
        try:
            return self.message['voice']['duration']
        except:
            return "Not Exists"
        
    @property
    def location(self):
        try:
            return self.message['location']
        except:
            return "Not Exists"
        
    @property
    def location_longitude(self):
        try:
            return self.message['location']['longitude']
        except:
            return "Not Exists"
        
    @property
    def location_latitude(self):
        try:
            return self.message['location']['latitude']
        except:
            return "Not Exists"
        
    def reply_to(self, text: str):
        return httpx.Client().get(f"https://tapi.bale.ai/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}&reply_to_message_id={self.message_id}").json()

class TextUpdater(object):
    def __init__(self, token, result: dict):
        self.token = token
        self.results = result

    @property
    def result(self):
        return self.results['result']
    
    @property
    def last_result(self):
        try:
            return self.result[-1]
        except:
            return "Not Exists"
        
    @property
    def message(self):
        try:
            return self.last_result['message']
        except:
            return "Not Exists"
        
    @property
    def chat_id(self):
        try:
            return self.message['chat']['id']
        except:
            return "Not Exists"
    
    @property
    def message_id(self):
        try:
            return self.message['message_id']
        except:
            return "Not Exists"
    
    @property
    def text(self):
        try:
            return self.message['text']
        except:
            return "Not Exists"
    
    def add_flag(self, flag: str):
        try:
            return self.text.replace(f"{flag} ", "")
        except:
            return "Not Exists"

    def add_stick_flag(self, flag: str):
        try:
            return self.text.replace(f"{flag}", "")
        except:
            return "Not Exists"
        
    def reply_to(self, text: str):
        return httpx.Client().get(f"https://tapi.bale.ai/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}&reply_to_message_id={self.message_id}").json()
    
class PictureUpdater(object):
    def __init__(self, token, result: dict):
        self.token = token
        self.results = result

    @property
    def result(self):
        return self.results['result']
    
    @property
    def last_result(self):
        try:
            return self.result[-1]
        except:
            return "Not Exists"
        
    @property
    def message(self):
        try:
            return self.last_result['message']
        except:
            return "Not Exists"
        
    @property
    def chat_id(self):
        try:
            return self.message['chat']['id']
        except:
            return "Not Exists"
    
    @property
    def message_id(self):
        try:
            return self.message['message_id']
        except:
            return "Not Exists"
    
    @property
    def document(self):
        try:
            return self.message['document']
        except:
            return "Not Exists"
    
    @property
    def document_file_id(self):
        try:
            return self.message['document']['file_id']
        except:
            return "Not Exists"
        
    @property
    def document_mime_type(self):
        try:
            return self.message['document']['mime_type']
        except:
            return "Not Exists"
        
    @property
    def document_file_size(self):
        try:
            return self.message['document']['file_size']
        except:
            return "Not Exists"
        
    @property
    def document_unique_id(self):
        try:
            return self.message['document']['file_unique_id']
        except:
            return "Not Exists"
        
    @property
    def document_caption(self):
        try:
            return self.message['caption']
        except:
            return "Not Exists"
        
    @property
    def photo(self):
        try:
            return self.message['photo']
        except:
            return "Not Exists"
        
    def reply_to(self, text: str):
        return httpx.Client().get(f"https://tapi.bale.ai/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}&reply_to_message_id={self.message_id}").json()
    
class VideoUpdater(object):
    def __init__(self, token, result: dict):
        self.token = token
        self.results = result

    @property
    def result(self):
        return self.results['result']
    
    @property
    def last_result(self):
        try:
            return self.result[-1]
        except:
            return "Not Exists"
        
    @property
    def message(self):
        try:
            return self.last_result['message']
        except:
            return "Not Exists"
        
    @property
    def chat_id(self):
        try:
            return self.message['chat']['id']
        except:
            return "Not Exists"
    
    @property
    def message_id(self):
        try:
            return self.message['message_id']
        except:
            return "Not Exists"
    
    @property
    def document(self):
        try:
            return self.message['document']
        except:
            return "Not Exists"
    
    @property
    def document_file_id(self):
        try:
            return self.message['document']['file_id']
        except:
            return "Not Exists"
        
    @property
    def document_mime_type(self):
        try:
            return self.message['document']['mime_type']
        except:
            return "Not Exists"
        
    @property
    def document_file_size(self):
        try:
            return self.message['document']['file_size']
        except:
            return "Not Exists"
        
    @property
    def document_unique_id(self):
        try:
            return self.message['document']['file_unique_id']
        except:
            return "Not Exists"
        
    @property
    def document_caption(self):
        try:
            return self.message['caption']
        except:
            return "Not Exists"
    
    @property
    def video(self):
        try:
            return self.message['video']
        except:
            return "Not Exists"
        
    @property
    def video_width(self):
        try:
            return self.message['video']['width']
        except:
            return "Not Exists"
        
    @property
    def video_height(self):
        try:
            return self.message['video']['height']
        except:
            return "Not Exists"
        
    @property
    def video_duration(self):
        try:
            return self.message['video']['duration']
        except:
            return "Not Exists"
        
    def reply_to(self, text: str):
        return httpx.Client().get(f"https://tapi.bale.ai/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}&reply_to_message_id={self.message_id}").json()
    
class VoiceAudioUpdater(object):
    def __init__(self, token, result: dict):
        self.token = token
        self.results = result

    @property
    def result(self):
        return self.results['result']
    
    @property
    def last_result(self):
        try:
            return self.result[-1]
        except:
            return "Not Exists"
        
    @property
    def message(self):
        try:
            return self.last_result['message']
        except:
            return "Not Exists"
        
    @property
    def chat_id(self):
        try:
            return self.message['chat']['id']
        except:
            return "Not Exists"
    
    @property
    def message_id(self):
        try:
            return self.message['message_id']
        except:
            return "Not Exists"
    
    @property
    def document(self):
        try:
            return self.message['document']
        except:
            return "Not Exists"
    
    @property
    def document_file_id(self):
        try:
            return self.message['document']['file_id']
        except:
            return "Not Exists"
        
    @property
    def document_mime_type(self):
        try:
            return self.message['document']['mime_type']
        except:
            return "Not Exists"
        
    @property
    def document_file_size(self):
        try:
            return self.message['document']['file_size']
        except:
            return "Not Exists"
        
    @property
    def document_unique_id(self):
        try:
            return self.message['document']['file_unique_id']
        except:
            return "Not Exists"
        
    @property
    def document_caption(self):
        try:
            return self.message['caption']
        except:
            return "Not Exists"

    @property
    def audio(self):
        try:
            return self.message['audio']
        except:
            return "Not Exists"
        
    @property
    def voice(self):
        try:
            return self.message['voice']
        except:
            return "Not Exists"
        
    @property
    def voice_duration(self):
        try:
            return self.message['voice']['duration']
        except:
            return "Not Exists"
    
    def reply_to(self, text: str):
        return httpx.Client().get(f"https://tapi.bale.ai/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}&reply_to_message_id={self.message_id}").json()
    
class LocationUpdater(object):
    def __init__(self, token, result: dict):
        self.token = token
        self.results = result

    @property
    def result(self):
        return self.results['result']
    
    @property
    def last_result(self):
        try:
            return self.result[-1]
        except:
            return "Not Exists"
        
    @property
    def message(self):
        try:
            return self.last_result['message']
        except:
            return "Not Exists"
        
    @property
    def chat_id(self):
        try:
            return self.message['chat']['id']
        except:
            return "Not Exists"
    
    @property
    def message_id(self):
        try:
            return self.message['message_id']
        except:
            return "Not Exists"
        
    @property
    def location(self):
        try:
            return self.message['location']
        except:
            return "Not Exists"
        
    @property
    def location_longitude(self):
        try:
            return self.message['location']['longitude']
        except:
            return "Not Exists"
        
    @property
    def location_latitude(self):
        try:
            return self.message['location']['latitude']
        except:
            return "Not Exists"
        
    def reply_to(self, text: str):
        return httpx.Client().get(f"https://tapi.bale.ai/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}&reply_to_message_id={self.message_id}").json()