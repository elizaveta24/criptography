import codecs
def open_files(): 
    text_file = ''  
    f = codecs.open('D:/proekt_crypto/test_file/text.txt', encoding='utf-8')
    for i in f:
        text_file+=i
    f.close()
    return text_file
def write_files(text):
    f = codecs.open('D:/proekt_crypto/test_file/encode_file_belazo.txt','w')
    f.write(text)
    f.close()
def encrypt (text,key):
    encode = ''
    key *= len(text) // len(key) + 1 
    for i,j in enumerate(text):
        temp = ord(j) + ord(key[i])#складываем числа символов ключа и текста
        encode += chr(temp % 32 + ord('а'))#берем модуль от суммы, 
        #у нас получается разница и прибавляем число символа а от которого начинается отсчет
    return encode
def decrypt (text,key):
    decode = ''
    key *= len(text) // len(key) + 1 
    for i,j in enumerate(text):
        temp = ord(j) - ord(key[i])
        decode += chr(temp % 32 + ord('а'))
    return decode
key = input('Введите ключ:').lower()
input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encrypt(input_text,key)
decrypted = decrypt(encrypted,key)
text_file = open_files()
str_text_file = open_files().lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted_file = encrypt(str_text_file,key)
decrypted_file = decrypt(encrypted_file,key)
write = write_files(encrypted_file)
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')
print(f'текст файла:{text_file}')
print(f'Зашифрованный текст файла:{encrypted_file}')
print(f'Расшифрованный текст файла:{decrypted_file}')