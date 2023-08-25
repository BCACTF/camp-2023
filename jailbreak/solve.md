# JailBreak

The `eval` function in python is very dangerous, especially with it evaluating an input given by the user. For instance, if you type evaluatate a string with the value of `randomVariable`, it will evaluatate to the value of a variable `randomVariable`. 

This can be used to retrieve the flag, as when it asked for the user input, if you give it `hidden_flag`, it will print out contents of the `hidden_flag` variable, which in this case is the flag.