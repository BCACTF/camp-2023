# JailBreak

The `exec` function in python is very dangerous, especially with it executing an input given by the user. 

This is what `PyJail` problems are built off of, where they restrict inputs, functions, or anything else to make it more challenging to get the flag.

Based off of the banned keys, `gdvxftundmn'~`\``@#$%^&*-/.{}`, there are only a few functions we can use, one of which is the key to solving the problem, `locals`.

`locals` is a function that has reference to all of the local parameters, including the `flag` variable which stores the flag. But since the `flag` has banned characters, we must use `chr()` function with the ascii value of each letter and join them together.  

```
locals()[chr(102)+chr(108)+chr(97)+chr(103)]
```

Using this input, the flag will be printed out.