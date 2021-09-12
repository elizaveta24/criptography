import codecs
alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
def open_files():
    text_file = ''  
    f = codecs.open('D:/proekt_crypto/test_file/text.txt', encoding='utf-8')
    for i in f:
        text_file+=i
    f.close()
    return text_file
def write_files(text):
    f = codecs.open('D:/proekt_crypto/test_file/encode_file_caesar.txt','w')
    f.write(text)
    f.close()
def encode_caesar(text,key):
    itog= ''
    for c in text:
            mesto = alpha.find(c) #Вычисляем места символов в списке
            new_mesto = mesto + key    #Сдвигаем символы на указанный в переменной new_mesto шаг
            if c in alpha:
                itog += alpha[new_mesto]  #Задаем значения в итог
            else:
                itog += c
    return itog
def decode_caesar(text,key):
    itog= ''
    for c in text:
            mesto = alpha.find(c) #Вычисляем места символов в списке
            new_mesto = mesto - key    #Сдвигаем символы на указанный в переменной new_mesto шаг
            if c in alpha:
                itog += alpha[new_mesto]  #Задаем значения в итог
            else:
                itog += c
    return itog


key = int(input('Введите ключ:'))
input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encode_caesar(input_text,key)
decrypted = decode_caesar(encrypted,key)
str_text_file = open_files().lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted_file = encode_caesar(str_text_file,key)
decrypted_file = decode_caesar(encrypted_file,key)
write = write_files(encrypted_file)
print('Цезарь')
print(f'Ваш текст:{input_text}')
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')
print(f'Зашифрованный текст файла:{encrypted_file}')
print(f'Расшифрованный текст файла:{decrypted_file}')
