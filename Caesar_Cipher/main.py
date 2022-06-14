# recreating caesar cipher using python
# the main idea is to encode and decode a message by shifting the alphabet
import art
from Cipher import caesarCipher as caesar

print(art.logo)
is_active = True
while is_active:
    direction = input("\nType 'encode' to encrypt. type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    exit_program = input("Type 'exit' to exit from the program\nTo try another text press enter: ").lower()

    if exit_program == "exit":
        is_active = False
