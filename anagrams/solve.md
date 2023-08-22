# Anagrams

The hint suggests that we should look up what a buffer overflow is. 

A quick google search returns this wikipedia result: [https://en.wikipedia.org/wiki/Buffer_overflow](https://en.wikipedia.org/wiki/Buffer_overflow)

> A buffer overflow, or buffer overrun, is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory locations.

If we read the source code, we can see that the author has lazily used the same string to store the user input and the flag. A null terminator is placed at the expected length of the user input, but the code does not restrict the size of our input. 

With the right length string, we can overwrite the `\0` (null terminator) and read the flag. In general, about 13 characters more than requested will suffice, as defined by the `SPACE` constant. Note that too many characters will cause part of the flag to be overwritten.

```bash
./anagrams
```

```text
Welcome to bofed!
The game is simple: I'll tell you a number, and you have to tell me an anagram of that length.
Let's see how far you can get!
Give me an anagram of length 5: aaaaaaaaaaaaaaaaaa
Checking the validity of the anagram... aaaaaaaaaaaaaaaaaacamp{7o0_m@nY_ch@RacteR5_buf349nrf}
Incorrect!
You got 0 correct!
```