const token = "";

const { BaleVK } = require("../main");
const app = new BaleVK(token);

let msg_list = [];

app.on({
    updatetime: 1000,
    callback: (msg) => {
        let text = String(msg.text);
        let chat = msg.chatID;
        let msg_id = msg.messageID;

        if (!msg_list.includes(msg_id)){
            msg_list.push(msg_id);

            if (text === "/start"){
                app.sendMessage({
                    text: "For More info type /help",
                    chatID: chat,
                    messageID: msg_id
                })
            }else if (text === "/help"){
                app.sendMessage({
                    text: "/get-info <TOKEN> : get information of a bot by token\n/set-hook <URL> <TOKEN> : set webhook for a bot by token",
                    chatID: chat,
                    messageID: msg_id
                })
            }else if (text.startsWith("/get-info")){
                let token = text.replace("/get-info ", "");

                if (token === "/get-info" || token == "" || token == " "){
                    app.sendMessage({
                        text: "Sorry bot cannot get the token",
                        chatID: chat,
                        messageID: msg_id
                    })
                }else{
                    app.getWebhookInfoByToken({
                        token: token,
                        callback: (webhookInfo) => {
                            app.sendMessage({
                                text: webhookInfo,
                                chatID: chat,
                                messageID: msg_id
                            })
                        }
                    })
                }
            }else if (text.startsWith("/set-hook")){
                let objects = text.replace("/set-hook ", "");
                if (objects === "/get-info" || objects == "" || objects == " "){
                    app.sendMessage({
                        text: "Sorry bot cannot get the objects",
                        chatID: chat,
                        messageID: msg_id
                    })
                }else{
                    if (!objects.split().length === 2){
                        app.sendMessage({
                            text: "Invalid objects, for more info type /help",
                            chatID: chat,
                            messageID: msg_id
                        })
                    }else{
                        app.setWebhookByToken({
                            url: objects.split()[0],
                            token: objects.split()[1],
                            callback: (setinfo) => {
                                app.sendMessage({
                                    text: setinfo,
                                    chatID: chat,
                                    messageID: msg_id
                                })
                            }
                        })
                    }
                }
            }

        }else{
            msg_list.push(msg_id);
        }
    }
})
