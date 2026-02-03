class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text


class Chat:
    def __init__(self):
        self.messages = []

    def send(self, msg):
        self.messages.append(msg)

    def history(self):
        for m in self.messages:
            print(f"{m.sender}: {m.text}")


chat = Chat()

while True:
    print("\n1.Xabar yuborish 2.Tarix 0.Exit")
    c = input(">>> ")

    if c == "1":
        chat.send(Message(input("Kim: "), input("Xabar: ")))
    elif c == "2":
        chat.history()
    elif c == "0":
        break
