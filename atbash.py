import codecs
def open_files(): 
    text_file = ''  
    f = codecs.open('D:/proekt_crypto/test_file/text.txt', encoding='utf-8')
    for i in f:
        text_file+=i
    f.close()
    return text_file
def write_files(text):
    f = codecs.open('D:/proekt_crypto/test_file/encode_file.txt','w')
    f.write(text)
    f.close()
  
def encode_atbash(text):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    return text.translate(str.maketrans(#translate()Метод возвращает строку , где некоторые заданные символы заменяются на символы , описанные в словаре, или в таблице отображения.
             #Используйте этот maketrans()метод для создания таблицы сопоставления
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))
    
def decode_atbash(text):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    return text.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))

input_text = input('Введите свой текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encode_atbash(input_text )
decrypted = decode_atbash(encrypted)
text_file = open_files()
str_text_file = open_files().lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted_file = encode_atbash(str_text_file)
decrypted_file = decode_atbash(encrypted_file)
write = write_files(encrypted_file)
print('Атбаш')
print(f'Ваш текст:{input_text}')
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')
print(f'Текст файла:{text_file}')
print(f'Зашифрованный текст файла:{encrypted_file}')
print(f'Расшифрованный текст файла:{decrypted_file}')
