import hashlib

def calculate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

file_name = input("Enter file name: ")

try:
    original_hash = calculate_hash(file_name)
    print("Original Hash:", original_hash)

    input("\nPress Enter after modifying the file...")

    new_hash = calculate_hash(file_name)
    print("New Hash:", new_hash)

    if original_hash == new_hash:
        print("\nFile integrity intact. No changes detected.")
    else:
        print("\nWarning! File has been modified.")

except FileNotFoundError:
    print("File not found.")
