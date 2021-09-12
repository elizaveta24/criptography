
def encrypt (text):
    encode = ''
    encoded = ''
    key = 'к'
    for j in text:
        temp = ord(j) + ord(key)#складываем числа символов ключа и текста
        encode = chr(temp % 32 + ord('а'))#берем модуль от суммы, 
        #у нас получается разница и прибавляем число символа а от которого начинается отсчет
        key = encode
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
        key = j
        decoded += decode
    return decoded
input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encrypt(input_text)
decrypted = decrypt(encrypted)
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')
