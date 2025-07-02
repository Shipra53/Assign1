from cryptography.fernet import Fernet

def get_fernet(key):
    return Fernet(key)

# Encrypt file data
def encrypt_file(file_data, key):
    fernet = get_fernet(key)
    return fernet.encrypt(file_data)

# Decrypt file data
def decrypt_file(encrypted_data, key):
    fernet = get_fernet(key)
    return fernet.decrypt(encrypted_data)
