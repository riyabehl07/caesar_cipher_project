def caesar_cipher_encrypt(text, keyword):
    encrypted_text = ''
    keyword_shifts = [ord(char) - ord('A') for char in keyword.upper()]
    keyword_length = len(keyword_shifts)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = keyword_shifts[i % keyword_length]
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char

    # Simple transposition step (reverse the string)
    encrypted_text = encrypted_text[::-1]

    return encrypted_text

def caesar_cipher_decrypt(text, keyword):
    # Reverse the transposition step
    text = text[::-1]
    
    decrypted_text = ''
    keyword_shifts = [ord(char) - ord('A') for char in keyword.upper()]
    keyword_length = len(keyword_shifts)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = keyword_shifts[i % keyword_length]
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char

    return decrypted_text
