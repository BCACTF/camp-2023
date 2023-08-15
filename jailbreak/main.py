import time

def sanitize(letter):
    print("Checking for contraband...")
    return any([i in letter.lower() for i in BANNED_CHARS])

BANNED_CHARS = ""

print("Welcome to the prison's mail center")
msg = input("Please enter your message: ")

if not sanitize(msg): 
    print("Contraband letters found!\nMessage Deleted!")
    exit()

exec(msg)