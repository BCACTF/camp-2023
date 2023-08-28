# Java Rev Three

This Java Rev challenge compares the chars of each of the strings against each other, and compares them to the difference located in the `distanceBetweenChars` array.

To solve this problem, you must first delete the `return False;` in the `checkPassword`, which enables the program to keep going even if the first character is wrong.

Then you must put a print statement inside the for loop which prints the correct character of the flag, such as:

```
System.out.print((char) (secondChar+distanceBetweenChars[i]));
```

and once running the program, input a random input such as:

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

producing the correct flag in the terminal.