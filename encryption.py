from cryptography.fernet import Fernet

# Genera una clave de encriptación y guárdala en un archivo
def generate_key(file_path):
    key = Fernet.generate_key()
    with open(file_path, 'wb') as key_file:
        key_file.write(key)

# Lee la clave de encriptación desde un archivo
def load_key(file_path):
    return open(file_path, 'rb').read()

# Encripta los datos utilizando la clave
def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Desencripta los datos utilizando la clave
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()