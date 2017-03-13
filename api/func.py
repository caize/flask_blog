#md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str.encode('utf-8'))
    return m.hexdigest()