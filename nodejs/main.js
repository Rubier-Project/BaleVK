const { NetworkHandler } = require("./network");
const { MessageUpdater } = require("./updater");
const { Formatter } = require("./formattingText");

class BaleVK{
    constructor(
        Bot_Token,
        Proxy,
        Headers
    ){
        this.token = Bot_Token;
        this.prx = Proxy ? Proxy : null || undefined;
        this.heads = Headers ? Headers : null || undefined;
        this.network = new NetworkHandler(this.token, this.prx, this.heads);
    }

    get messageUpdaterObjects(){
        return Object.getOwnPropertyNames(MessageUpdater.prototype);
    }

    on({
        updatetime = 5000,
        callback = null,
        offset = null,
        limit = null
    } = {}){
        const params = {
            "offset": offset,
            "limit": limit
        }

        setInterval(() => {
            this.network.createGet("getUpdates", params, (data) => {
                if (callback === null){true;}else{
                    callback(new MessageUpdater(this.token, data));
                }
            })
        }, updatetime);
        
    }

    onChat({
        chatID,
        updatetime = 5000,
        callback = null,
        offset = null,
        limit = null
    
    } = {}){
        this.on({
            updatetime: updatetime,
            limit: limit,
            offset: offset,
            callback: (recv) => {
                if (recv.chatID === chatID){
                    if (callback === null){
                        true;
                    }else{
                        callback(recv);
                    }
                }else{true;}
            }
        })
    }

    sendMessage({
        text = "",
        chatID = null,
        messageID = null,
        replyMarkup = null,
        callback = null
    } = {}){
        if (chatID === null){
            throw new Error("Chat id cannot be empty");
        }else{
            this.network.createGet("sendMessage", {
                "chat_id": chatID,
                "text": text,
                "reply_to_message_id": messageID,
                "reply_markup": replyMarkup
            }, (data) => {
                if (callback === null){true;}else{
                    callback(data);
                }
            })
        }
    }

    forwardMessage({
        toChatID = null,
        fromChatID = null,
        messageID = null,
        callback = null
    } = {}){
        if (toChatID === null ||
            fromChatID === null ||
            messageID === null){
                throw new Error("to chat id or from chat id or message id for forward cannot be null");
            }else{
                this.network.createGet("forwardMessage", {
                    "chat_id": toChatID,
                    "from_chat_id": fromChatID,
                    "message_id": messageID
                }, (data) => {
                    if (callback === null){true;}else{
                        callback(data);
                    }
                })
            }
    }

    forwardMessages({
        toChatID = null,
        fromChatID = null,
        messageIDs = [],
        callback = null
    } = {}) {
        global.forInfo = JSON.parse(JSON.stringify({}));
    
        if (toChatID === null || fromChatID === null || messageIDs.length === 0) {
            throw new Error("to chat id or from chat id or message id list for forward cannot be null");
        } else {
            const promises = messageIDs.map((messageID) => {
                return new Promise((resolve) => {
                    this.network.createGet("forwardMessage", {
                        "chat_id": toChatID,
                        "from_chat_id": fromChatID,
                        "message_id": messageID
                    }, (data) => {
                        global.forInfo[messageID] = data;
                        resolve(data);
                    });
                });
            });
    
            Promise.all(promises).then(() => {
                if (callback !== null) {
                    callback(global.forInfo);
                }else{true;}
            });
        }
    }

    sendPhoto({
        file = null,
        chatID = null,
        caption = "" || null,
        messageID = null,
        callback = null
    } = {}){
        if (file === null ||
            chatID === null){
                throw new Error("File or Chat id parameter in sendPhoto cannot be null");
            }else{
                this.network.upload({
                    TypeFile: "photo",
                    path: file,
                    chatID: chatID,
                    caption: caption,
                    messageID: messageID,
                    callback: (data) => {
                        if (callback === null){
                            true;
                        }else{
                            callback(data);
                        }
                    }
                })
            }
    }

    sendVideo({
        file = null,
        chatID = null,
        caption = "" || null,
        messageID = null,
        callback = null
    } = {}){
        if (file === null ||
            chatID === null){
                throw new Error("File or Chat id parameter in sendVideo cannot be null");
            }else{
                this.network.upload({
                    TypeFile: "video",
                    path: file,
                    chatID: chatID,
                    caption: caption,
                    messageID: messageID,
                    callback: (data) => {
                        if (callback === null){
                            true;
                        }else{
                            callback(data);
                        }
                    }
                })
            }
    }

    sendAudio({
        file = null,
        chatID = null,
        caption = "" || null,
        messageID = null,
        callback = null
    } = {}){
        if (file === null ||
            chatID === null){
                throw new Error("File or Chat id parameter in sendAudio cannot be null");
            }else{
                this.network.upload({
                    TypeFile: "audio",
                    path: file,
                    chatID: chatID,
                    caption: caption,
                    messageID: messageID,
                    callback: (data) => {
                        if (callback === null){
                            true;
                        }else{
                            callback(data);
                        }
                    }
                })
            }
    }

    sendVoice({
        file = null,
        chatID = null,
        caption = "" || null,
        messageID = null,
        callback = null
    } = {}){
        if (file === null ||
            chatID === null){
                throw new Error("File or Chat id parameter in sendVoice cannot be null");
            }else{
                this.network.upload({
                    TypeFile: "voice",
                    path: file,
                    chatID: chatID,
                    caption: caption,
                    messageID: messageID,
                    callback: (data) => {
                        if (callback === null){
                            true;
                        }else{
                            callback(data);
                        }
                    }
                })
            }
    }

    sendDocument({
        file = null,
        chatID = null,
        caption = "" || null,
        messageID = null,
        callback = null
    } = {}){
        if (file === null ||
            chatID === null){
                throw new Error("File or Chat id parameter in sendDocument cannot be null");
            }else{
                this.network.upload({
                    TypeFile: "document",
                    path: file,
                    chatID: chatID,
                    caption: caption,
                    messageID: messageID,
                    callback: (data) => {
                        if (callback === null){
                            true;
                        }else{
                            callback(data);
                        }
                    }
                })
            }
    }

    sendLocation({
        chatID = null,
        longitude = null,
        latitude = null,
        messageID = null,
        callback = null
    } = {}){
        if (chatID === null ||
            longitude === null ||
            latitude === null){
                throw new Error("Chat id or longitude or latitude parameters of sendLocation cannot be null");
            }else{
                this.network.createGet("sendLocation", {
                    "chat_id": chatID,
                    "latitude": latitude,
                    "longitude": longitude,
                    "reply_to_message_id": messageID
                }, (data) => {
                    if (callback === null){true;}else{
                        callback(data);
                    }
                })
            }
    }

    sendContact({
        chatID = null,
        firstName = null,
        phoneNumber = null,
        lastName = null,
        messageID = null,
        callback = null
    } = {}){
        if (chatID === null ||
            firstName === null ||
            phoneNumber === null){
                throw new Error("Chat id or first name or phone number parameters of sendContact cannot be null");
            }else{
                this.network.createGet("sendContact", {
                    "chat_id": chatID,
                    "first_name": firstName,
                    "last_name": lastName,
                    "phone_number": phoneNumber,
                    "reply_to_message_id": messageID
                }, (data) => {
                    if (callback === null){true;}else{
                        callback(data);
                    }
                })
            }
    }

    getFile({
        fileID = null,
        callback = null
    } = {}){
        if (fileID === null){
            throw new Error("File id parameter of getFile cannot be null");
        }else{
            this.network.createGet("getFile", {
                "file_id": fileID
            }, (data) => {
                if (callback === null){true;}else{
                    callback(data);
                }
            })
        }
    }

    banChatMember({
        chatID = null,
        userID = null,
        callback = null
    } = {}){
        if (chatID === null || userID === null){
            throw new Error("Chat id and user id of banChatMember Cannot be null");
        }else{
            this.network.createGet("banChatMember", {
                "user_id": userID,
                "chat_id": chatID
            }, (data) => {
                if (callback === null){true;}else{
                    callback(data);
                }
            })
        }
    }
    
    unbanChatMember({
        chatID = null,
        userID = null,
        callback = null
    } = {}){
        if (chatID === null || userID === null){
            throw new Error("Chat id and user id of unbanChatMember Cannot be null");
        }else{
            this.network.createGet("unbanChatMember", {
                "user_id": userID,
                "chat_id": chatID
            }, (data) => {
                if (callback === null){true;}else{
                    callback(data);
                }
            })
        }
    }

    promoteChatMember({
        chatID = null,
        userID = null,
        callback = null
    } = {}){
        if (chatID === null || userID === null){
            throw new Error("Chat id and user id of promoteChatMember Cannot be null");
        }else{
            this.network.createGet("promoteChatMember", {
                "user_id": userID,
                "chat_id": chatID
            }, (data) => {
                if (callback === null){true;}else{
                    callback(data);
                }
            })
        }
    }

    leaveChat({
        chatID = null,
        callback = null
    } = {}){
        if (chatID === null){
            throw new Error("Chat id of leaveChat Cannot be null");
        }else{
            this.network.createGet("leaveChat", {
                "chat_id": chatID
            }, (data) => {
                if (callback === null){true;}else{
                    callback(data);
                }
            })
        }
    }

    getMemberCount({
        chatID = null,
        callback = null
    } = {}){
        if (chatID === null){
            throw new Error("Chat id of getMemberCount Cannot be null");
        }else{
            this.network.createGet("getMemberCount", {
                "chat_id": chatID
            }, (data) => {
                if (callback === null){true;}else{
                    callback(data);
                }
            })
        }
    }

    editMessageText({
        chatID = null,
        messageID = null,
        newText = null,
        callback = null
    } = {}){
        if (chatID === null ||
            messageID === null ||
            newText === null){
                throw new Error("Chat id or message id or new text parameters of editMessageText Cannot be null");
            }else{
                this.network.createGet("editMessageText", {
                    "chat_id": chatID,
                    "message_id": messageID,
                    "text": newText
                }, (data) => {
                    if (callback === null){true;}else{
                        callback(data);
                    }
                })
            }
    }

    deleteMessage({
        chatID = null,
        messageID = null,
        callback = null
    } = {}){
        if (chatID === null ||
            messageID === null){
                throw new Error("Chat id or message id parameters of deleteMessage Cannot be null");
            }else{
                this.network.createGet("deleteMessage", {
                    "chat_id": chatID,
                    "message_id": messageID
                }, (data) => {
                    if (callback === null){true;}else{
                        callback(data);
                    }
                })
            }
    }

    sendInvoice({
        chatID = null,
        goodsTitle = null || "",
        description = null || "",
        payload = null,
        providerToken = null,
        prices = [] || null,
        photoUrl = null,
        messageID = null,
        replyMarkup = null,
        callback = null
    } = {}){
        if (chatID === null ||
            goodsTitle === null ||
            goodsTitle === "" ||
            description === null ||
            description === "" ||
            payload === null ||
            providerToken === null ||
            prices.length === 0 || 
            prices === null){
                throw new Error("Chat id or goods title or description or payload or provider token or prices parameter of sendInvoice cannot be null");
            }else{
                this.network.createGet("sendInvoice", {
                    "chat_id": chatID,
                    "title": goodsTitle,
                    "description": description,
                    "payload": payload,
                    "provider_token": providerToken,
                    "prices": prices,
                    "photo_url": photoUrl,
                    "reply_to_message_id": messageID,
                    "reply_markup": replyMarkup

                }, (data) => {
                    if (callback === null){true;}else{
                        callback(data);
                    }
                })
            }
    }

    getMe({
        callback = null
    } = {}){
        this.network.createGet("getMe", {}, (data) => {
            if (callback === null){true;}else{
                callback(data);
            }
        })
    }

    logout({
        callback = null
    } = {}){
        this.network.createGet("logout", {}, (data) => {
            if (callback === null){true;}else{
                callback(data);
            }
        })
    }

    close({
        callback = null
    } = {}){
        this.network.createGet("close", {}, (data) => {
            if (callback === null){true;}else{
                callback(data);
            }
        })
    }
}

module.exports = {
    BaleVK
}
