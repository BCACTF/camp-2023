#camp{THis_wA5_SUPpO5E_to_Be_5Ecur3_b34018d8b0f1e}
def passwordChecker(guess):
    flag = ['c', 'a', 'm', 'p', '{', 'T', 'H', 'i', 's', '_', 'w', 'A', '5', '_', 'S', 'U', 'P', 'p', 'O', '5', 'E', '_', 't', 'o', '_', 'B', 'e', '_', '5', 'E', 'c', 'u', 'r', '3', '_', 'b', '3', '4', '0', '1', '8', 'd', '8', 'b', '0', 'f', '1', 'e', '}']
    
    return guess == "".join(flag)


guess = input("Enter the password: ")

if passwordChecker(guess): print("That's the right password!")
else: print("That's the incorrect password!")