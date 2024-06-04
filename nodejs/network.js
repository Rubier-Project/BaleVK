const axiosClass = require("axios");
const FormData = require('form-data');
const fs = require('fs');

console.log("connecting to api server ...");

class NetworkHandler{
    constructor(
        auth_token,
        proxy,
        header){
        this.auth = auth_token;
        this.proxy = proxy;
        this.head = header;
        this.axGet = new axiosClass.Axios("GET");
        this.axPost = new axiosClass.Axios("POST");
    }

    makeMethod(method){
        return `https://tapi.bale.ai/bot${this.auth}/${method}`;
    }

    createGet(method, params, callback = null){
        try{
            this.axGet.get(this.makeMethod(method), {
                proxy: this.proxy,
                headers: this.head,
                params:params
            }).then((resp) => {
                if (callback === null){
                    true;
                }else{
                    let data = JSON.parse(resp.data);
                    data.error = false;
                    data.base = null;
                    callback(data)
                }
            })
        }catch (er){
            if (callback === null){
                true;
            }else{
                let data = JSON.parse(JSON.stringify(
                    {
                        "error": true,
                        "base": er
                    }
                ));
                callback(data)
            }
        }
    }

    createPost(method, params, callback = null){
        try{
            this.axPost.post(this.makeMethod(method), {
                proxy: this.proxy,
                headers: this.head,
                params:params
            }).then((resp) => {
                if (callback === null){
                    true;
                }else{
                    let data = JSON.parse(resp.data);
                    data.error = false;
                    data.base = null;
                    callback(data)
                }
            })
        }catch (er){
            if (callback === null){
                true;
            }else{
                let data = JSON.parse(JSON.stringify(
                    {
                        "error": true,
                        "base": er
                    }
                ));
                callback(data)
            }
        }
    }

    upload({TypeFile, path, chatID, caption = null, messageID = null, callback = null}={}){
        const formData = new FormData();
		const file = fs.createReadStream(path);
		formData.append(TypeFile, file);
		formData.append("chat_id", chatID);
		formData.append("caption", caption ? caption !== null : "");
		formData.append("reply_to_message_id", messageID ? messageID !== null : "")
		this.axPost.post(this.makeMethod(`send${TypeFile}`), formData, {
		headers: {
			'Content-Type': 'multipart/form-data',
		},
		})
		.then((response) => {
            if (callback === null){
                true;
            }else{
                let data = JSON.parse(response.data);
                data.error = false;
                data.base = null;
                callback(data);
            }
		})
		.catch((error) => {
			if (callback === null){
                true;
            }else{
                let data = JSON.parse(JSON.stringify({}));
                data.error = true;
                data.base = error;
                callback(data);
            }
		});
    }
}

module.exports = {
    NetworkHandler
}