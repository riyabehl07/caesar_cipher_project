import caesar_cipher

def main():
    print("Caesar Cipher with Keyword Encryption")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("Enter the text: ")
    keyword = input("Enter the keyword: ")

    if choice == 'e':
        encrypted_text = caesar_cipher.caesar_cipher_encrypt(text, keyword)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        decrypted_text = caesar_cipher.caesar_cipher_decrypt(text, keyword)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
