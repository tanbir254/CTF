# Input the text as a single string
input_text = input()

# Write your solution below and make sure to encode the word correctly
########
import string

def decrypt_char(c, shift):
    """Decrypt a single alphabetical character by shifting it backwards."""
    alphabet = string.ascii_lowercase
    if c in alphabet:
        return alphabet[(alphabet.index(c) - shift) % 26]
    return c  # Keep non-alphabet characters unchanged

def parse_shifts(shift_input):
    """Extract shift values from a bracketed list format (e.g., '[4, 7, 12]')."""
    shift_input = shift_input.strip()[1:-1]  # Remove brackets
    return list(map(int, shift_input.split(",")))  # Convert string numbers to integers

def decrypt_ciphertext(ciphertext, shifts):
    """Decrypt the ciphertext while keeping spaces in their original positions."""
    clean_text = [c for c in ciphertext if c.isalpha()]  # Extract only letters
    decrypted_text = list(ciphertext)  # Initialize with original text (to keep spaces)
    letter_positions = [i for i, c in enumerate(ciphertext) if c.isalpha()]  # Track letter positions

    index = 0
    for shift in shifts:
        group = clean_text[index:index+5]  # Extract next 5-character group
        decrypted_group = [decrypt_char(c, shift) for c in group]

        # Replace only the letters in the original text
        for j, char_index in enumerate(letter_positions[index:index+len(decrypted_group)]):
            decrypted_text[char_index] = decrypted_group[j]

        index += len(group)  # Move to the next group

    return "".join(decrypted_text)  # Convert list back to string

# Example input
ciphertext = input_text
num_groups = int(input())  # Unused, kept for compatibility
shift_input = input()

# Parse shift values
shifts = parse_shifts(shift_input)

# Decrypt and display the result
decrypted_text = decrypt_ciphertext(ciphertext, shifts)
print(decrypted_text)


