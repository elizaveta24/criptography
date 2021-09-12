
def encrypt (text,key):
    encode = ''
    key *= len(text) // len(key) + 1 
    for i,j in enumerate(text):
        temp = ord(j) + ord(key[i])#складываем числа символов ключа и текста
        encode += chr(temp % 32 + ord('б'))#берем модуль от суммы, 
        #у нас получается разница и прибавляем число символа а от которого начинается отсчет
    return encode
def decrypt (text,key):
    decode = ''
    key *= len(text) // len(key) + 1 
    for i,j in enumerate(text):
        temp = ord(j) - ord(key[i])
        decode += chr(temp % 32 + ord('б'))
    return decode
key = input('Введите ключ:').lower()
input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encrypt(input_text,key)
decrypted = decrypt(encrypted,key)
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')