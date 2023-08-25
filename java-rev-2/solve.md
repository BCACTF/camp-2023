# Java Rev Two

This Java Rev challenge has an array with all of ascii values of the flag, however, they seem a little bit too high to fit into the normal 128 values. 

This is where `modulus` or the `%`, which acts sort of like a `division` statement but is instead of taking the evaluated results, it takes the remainer. In this case, it takes `nums[i] % 128`, which means that it gets the number from the array and then takes the remainer of that number after being divised by 128. 

To solve this problem, you must first delete the `return False;` in the `checkPassword`, which enables the program to keep going even if the first character is wrong.

Then you must put a print statement inside the for loop which prints the correct character of the flag, such as:

```
System.out.print((char) (nums[i] % 128));
```

and once running the program, input a random input such as:

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

producing the correct flag in the terminal.