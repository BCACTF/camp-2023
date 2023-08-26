# Intro To RSA 1

RSA is a popular type of asymmetric encryption algorithm used in cryptology. Public keys are used for encryption, and the private keys are used for decryption.

In this case, we have the 2 private keys, `p` and `q`, as well as one of the public keys `e`, and the ciphertext `c`.

To use decryption, you need private key exponent `d`, and to calculate this, you take the modular multiplicative inverse of `e`, and mod it by `(p-1)(q-1)`.

Once you have `d`, the decryption is simple. All you need to do is take `c` or the cipher text, and raise it to the `d` power, modded by `p*q`.

Once you do this, you will get the number as a integer in base 10. However, as noted in the challenge description, the message is turned into hex and then into an int, so to get the plaintext, you have to convert it into hex, and the convert it into text from there.