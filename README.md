cipherchallenge

IF YOU GOT HERE FROM MY DISCORD PROFILE, READ "cipher 1.txt" FOR AN EXPLANATION.

This is a collection of cryptanalysis tools for the National Cipher Challenge, and now my personal cipher challenge.

Caesar Decryptor.py decrypts caesar ciphers with a known key. Requires English.py

Caesar Encryptor.py encrypts caesar ciphers. Requires English.py

Caesar breaker.py deterministically breaks caesar ciphers where the word spacing is preserved. (i.e. 'he was a person' will work, but 'he wa sa pe rs on' will not). Requires English.py

Clumped Caesar Breaker v2.py heuristically breaks caesar ciphers regardless of whether word spacing is preserved, using frequency analysis. Requires English.py

English.py is a module required by several of the other programs here. It provides useful tools for crytanalysis.

Vigenere encryptor.py encrypts vigenere ciphers. Requires English.py

Vigenere Frequencies v2.py heuristically breaks vigenere ciphers of a key-length entered by the programmer, using frequency analysis. Requires English.py

Vigenere Frequencies v3.py heuristically breask vigenere ciphers of an unknown key-length, using frequency analysis. Requires English.py

binary to text.py deterministically converts 5 bit encoding to text. This is not a standard cipher, but was featured.

digrams.json is required by transposition v3.py

frequency analysis.py runs frequency analysis on entered text, and offers letter swapping capabilities. Uses: monoalphabetic ciphers, identifying other ciphers. Requires English.py

polybius.py deterministically breaks the polybius cipher. Alterations to the variable "alpha" may be required, dependant on the challenge.

transposition v3.py heuristically breaks transposition ciphers. Requires English.py and digrams.json

vigenere decryptor.py decrypts vigenere cipherss with a known key. Requires English.py
