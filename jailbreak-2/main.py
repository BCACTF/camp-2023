def sanitize(letter):
    print("Checking for contraband...")
    return any([i in letter.lower() for i in BANNED_CHARS])

BANNED_CHARS = "gdvxcfiyunrdmn'~`@#$%^&*-/.{}0123456789"
solve = "locals()[chr(102)+chr(108)+chr(97)+chr(103)]"
flag = "REDACTED"

print("Welcome to the prison's mail center")

msg = input("\nPlease enter your message: ")

while msg != "":
    if sanitize(msg): 
        print("Contraband letters found!\nMessages Deleted!")
        exit()

    try:
        exec(msg)
    except Exception as e:
        print(f'Error occured: {str(e)}; Message could not be sent.')

    msg = input("\nPlease enter your message: ")