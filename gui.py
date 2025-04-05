import tkinter as tk
from tkinter import messagebox
import caesar_cipher

def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    keyword = keyword_entry.get().strip()
    if not text or not keyword:
        messagebox.showwarning("Input Error", "Please provide both text and keyword.")
        return
    encrypted_text = caesar_cipher.caesar_cipher_encrypt(text, keyword)
    result_text.set(encrypted_text)

def decrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    keyword = keyword_entry.get().strip()
    if not text or not keyword:
        messagebox.showwarning("Input Error", "Please provide both text and keyword.")
        return
    decrypted_text = caesar_cipher.caesar_cipher_decrypt(text, keyword)
    result_text.set(decrypted_text)

app = tk.Tk()
app.title("Caesar Cipher with Keyword Encryption")

# Text Entry
tk.Label(app, text="Enter Text:").grid(row=0, column=0, padx=10, pady=10)
text_entry = tk.Text(app, height=10, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=10)

# Keyword Entry
tk.Label(app, text="Enter Keyword:").grid(row=1, column=0, padx=10, pady=10)
keyword_entry = tk.Entry(app)
keyword_entry.grid(row=1, column=1, padx=10, pady=10)

# Encrypt Button
encrypt_button = tk.Button(app, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

# Decrypt Button
decrypt_button = tk.Button(app, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Result Display
tk.Label(app, text="Result:").grid(row=3, column=0, padx=10, pady=10)
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, wraplength=400)
result_label.grid(row=3, column=1, padx=10, pady=10)

app.mainloop()
