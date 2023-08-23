#camp{THis_wA5_SUPpO5E_to_Be_5Ecur3_b34018d8b0f1e}
def passwordChecker(guess):
    flag = {'D': 13, 'a': 1, 'O': 6, 'u': 7, 'r': 17, 'Y': 5, 'U': 11, '!': 27, 'c': 0, 'A': 15, 'n': 12, 'P': 23, 't': 25, '}': 28, 'h': 20, 'm': 2, 'G': 19, 'f': 9, 'p': 3, '{': 4, 'I': 18, 'T': 21, 'H': 26, '4': 24, 'o': 10}
    
    for i in range(len(guess)):
        letter = guess[i]
        if flag.get(letter) != None:
            if flag[letter] == i:
                continue
        if letter == "_": continue
        return False

    return True


guess = input("Enter the password: ")

if passwordChecker(guess): print("That's the right password!")
else: print("That's the incorrect password!")