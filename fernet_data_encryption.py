from cryptography.fernet import Fernet
import os

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load the previously generated key
def load_key():
    if not os.path.exists("secret.key"):
        print("Key file not found. Generating a new key.")
        return generate_key()  # Create a new key if not found
    return open("secret.key", "rb").read()

# Encrypt a message
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Encrypt a file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

    print(f"File '{file_path}' has been encrypted and saved as '{file_path}.encrypted'.")

# Decrypt a file
def decrypt_file(encrypted_file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_file_path = encrypted_file_path.replace('.encrypted', '')
    
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"File '{encrypted_file_path}' has been decrypted and saved as '{original_file_path}'.")

# Example usage
if __name__ == "__main__":
    while True:
        choice = input("Do you want to (1) encrypt a message, (2) decrypt a message, (3) encrypt a file, (4) decrypt a file, or (5) exit? ")

        if choice == '1':
            original_message = input("Enter the message to encrypt: ")
            encrypted = encrypt_message(original_message)
            print(f"Encrypted message: {encrypted}")

        elif choice == '2':
            encrypted_message = input("Enter the encrypted message: ")
            decrypted = decrypt_message(encrypted_message.encode())
            print(f"Decrypted message: {decrypted}")

        elif choice == '3':
            file_path = input("Enter the path of the file to encrypt: ")
            if os.path.exists(file_path):
                encrypt_file(file_path)
            else:
                print("File not found!")

        elif choice == '4':
            encrypted_file_path = input("Enter the path of the encrypted file: ")
            if os.path.exists(encrypted_file_path) and encrypted_file_path.endswith('.encrypted'):
                decrypt_file(encrypted_file_path)
            else:
                print("Encrypted file not found or invalid format!")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
