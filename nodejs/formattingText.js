class Formatter{
    constructor(textMessage){
        this.text = String(textMessage);
    }

    bold(){
        return `*${this.text}*`;
    }

    italic(){
        return `_${this.text}_`;
    }

    add_link(link){
        return `[${this.text}](${link})`;
    }

    add_details(details){
        return "```["+this.text+"]"+details+"```";
    }
}

module.exports = {
    Formatter
}