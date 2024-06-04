from ..main import BaleVK
from formattingText import formatObject
from forefront import ForefrontClient
from forefront.utils import SystemChat, UserChat

token = ""
apiKey = ""
ff = ForefrontClient(api_key=apiKey)

def gpt(user: str):
    completion = ff.chat.completions.create(
        messages=[
            SystemChat("You are a helpful assistant"),
            UserChat(user),
        ],
        model="mistralai/Mistral-7B-v0.1",
        temperature=0.5,
        max_tokens=128,
    )
    return str(completion.message['content'])

app = BaleVK(token)
msg_lis = set()

print("Start")

while 1:
    for msg in app.on(
        "message"
    ):
        text = msg.text
        chat = msg.chat_id
        msg_id = msg.message_id

        if not msg_id in msg_lis:
            msg_lis.add(msg_id)
            print("Text Recived:", text, f":{chat}")

            if text == "/start":
                app.sendMessage(chat, "type /help to see options", msg_id)

            if text == "/help":
                app.sendMessage(chat, "Write your order or question in front of command /gpt\n  /gpt Hello can you help Me?", msg_id)

            if text.startswith("/gpt"):
                txt = text.replace("/gpt ", "")

                if txt == "/gpt" or txt == " ":
                    app.sendMessage(chat, "Faild to Use, to see usage type {}".format(formatObject('/help').add_info('Write your order or question in front of command /gpt\n  /gpt Hello can you help Me?')), msg_id)
                else:
                    uinion = app.sendMessage(chat, "Wait a Second ...", msg_id)
                    info = gpt(txt)
                    app.editMessageText(chat, info, uinion['result']['message_id'])
        else:
            msg_lis.add(msg_id)
