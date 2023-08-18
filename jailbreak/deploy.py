def sanitize(letter):
    print("Checking for contraband...")
    return any([i in letter.lower() for i in BANNED_CHARS])

BANNED_CHARS = "gdvxftundmn'~`@#$%^&*-/.{}"
flag = "REDACTED"

print("Welcome to the prison's mail center")
msg = input("Please enter your message: ")

if sanitize(msg): 
    print("Contraband letters found!\nMessage Deleted!")
    exit()

try:
    exec(msg)
except Exception as e:
    print(f'Error occured: {str(e)}; Message could not be sent.')