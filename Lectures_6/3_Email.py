class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while (cmd := input()) != "Stop":
    the_sender, the_receiver, the_content = cmd.split()
    email = Email(the_sender, the_receiver, the_content)
    emails.append(email)

sent_mails = [int(x) for x in input().split(", ")]
for index in sent_mails:
    emails[index].is_sent = True

print("\n".join(list(map(lambda x: x.get_info(), emails))))