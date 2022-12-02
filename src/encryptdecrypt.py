from cryptography.fernet import Fernet

encryptionKey = 'R2SWszpcrbz8vfYmWb9wAkNnvz4p-EA80o2IffuJCiQ='
encoding = 'utf-8'

def encrypt(message):
    return Fernet(encryptionKey).encrypt(message.encode()).decode(encoding)

def decrypt(token):
    return Fernet(encryptionKey).decrypt(token.encode()).decode(encoding)