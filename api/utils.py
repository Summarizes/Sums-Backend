from hashlib import sha512

def encryption(text):
    encoded = str(text).encode('utf8')
    hashed = sha512(encoded)
    return hashed.hexdigest()