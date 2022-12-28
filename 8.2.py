def encrypt(text, shift):
    new_text = ""
    for i in text:
        shifted = ord(i) + shift
        if shifted >= 123:
            print(shifted)
            shifted = 97 + (shifted - 123)
            print(shifted)
        new_text += chr(shifted)
    return new_text
def decrypt(text, shift):
    new_text = ""
    for i in text:
        shifted = ord(i) - shift
        if shifted < 97:
            print(shifted)
            shifted = 123 - (97 - shifted)
            print(shifted)
        new_text += chr(shifted)
    return new_text

def caesar(text, shift, code):
    if code == "decode":
        return decrypt(text, shift)
    else:
        return encrypt(text,shift)


alphabet = [chr(x) for x in range(97, 123)]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



print(caesar(text, shift, direction))