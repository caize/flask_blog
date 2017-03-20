#md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str.encode('utf-8'))
    return m.hexdigest()

def md5sum(filename):
    file_object = open(filename, 'rb')
    file_content = file_object.read()
    file_object.close()
    file_md5 = hashlib.md5(file_content)
    return file_md5