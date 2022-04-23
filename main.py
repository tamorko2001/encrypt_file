import os
import pyAesCrypt

def crypter(mode, _file):
    password = input('Enter password: ')
    buffer = 512 * 1024
    ext = _file.split('.')

    if(int(mode) == 0 ):
        pyAesCrypt.encryptFile(_file, ext[0].lower() + '.cw' , password, buffer)
    
    elif(int(mode) == 1):
        _type = input('Enter _type: ')
        pyAesCrypt.encryptFile(_file, ext[0].lower() + '.' + _type, password, buffer)

    os.remove(_file)

print('... File Crypring ...')
print('0 - Crypt')
print('1 - Decrypt')

mode = input('Enter mode: ')
filename = input('Enter filename: ')
crypter(mode, filename)