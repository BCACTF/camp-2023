def sanitize():
    try:
        return eval(msg)
    except Exception:
        return str(msg)

try:
    global hidden_flag
    with open("flag.txt","r") as f:
        hidden_flag = f.read()

except Exception:
    hidden_flag = "REDACTED"


print("Welcome to the prison's mail center")
msg = input("Please enter your message: ")

print("Your message is:",end=' ')
print(sanitize())