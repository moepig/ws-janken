from channels import Group

def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("sample").add(message.reply_channel)

def ws_disconnect(message):
    Group("sample").discard(message.reply_channel)
