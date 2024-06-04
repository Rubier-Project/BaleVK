const { NetworkHandler } = require("./network");

class MessageUpdater{
    constructor(token, results){
        this.tok = token;
        this.res = results;
        this.network = new NetworkHandler(this.tok);
    }

    get result(){
        return this.res.result;
    }

    get lastResult(){
        return this.result[this.result.length - 1];
    }

    get updateID(){
        return this.lastResult.update_id;
    }

    get message(){
        return this.lastResult.message;
    }

    get messageID(){
        return this.message.message_id;
    }

    get fromChat(){
        return this.message.from;
    }

    get fromID(){
        return this.fromChat.id;
    }

    get fromIsBot(){
        return this.from.is_bot;
    }

    get fromFirstName(){
        return this.from.first_name;
    }

    get fromLastName(){
        return this.from.last_name;
    }

    get date(){
        return this.message.date;
    }

    get chat(){
        return this.message.chat;
    }

    get chatID(){
        return this.chat.id;
    }

    get chatType(){
        return this.chat.type;
    }

    get chatFirstName(){
        return this.chat.first_name;
    }

    get chatLastName(){
        return this.chat.last_name;
    }

    get chatPhoto(){
        return this.chat.photo;
    }

    get chatPhotoSmallFileID(){
        return this.chatPhoto.small_file_id;
    }

    get chatPhotoSmallUniqueID(){
        return this.chatPhoto.small_file_unique_id;
    }
    
    get chatPhotoBigFileID(){
        return this.chatPhoto.big_file_id;
    }

    get chatPhotoBigUniqueID(){
        return this.chatPhoto.big_file_unique_id;
    }

    get text(){
        return this.message.text;
    }

    get document(){
        return this.message.document;
    }

    get documentFileID(){
        return this.document.file_id;
    }

    get documentMimeType(){
        return this.document.mime_type;
    }

    get documentSize(){
        return this.document.file_size;
    }

    get documentUniqueID(){
        return this.document.unique_id;
    }

    get documentCaption(){
        return this.message.caption;
    }

    get photo(){
        return this.message.photo;
    }

    get video(){
        return this.message.video;
    }
    
    get videoWidth(){
        return this.video.width;
    }

    get videoHeight(){
        return this.video.height;
    }

    get videoDuration(){
        return this.video.duration;
    }

    get audio(){
        return this.message.audio;
    }

    get voice(){
        return this.message.voice;
    }

    get voiceDuration(){
        return this.voice.duration;
    }

    get location(){
        return this.message.location;
    }

    get locationLongitude(){
        return this.location.longitude;
    }

    get locationLatitude(){
        return this.location.latitude;
    }

    replyTo(text, callback = null){
        this.network.createGet("sendMessage", {
            "chat_id": this.chatID,
            "reply_to_message_id": this.messageID,
            "text": text
        }, (datas) => {
            if (callback === null){true;}else{
                callback(datas);
            }
        })
    }
}

module.exports = {
    MessageUpdater
}
