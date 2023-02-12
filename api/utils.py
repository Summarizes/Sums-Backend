from hashlib import sha512

def encryption(text):
    encoded = str(text).encode('utf8')
    hashed = sha512(encoded)
    return hashed.hexdigest()

def form_to_dict(form):
    dict_data = {**form}
    return {i:dict_data[i][0] for i in dict_data}