def de_cipher(content, SYMBOLS, key):
    """Function to (de)cipher a message"""
    # Check if key is an integer value
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
            # Subtract the key to decipher
            a += SYMBOLS[(SYMBOLS.find(i.upper())-key) % 26]
    return a

# Add symbols in a list
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("What message would you like to decipher?")
cipher = input("> ")

for key in range(26):
    message = de_cipher(cipher, SYMBOLS, key)
    print(f"Key #{key}: {message}")
