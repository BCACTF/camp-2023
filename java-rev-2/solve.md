# Java Rev Two

This Java Rev challenge has an array with all of ascii values of the flag, however, they seem a little bit too high to fit into the normal 128 values. 

This is where `modulus` or the `%`, which acts sort of like a `division` statement. However, instead of returning the evaluated results, it gives us the remainder. In this case, it takes `nums[i] % 128`, which means that it gets the number from the array and then takes the remainder of that number after being divided by 128. 

For example, 6113 divided by 128 is 47, remainder 97. As such, 6113 mod 128 = 97

To solve this problem, you must first delete the `return False;` in the `checkPassword`, which enables the program to keep going even if the first character is wrong.

Then you must put a print statement inside the for loop which prints the correct character of the flag, such as:

```
System.out.print((char) (nums[i] % 128));
```

Note that `(char)` will display the corresponding character for the number.

Once you run the program, input a long and random input such as:

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

which will produce the correct flag in the terminal.