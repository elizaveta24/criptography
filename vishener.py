
import codecs
def open_files(): 
    text_file = ''  
    f = codecs.open('D:/proekt_crypto/test_file/text.txt', encoding='utf-8')
    for i in f:
        text_file+=i
    f.close()
    return text_file
def write_files(text):
    f = codecs.open('D:/proekt_crypto/test_file/encode_file_vishener.txt','w')
    f.write(text)
    f.close()

def encrypt (text):
    encode = ''
    encoded = ''
    key = 'к'
    for j in text:
        temp = ord(j) + ord(key)#складываем числа символов ключа и текста
        encode = chr(temp % 32 + ord('а'))#берем модуль от суммы, 
        #у нас получается разница и прибавляем число символа а от которого начинается отсчет
        key = encode #сохраняем символ в ключ
        encoded += encode
    return encoded
def decrypt (text):
    decode = ''
    decoded = ''
    key = 'к'
    for j in text:
        temp = ord(j) - ord(key)#складываем числа символов ключа и текста
        decode = chr(temp % 32 + ord('а'))#берем модуль от суммы, 
        #у нас получается разница и прибавляем число символа а от которого начинается отсчет
        key = j #сохраняем букву в ключ
        decoded += decode
    return decoded
input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encrypt(input_text)
decrypted = decrypt(encrypted)
text_file = open_files()
str_text_file = open_files().lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted_file = encrypt(str_text_file)
decrypted_file = decrypt(encrypted_file)
write = write_files(encrypted_file)
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')
print(f'Зашифрованный текст файла:{encrypted_file}')
print(f'Расшифрованный текст файла:{decrypted_file}')
