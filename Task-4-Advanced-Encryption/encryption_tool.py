from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(filename, password):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print("File encrypted successfully.")

def decrypt_file(filename, password):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print("File decrypted successfully.")

def main():
    print("\n--- Advanced Encryption Tool (AES-256) ---")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Enter your choice: ")
    filename = input("Enter file name: ")
    password = input("Enter password: ")

    if choice == "1":
        encrypt_file(filename, password)
    elif choice == "2":
        decrypt_file(filename, password)
    else:
        print("Invalid choice!")

if _name_ == "_main_":
    main()
