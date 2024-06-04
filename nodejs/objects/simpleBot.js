const token = "";

const { BaleVK } = require("../main");
const app = new BaleVK(token);

let msg_lis = [];

app.on({
    updatetime: 1000,
    callback: (msg) => {
        let text = String(msg.text);
        let chat = msg.chatID;
        let msg_id = msg.messageID;

        if (!msg_lis.includes(msg_id)){
            msg_lis.push(msg.chatID);

            if (text === "/start"){
                app.sendMessage({text: "Hello Sir this is a Bot from BaleVK Nodejs !", chatID: chat, messageID:msg_id});
            }else if (text.startsWith("say")){
                app.sendMessage({text: text.replace("say ", ""), chatID: chat, messageID: msg_id});
            }

        }else{
            msg_lis.push(msg.chatID);
        }
    }
})
