def sanitize():
    try:
        return eval(msg)
    except Exception:
        return str(msg)

hidden_flag = "REDACTED"

print("Welcome to the prison's mail center")
msg = input("Please enter your message: ")

print("Your message is: "+sanitize())