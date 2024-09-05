import string

# Function to encrypt the text by shifting characters to the right by 'num' positions
def encrypt_text(text, num):
    # Initialise an empty string to store the result
    answer = ""
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is an uppercase letter
        if char in string.ascii_uppercase:
            # Shift the character by 'num' positions within the uppercase letters
            shifted_index = (string.ascii_uppercase.index(char) + num) % 26
            answer += string.ascii_uppercase[shifted_index]
        # Check if the character is a lowercase letter
        elif char in string.ascii_lowercase:
            # Shift the character by 'num' positions within the lowercase letters
            shifted_index = (string.ascii_lowercase.index(char) + num) % 26
            answer += string.ascii_lowercase[shifted_index]
        else:
            # Non-alphabetic characters remain unchanged
            answer += char

    # Return the encrypted text
    return answer

# Function to decrypt the text by shifting characters to the left by 'num' positions
def decrypt_text(text, num):
    # Initialise an empty string to store the result
    answer = ""

    # Loop through each character in the input text
    for char in text:
        # Check if the character is an uppercase letter
        if char in string.ascii_uppercase:
            # Shift the character by 'num' positions within the uppercase letters
            shifted_index = (string.ascii_uppercase.index(char) - num) % 26
            answer += string.ascii_uppercase[shifted_index]
        # Check if the character is a lowercase letter
        elif char in string.ascii_lowercase:
            # Shift the character by 'num' positions within the lowercase letters
            shifted_index = (string.ascii_lowercase.index(char) - num) % 26
            answer += string.ascii_lowercase[shifted_index]
        else:
            # Non-alphabetic characters remain unchanged
            answer += char

    # Return the decrypted text
    return answer
    
# ----------------------------------------------------------------------------------------------------------------------------------
print("Welcome to my cipher program!")
print("Please Note: all non-alphabetic characters will not have their position shifted.")

while True:
    choice = input("Welcome! Choose 'e' to encrypt or 'd' to decrypt: \n")

    if choice == "e":
        user_input = input("Type what you would like to encrypt: ")
        num = int(input("How many letters should it be displaced by? "))

        encrypted_text = encrypt_text(user_input, num)

        print("Encrypted text:", encrypted_text)

    elif choice == "d":
        user_input = input("Type what you would like to decrypt: ")
        num = int(input("How many letters should it be displaced by? "))

        decrypted_text = decrypt_text(user_input, num)

        print("Decrypted text:", decrypted_text)

    else:
        print("Invalid choice, please select 'e' or 'd'.")
