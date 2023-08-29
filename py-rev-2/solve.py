dict = {'D': 13, 'a': 1, 'O': 6, 'u': 7, 'r': 17, 'Y': 5, 'U': 11, '!': 27, 'c': 0, 'A': 15, 'n': 12, 'P': 23, 't': 25, '}': 28, 'h': 20, 'm': 2, 'G': 19, 'f': 9, 'p': 3, '{': 4, 'I': 18, 'T': 21, 'H': 26, '4': 24, 'o': 10}
# We can see that the program simply checks each character of the input to ensure its index matches the dictionary, skipping underscores.
# So we just assemble the flag from the dictionary in reverse - by placing each character in its corresponding spot (underscores fill the rest).
flag = "_" * 29 # length of flag, based on position of }
for char, index in dict.items():
    flag = flag[:index] + char + flag[index+1:] # replace character at index with char from dict
print(flag)