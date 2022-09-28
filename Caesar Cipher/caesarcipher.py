def de_cipher(content, SYMBOLS, decipher=False):
    """Function to (de)cipher a message"""
    # Check if key is an integer value
    while True:
        key = input("> ")
        if key.isdecimal():
            pass

        key = int(key)

        a = ''
        for i in content:
            # Keep spaces intact
            if i == ' ':
                a += ' '
            # Keep numbers intact
            elif i.isnumeric():
                a += i
            else:
                if decipher:
                    # Subtract the key to decipher
                    a += SYMBOLS[(SYMBOLS.find(i.upper()) - key) % 26]
                else:
                    # Add the key to encrypt
                    a += SYMBOLS[(SYMBOLS.find(i.upper()) + key) % 26]
        return a


# Add symbols in a list
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("""
A Caesar cipher is an ancient way to encrypt
messages by shifting each letter in the message
by a certain integer value in the alphabet.
This integer value is called a key. For instance
if the key was 2, the message 'hello' would become
JGNNQ, because 'h' is the 8th letter in the alphabet
so we add 2 to find the 10th letter which is 'j'. 
""")

print("""Would you like to (e)ncrypt or (d)ecipher?""")
# Ask user if they want to encrypt or decipher and keep
# asking until a valid answer is given
while True:
    mode = input("> ")
    if mode[0].lower() in ("e", "d"):
        break

if mode[0] == "e":
    # User wants to encrypt
    print("What message would you like to encrypt?")
    message = input("> ")
    print("What key would you like to use?")
    cipher = de_cipher(message, SYMBOLS)
    print(cipher)

else:
    # User wants to decipher
    print("What message would you like to decipher?")
    cipher = input("> ")
    print("What key would you like to use?")
    message = de_cipher(cipher, SYMBOLS, decipher=True)
    print(message)
