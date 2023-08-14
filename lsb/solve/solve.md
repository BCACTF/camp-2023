# LSB

LSB stands for least significant bit, and is a simple way of hiding text, especially in binary encoded files, such as images.

To encode, the least significant bit of each byte is changed to the next bit of the message. For example, if the message is "hello", the first few bytes of the image would be changed to:

Since the least significant bit of each byte is changed, the image will look almost exactly the same, and the message can be retrieved by reversing the process.

For example, if one byte in our image is `10010101`, the binary place value is greatest at the right most side of the byte.

In order to decode LSB, we can use an online tool or write our own script in python, as seen in the [dec.py](dec.py) file.

Run it, redirecting the output to a file, and you will get the flag.
```bash
    python dec.py > out.txt
```

```text
camp{!3aSt_$iGn!fic@nT_B!7s_fbruw9ni24u9f}
```