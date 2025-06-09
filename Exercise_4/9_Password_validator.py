def password_validator(password: str):
    error_messages = []

    if len(password) not in range(6, 10+1):
        error_messages.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        error_messages.append("Password must consist only of letters and digits")

    if len([char for char in password if char.isdigit()]) < 2:
        error_messages.append("Password must have at least 2 digits")

    if not error_messages:
        error_messages.append("Password is valid")

    message = ""
    for i in error_messages:
        if i == error_messages[-1]:
            message += i
        else:
            message += i + "\n"

    return message


print(password_validator(input()))