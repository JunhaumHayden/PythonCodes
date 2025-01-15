import hashlib
import os
import tkinter as tk
from tkinter import messagebox

from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt_file():
    filename = filename_entry.get()
    content = content_text.get("1.0", tk.END).strip()

    if not filename:
        filename = "texto.txt"

    encrypted_content = cipher_suite.encrypt(content.encode())
    with open(filename, "wb") as file:
        file.write(encrypted_content)

    hash_code = hashlib.sha256(encrypted_content).hexdigest()
    with open("hash_code.txt", "w") as hash_file:
        hash_file.write(hash_code)

    hash_text.delete("1.0", tk.END)
    hash_text.insert(tk.END, hash_code)
    messagebox.showinfo("Success", "File encrypted successfully!")


def decrypt_file():
    filename = filename_entry.get()
    hash_code = hash_text.get("1.0", tk.END).strip()

    if not filename:
        filename = "texto.txt"

    if not os.path.exists(filename):
        messagebox.showerror("Error", "File not found!")
        return

    with open(filename, "rb") as file:
        encrypted_content = file.read()

    current_hash_code = hashlib.sha256(encrypted_content).hexdigest()

    if current_hash_code != hash_code:
        messagebox.showerror("Error", "Hash codes do not match!")
        return

    decrypted_content = cipher_suite.decrypt(encrypted_content).decode()
    with open(filename, "w") as file:
        file.write(decrypted_content)

    content_text.delete("1.0", tk.END)
    content_text.insert(tk.END, decrypted_content)
    messagebox.showinfo("Success", "File decrypted successfully!")


def update_hash_code():
    filename = filename_entry.get()

    if not filename:
        filename = "texto.txt"

    if not os.path.exists(filename):
        messagebox.showerror("Error", "File not found!")
        return

    with open(filename, "rb") as file:
        encrypted_content = file.read()

    hash_code = hashlib.sha256(encrypted_content).hexdigest()
    hash_text.delete("1.0", tk.END)
    hash_text.insert(tk.END, hash_code)


def load_file_content():
    filename = filename_entry.get()

    if not filename:
        filename = "texto.txt"

    if not os.path.exists(filename):
        messagebox.showerror("Error", "File not found!")
        return

    with open(filename, "r") as file:
        content = file.read()

    content_text.delete("1.0", tk.END)
    content_text.insert(tk.END, content)
    messagebox.showinfo("Success", "File content loaded successfully!")


# Create the main window
root = tk.Tk()
root.title("Encrypt/Decrypt System")

# Create and place the widgets
tk.Label(root, text="Filename:").grid(row=0, column=0, padx=10, pady=10)
filename_entry = tk.Entry(root)
filename_entry.insert(0, "texto.txt")
filename_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Content:").grid(row=1, column=0, padx=10, pady=10)
content_text = tk.Text(root, height=10, width=70)
content_text.grid(row=1, column=1, padx=10, pady=10)

load_button = tk.Button(root, text="Load File Content", command=load_file_content)
load_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

tk.Label(root, text="Hash Code:").grid(row=3, column=0, padx=10, pady=10)
hash_text = tk.Text(root, height=1, width=70)
hash_text.grid(row=3, column=1, padx=10, pady=10)

update_hash_button = tk.Button(root, text="Update Hash Code", command=update_hash_code)
update_hash_button.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_file)
encrypt_button.grid(row=5, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_file)
decrypt_button.grid(row=5, column=1, padx=10, pady=10)


# Run the main loop
root.mainloop()
