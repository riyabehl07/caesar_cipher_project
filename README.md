#  Caesar Cipher with Keyword Encryption

A modern twist on the classic Caesar Cipher! This Python-based application uses a **keyword-based Caesar cipher** for encryption and decryption, along with a simple **transposition step** (string reversal) for added security. It includes both a **Graphical User Interface (GUI)** using Tkinter and a **Command-Line Interface (CLI)** version.

##  How It Works

- Each character in the text is shifted by a value determined by a keyword.
- After shifting, the encrypted string is reversed for additional obfuscation.
- Decryption performs the reverse operations in order.

###  Example

**Input:** `HELLO`, **Keyword:** `KEY`  
**Encrypted Output:** `...` *(based on shifts and reverse)*  
**Decryption** restores the original text.

##  Features

- Keyword-based Caesar cipher with dynamic character shifting
- Extra layer of encryption with text reversal
- GUI with Tkinter for user-friendly experience
- CLI version for quick terminal usage
- Handles both uppercase and lowercase letters
- Skips non-alphabetic characters

##  Technologies Used

- **Programming Language:** Python 3
- **Libraries:** Tkinter (for GUI), Standard Python modules


##  How to Run

1. Clone the Repository
```bash
git clone https://github.com/yourusername/caesar_cipher_project.git
cd caesar_cipher_project

2. Run the GUI Version
python gui.py
This will launch a Tkinter window for encrypting and decrypting text.

3. Run the CLI Version

python caesar_cipher_project.py\
You’ll be prompted to input the text, keyword, and your action (encrypt/decrypt).





