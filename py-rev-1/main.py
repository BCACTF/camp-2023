def passwordChecker(guess):
    if guess[:5] == "camp{":
        if guess[41:43] == "d8":
            if guess[12:15] == "5_S":
                if guess[30:34] == "cur3":
                    if guess[23:30] == "o_Be_5E":
                        if guess[5:12] == "THis_wA":
                            if guess[15:23] == "UPpO5E_t":
                                if guess[43:] == "b0f1e}":
                                    if guess[34:41] == "_b34018":
                                        return True

    return False


guess = input("Enter the password: ")

if passwordChecker(guess):
    print("That's the right password!")
else:
    print("That's the incorrect password!")