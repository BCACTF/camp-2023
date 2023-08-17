# LSB

LSB stands for least significant bit, and is a simple way of hiding text, especially in binary encoded files, such as images.

To encode, the least significant bit of each byte is changed to the next bit of the message. The image will look almost exactly the same, since the tiny difference does not affect the color by a perceivable amount, and the message can be retrieved by reversing the process.

The most significant bit in a byte is worth 2^7 or 128, while the least significant bit is only worth 2^0 or 1. Changing the lesser one will not affect the color significantly, so we can chain the least significant bits of each byte to encode a message.

In order to decode LSB, we can use an online tool or write our own script in python, as seen in the [dec.py](dec.py) file.

Run it, redirecting the output to a file, and you will get the flag.
```bash
    python dec.py > out.txt
```

```text
camp{!3aSt_$iGn!fic@nT_B!7s_fbruw9ni24u9f}
```