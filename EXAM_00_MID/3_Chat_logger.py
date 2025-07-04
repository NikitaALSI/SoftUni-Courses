def chat(text: str, log: list):
    log.append(text)
    return log


def delete(text: str, log: list):
    if text in log:
        log.remove(text)
    return log


def edit(text: str, text2: str, log: list):
    if text in log:
        log[log.index(text)] = text2
    return log


def pin(text: str, log: list):
    if text in log:
        log.append(log.pop(log.index(text)))
    return log


def spam(texts: list, log: list):
    log.extend(texts)
    return log


messages = []
while True:
    cmd = input()
    if cmd == "end":
        print("\n".join(messages))
        break
    elif cmd.startswith("Chat"):
        message = cmd.split()[-1]
        message = chat(message, messages)
    elif cmd.startswith("Delete"):
        message = cmd.split()[-1]
        message = delete(message, messages)
    elif cmd.startswith("Edit"):
        message, edited_message = cmd.split()[1:]
        message = edit(message, edited_message, messages)
    elif cmd.startswith("Pin"):
        message = cmd.split()[-1]
        message = pin(message, messages)
    elif cmd.startswith("Spam"):
        spam_message = cmd.split()[1:][:]
        message = spam(spam_message, messages)