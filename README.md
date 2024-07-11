**Prodigy Infotech: Caesar Cipher Encryption and Decryption Program:**

**Introduction:**

The Caesar Cipher is a classical encryption algorithm named after Julius Caesar, who used it for private correspondence. This algorithm involves shifting each letter of the plaintext by a fixed number of positions down the alphabet. This Python program offers a straightforward implementation of the Caesar Cipher, providing both encryption and decryption functionalities.

**Features:**
**Encryption:**

* Functionality: Converts plaintext into encrypted text by shifting each letter according to a user-defined shift value.

* Process: Each letter in the input text is shifted by a specified number of positions in the alphabet.
For instance, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so forth.
* Result: The output is an encrypted string that conceals the original message, ensuring confidentiality.

**Decryption:**
  
* Functionality: Reverts the encrypted text back to its original form using the same user-defined shift value.
* Process: Each letter in the encrypted text is shifted back by the same number of positions used during encryption.
For instance, if 'D' was shifted by 3 to become 'A', shifting 'A' back by 3 will return 'D'.
* Result: The output is the original plaintext, making the hidden message readable again.


**Usage Instructions:**

**Execution:**

To use the program, execute the Python script in a suitable Python environment (e.g., terminal, command prompt, or an IDE like PyCharm or VSCode).

**User Inputs:**

* Choice of Operation: The user will be prompted to choose between encryption and decryption.
* Encryption (E): Converts plaintext to ciphertext.
* Decryption (D): Converts ciphertext back to plaintext.
* Message or Text: The user will provide the text to be encrypted or decrypted.
* Encryption: The plaintext message to be secured.
* Decryption: The encrypted message to be restored to its original form.
* Shift Value: A numerical value defining the number of positions each letter should be shifted.
* Positive Integer: Shifts letters to the right (e.g., 'A' becomes 'D' with a shift of 3).

Same Value for Both Operations: The shift value used for encryption should be the same as the one used for decryption to correctly restore the original message.

