import hashlib

def calculate_md5(file):
    md5_obj = hashlib.md5()
    md5_obj.update(file.read())
    hash_code = md5_obj.hexdigest()
    md5 = str(hash_code).lower()
    return md5