def sanitize(letter):
    print("Checking for contraband...")
    return any([i in letter.lower() for i in BANNED_CHARS])

def end():
    print("Contraband letters found!\nMessage Deleted!")
    exit()

BANNED_CHARS = "gdvxftundmn'~`@#$%^&*-/.{}"
flag = "REDACTED"

print("Welcome to the prison's mail center")
msg = input("Please enter your message: ")

if sanitize(msg): 
    end()

try:
    x = eval(msg)
    if len(x) != len(flag): end()
    print(x)
except Exception as e:
    print(f'Error occured: {str(e)}; Message could not be sent.')