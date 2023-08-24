# XylophOner Solvepath

The challenge name alludes to XOR, a type of boolean logic that is true only if one of the values is true, not both. The code provided turns every letter of the flag into hex and then into binary, and the XORs the corresponding digits.

XOR is commonly used in cryptology with a key, or in this case the `flag`, where every string is XORed against the key.

Something notable about using XOR with a key is that is predictable. For example, we have a key `key`, and input `in`, and the output of XORing `key` and `in`, `out`. Using XOR of any two of them will produce the other one, for example, `key` and `out` will produce `in`, and most importantly `out` and `in` will produce `key`.

Using this in the challenge, we have our input `inp` and our key `flag`. If we try using a test input (Something random) like 50 of the same character.

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

And we will get an output such as 

```
02000c111a3851143e5533043e553e3951333e2209550c11502e0f3e40401c02000c111a3851143e5533043e553e3951333e
```

And using our above logic, we now have a `in` and `out`, and XORing them against each other in `XylOphoneR.py` like this,

```
flag = "02000c111a3851143e5533043e553e3951333e2209550c11502e0f3e40401c02000c111a3851143e5533043e553e3951333e" # The output
inp = hexify("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") # the same input as above
```

will produce our flag in hex, and using a hex to ascii converter like [RapidTables](https://www.rapidtables.com/convert/number/hex-to-ascii.html), we can get our flag.

```
camp{Y0u_4Re_4_X0R_Ch4mp1On_!!}
```