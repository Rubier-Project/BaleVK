#!/usr/bin/python3
# MIT License
"""
Copyright 2024 Rubier-Project | Host1let | Zrexer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import warnings
import sys
from typing import List

from network import NetworkHandler
from req import requirements_checker
from updater import (
    Updater,
    TextUpdater,
    PictureUpdater,
    VideoUpdater,
    VoiceAudioUpdater,
    LocationUpdater
)

from console import (
    Console
)

from fileio import (
    FileIO
)

warnings.filterwarnings('ignore')
requirements_checker()

class BaleVK(object):
    def __init__(self,
                 TokenBot: str, Proxies: dict = None,
                 Headers: dict = None):
        self.token = TokenBot
        self.prx = Proxies
        self.head = Headers
        self.network = NetworkHandler(self.token, self.head, self.prx)
        self.on_types = [
            "message",
            "text",
            "pic",
            "video",
            "voice",
            "audio",
            "location"
        ]

    def on(self,
           typing: str = "message"):
        
        if not typing in self.on_types:
            exit("Type of 'on' function is not available")

        if typing == "message":
            yield Updater(self.token, self.network.create("getUpdates"))

        elif typing == "text":
            yield TextUpdater(self.token, self.network.create("getUpdates"))

        elif typing == "pic":
            yield PictureUpdater(self.token, self.network.create("getUpdates"))

        elif typing == "video":
            yield VideoUpdater(self.token, self.network.create("getUpdates"))

        elif typing == "voice" or typing == "audio":
            yield VoiceAudioUpdater(self.token, self.network.create("getUpdates"))

        elif typing == "location":
            yield LocationUpdater(self.token, self.network.create("getUpdates"))

    @property
    def on_types_list(self):
        return self.on_types
    
    def setWebhook(self, url: str = None):
        assert url is not None, exit("Url Cannot be Empty")

        return self.network.create(f"setWebhook?url={url}")

    def getWebhookInfo(self, token = None):
        if token == None:
            return self.network.create("getWebhookInfo")
        else:
            return NetworkHandler(token, self.head, self.prx).create("getWebhookInfo")
        
    def getWebhookInfoByURL(self, url: str = None):
        assert url is not None, exit("Url Cannot be Empty")

        return self.network.create(f"WebhookInfo?url={url}")
    
    def sendPhoto(self, chatID: str, messageID: str = None, caption: str = None, fileOrPath: str | bytes = None):
        assert ( fileOrPath is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        fio = FileIO(fileOrPath)

        if not fio.existsStat():
            param = {
                'chat_id': chatID,
                "reply_to_message_id": messageID,
                "caption": caption,
                "photo": fileOrPath
            }
            return self.network.create(f"sendPhoto", param)
        
        else:
            if not fio.isFile():
                if "--ignore" in sys.argv:
                    apps = fio.listDir()
                    dbs = dict()

                    for app in apps:
                        if str(app).endswith("jpg") or str(app).endswith("png") or str(app).endswith("webp"):
                            try:
                                result = self.network.upload("photo", app, chatID, caption=caption, message_id=messageID)
                                dbs[app] = result
                            except Exception as ER:
                                dbs[app] = str(ER)

                    return dbs
                
                else:
                    raise ValueError("The Path is not File -- if you want to upload files of a folder next by next please use '--ignore' flag")
            else:
                try:
                    return self.network.upload("photo", fileOrPath, chatID, caption=caption, message_id=messageID)
                except Exception as ER:
                    return str(ER)
                
    def sendGroupPhoto(self, chatID: str, messageID: str = None, caption: str = None, filesOrPaths: List[str] = None):
        assert ( filesOrPaths is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        dbs = dict()
        for app in filesOrPaths:
            fio = FileIO(app)

            if not fio.existsStat():
                param = {
                    'chat_id': chatID,
                    "reply_to_message_id": messageID,
                    "caption": caption,
                    "photo": app
                }
                dbs[app] = self.network.create(f"sendPhoto", param)
            
            else:
                if str(app).endswith("jpg") or str(app).endswith("png") or str(app).endswith("webp"):
                    try:
                        result = self.network.upload("photo", app, chatID, caption=caption, message_id=messageID)
                        dbs[app] = result
                    except Exception as ER:
                        dbs[app] = str(ER)

        return dbs
    
    def sendVideo(self, chatID: str, messageID: str = None, caption: str = None, fileOrPath: str | bytes = None):
        assert ( fileOrPath is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        fio = FileIO(fileOrPath)

        if not fio.existsStat():
            param = {
                'chat_id': chatID,
                "reply_to_message_id": messageID,
                "caption": caption,
                "video": fileOrPath
            }
            return self.network.create(f"sendVideo", param)
        
        else:
            if not fio.isFile():
                if "--ignore" in sys.argv:
                    apps = fio.listDir()
                    dbs = dict()

                    for app in apps:
                        if str(app).endswith("mp4") or str(app).endswith("mov") or str(app).endswith("mkv") or str(app).endswith("wmv") or str(app).endswith("mpg") or str(app).endswith("ogg"):
                            try:
                                result = self.network.upload("video", app, chatID, caption=caption, message_id=messageID)
                                dbs[app] = result
                            except Exception as ER:
                                dbs[app] = str(ER)

                    return dbs
                
                else:
                    raise ValueError("The Path is not File -- if you want to upload files of a folder next by next please use '--ignore' flag")
            else:
                try:
                    return self.network.upload("video", fileOrPath, chatID, caption=caption, message_id=messageID)
                except Exception as ER:
                    return str(ER)
                
    def sendGroupVideo(self, chatID: str, messageID: str = None, caption: str = None, filesOrPaths: List[str] = None):
        assert ( filesOrPaths is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        dbs = dict()
        for app in filesOrPaths:
            fio = FileIO(app)

            if not fio.existsStat():
                param = {
                    'chat_id': chatID,
                    "reply_to_message_id": messageID,
                    "caption": caption,
                    "video": app
                }
                dbs[app] = self.network.create(f"sendVideo", param)
            
            else:
                if str(app).endswith("jpg") or str(app).endswith("png") or str(app).endswith("webp"):
                    try:
                        result = self.network.upload("video", app, chatID, caption=caption, message_id=messageID)
                        dbs[app] = result
                    except Exception as ER:
                        dbs[app] = str(ER)

        return dbs
    
    def sendAudio(self, chatID: str, messageID: str = None, caption: str = None, fileOrPath: str | bytes = None):
        assert ( fileOrPath is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        fio = FileIO(fileOrPath)

        if not fio.existsStat():
            param = {
                'chat_id': chatID,
                "reply_to_message_id": messageID,
                "caption": caption,
                "audio": fileOrPath
            }
            return self.network.create(f"sendAudio", param)
        
        else:
            if not fio.isFile():
                if "--ignore" in sys.argv:
                    apps = fio.listDir()
                    dbs = dict()

                    for app in apps:
                        if str(app).endswith("mp3") or str(app).endswith("wav") or str(app).endswith("wma"):
                            try:
                                result = self.network.upload("audio", app, chatID, caption=caption, message_id=messageID)
                                dbs[app] = result
                            except Exception as ER:
                                dbs[app] = str(ER)

                    return dbs
                
                else:
                    raise ValueError("The Path is not File -- if you want to upload files of a folder next by next please use '--ignore' flag")
            else:
                try:
                    return self.network.upload("audio", fileOrPath, chatID, caption=caption, message_id=messageID)
                except Exception as ER:
                    return str(ER)
                
    def sendGroupAudio(self, chatID: str, messageID: str = None, caption: str = None, filesOrPaths: List[str] = None):
        assert ( filesOrPaths is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        dbs = dict()
        for app in filesOrPaths:
            fio = FileIO(app)

            if not fio.existsStat():
                param = {
                    'chat_id': chatID,
                    "reply_to_message_id": messageID,
                    "caption": caption,
                    "audio": app
                }
                dbs[app] = self.network.create(f"sendAudio", param)
            
            else:
                if str(app).endswith("mp3") or str(app).endswith("wav") or str(app).endswith("wma"):
                    try:
                        result = self.network.upload("audio", app, chatID, caption=caption, message_id=messageID)
                        dbs[app] = result
                    except Exception as ER:
                        dbs[app] = str(ER)

        return dbs
    
    def sendDocument(self, chatID: str, messageID: str = None, caption: str = None, fileOrPath: str | bytes = None):
        assert ( fileOrPath is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        fio = FileIO(fileOrPath)

        if not fio.existsStat():
            param = {
                'chat_id': chatID,
                "reply_to_message_id": messageID,
                "caption": caption,
                "document": fileOrPath
            }
            return self.network.create(f"sendDocument", param)
        
        else:
            if not fio.isFile():
                if "--ignore" in sys.argv:
                    apps = fio.listDir()
                    dbs = dict()

                    for app in apps:
                        try:
                            result = self.network.upload("document", app, chatID, caption=caption, message_id=messageID)
                            dbs[app] = result
                        except Exception as ER:
                            dbs[app] = str(ER)

                    return dbs
                
                else:
                    raise ValueError("The Path is not File -- if you want to upload files of a folder next by next please use '--ignore' flag")
            else:
                try:
                    return self.network.upload("document", fileOrPath, chatID, caption=caption, message_id=messageID)
                except Exception as ER:
                    return str(ER)
                
    def sendGroupDocument(self, chatID: str, messageID: str = None, caption: str = None, filesOrPaths: List[str] = None):
        assert ( filesOrPaths is not None ) or ( chatID is not None ),  exit("File Path and Chat ID Cannot be Empty")
        dbs = dict()
        for app in filesOrPaths:
            fio = FileIO(app)

            if not fio.existsStat():
                param = {
                    'chat_id': chatID,
                    "reply_to_message_id": messageID,
                    "caption": caption,
                    "document": app
                }
                dbs[app] = self.network.create(f"sendDocument", param)
            
            else:
                try:
                    result = self.network.upload("document", app, chatID, caption=caption, message_id=messageID)
                    dbs[app] = result
                except Exception as ER:
                    dbs[app] = str(ER)

        return dbs
    
    def sendLocation(self, chatID: str, longitude: str, latitude: str, messageID: str = None):
        assert ( chatID is not None ) or ( ( longitude and latitude ) is not None ), exit("Chat ID or Longitude or Latitude cannot be Empty")

        params = {
            "chat_id": chatID,
            "longitude": longitude,
            "latitude": latitude,
            "reply_to_message_id": messageID
        }
        return self.network("sendLocation", params)
    
    def sendContact(self, chatID: str, phoneNumber: str | int, firstName: str, lastName: str = None, messageID: str = None):
        assert ( ( chatID and phoneNumber and firstName) is not None ), exit("Chat ID or Phone Number or Firstname cannot be empty")

        params = {
            "chat_id": chatID,
            "phone_number": phoneNumber,
            "first_name": firstName,
            "last_name": lastName,
            "reply_to_message_id": messageID
        }

        return self.network.create("sendContact", params)
    
    def sendMessage(self, chatID: str, message: str = None, messageID: str = None):
        assert ( ( chatID and message) is not None ), exit("Chat ID or Message cannot be empty")

        params = {
            "chat_id": chatID,
            "text": message,
            "reply_to_message_id": messageID
        }

        return self.network.create("sendMessage", params)
    
    def forwardMessage(self, fromChatID: str, toChatID: str, messageID: str):
        assert ( ( fromChatID and toChatID and messageID ) is not None ), exit("Chat ID or From Chat ID or To Chat ID cannot be empty")

        params = {
            "chat_id": toChatID,
            "from_chat_id": fromChatID,
            "message_id": messageID
        }

        return self.network.create("forwardMessage", params)
    
    def getFile(self, fileID: str = None):
        assert ( fileID is not None ),  exit("File ID Cannot be Empty")

        return self.network.create("getFile", {
            "file_id": fileID
        })
    
    def banMember(self, chatID: str, userID: str):
        assert ( userID is not None ) or ( chatID is not None ),  exit("User ID and Chat ID Cannot be Empty")

        return self.network.create("banChatMember", {
            "chat_id": chatID,
            "user_id": userID
        })
    
    def unbanMember(self, chatID: str, userID: str, only_if_banned: bool = None):
        assert ( userID is not None ) or ( chatID is not None ),  exit("User ID and Chat ID Cannot be Empty")

        return self.network.create("unbanChatMember", {
            "chat_id": chatID,
            "user_id": userID,
            "only_if_banned": only_if_banned
        })
    
    def promoteMember(self, chatID: str, userID: str):
        assert ( userID is not None ) or ( chatID is not None ),  exit("User ID and Chat ID Cannot be Empty")

        return self.network.create("promoteChatMember", {
            "chat_id": chatID,
            "user_id": userID
        })
    
    def editMessageText(self, chatID: str, newText: str, oldMessageID: str):
        assert ( ( newText and chatID and oldMessageID ) is not None ), exit("Chat ID or New Text or Old Message ID cannot be empty")

        return self.network.create("editMessageText", {
            "chat_id": chatID,
            "text": newText,
            "message_id": oldMessageID
        })
    
    def deleteMessage(self, chatID: str, messageID: str):
        assert ( messageID is not None ) or ( chatID is not None ),  exit("Message ID and Chat ID Cannot be Empty")

        return self.network.create("deleteMessage", {
            "chat_id": chatID,
            "message_id": messageID
        })
    
    def setChatPhoto(self, chatID: str, photo: str):
        assert ( photo is not None ) or ( chatID is not None ),  exit("photo and Chat ID Cannot be Empty")

        return self.network.create("setChatPhoto", {
            "chat_id": chatID,
            "photo": photo
        })
    
    def leaveChat(self, chatID: str):
        assert ( chatID is not None ),  exit("Chat ID Cannot be Empty")

        return self.network.create("leaveChat", {
            "chat_id": chatID
        })
    
    def getChat(self, chatID: str):
        assert ( chatID is not None ),  exit("Chat ID Cannot be Empty")

        return self.network.create("getChat", {
            "chat_id": chatID
        })
    
    def getChatMemberCount(self, chatID: str):
        assert ( chatID is not None ),  exit("Chat ID Cannot be Empty")

        return self.network.create("getChatMemberCount", {
            "chat_id": chatID
        })
    
    def getMe(self):
        return self.network.create("getMe")
    
    def close(self):
        return self.network.create("close")
    
    def logout(self):
        return self.network.create("logout")