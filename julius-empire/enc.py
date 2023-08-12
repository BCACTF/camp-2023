flag = 'camp{caesar_what_a_cool_cipher_ejeekwnenjdkwef}'

enc = ''
rot = 13
for char in flag:
    print(char,end='.')
    if char in 'abcdefghijklmnopqrstuvwxyz':
        enc += chr((ord(char) + rot-97) % 26 + 97)
    else:
        enc += char

with open('flags.txt','a+') as f:
    f.write(enc + '\n')