alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def caesarCipher(text, shift, direction):
    caesar_text = ""
    for letter in text:
        # if the letter is a space, don't shift the space add it as it is to the string
        if letter == " ":
            caesar_text += " "
            continue
        # if the letter is a number, don't shift the number add it as it is to the string
        elif letter in numbers:
            caesar_text += letter
            continue

        position = alphabet.index(letter)
        # if the shift is higher than 27, get the modulo so the shift won't be out of index lenght
        if shift > 26:
            shift = shift % 26

        # based on the direction the message is encoded or decoded
        if direction == "encode":
            if position + shift > 25:
                new_position = (position + shift) - 26
            else:
                new_position = position + shift
            caesar_text += alphabet[new_position]
        elif direction == "decode":
            new_position = -(shift) + position
            caesar_text += alphabet[new_position]
        else:
            print("Your input does not match 'encode' or 'decode'")
            exit()

    print(f"The {direction}d text is {caesar_text}\n")