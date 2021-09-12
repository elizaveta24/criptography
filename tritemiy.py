import codecs
def open_files(): 
    text_file = ''  
    f = codecs.open('D:/proekt_crypto/test_file/text.txt', encoding='utf-8')
    for i in f:
        text_file+=i
    f.close()
    return text_file
def write_files(text):
    f = codecs.open('D:/proekt_crypto/test_file/encode_file_tritemiy.txt','w')
    f.write(text)
    f.close()
alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def decode(text: str, a: int = 1, b: int = 1, c: int = 1) -> str:
    decode: str = ""
    for position, symbol in enumerate(text):
        k: int = (a * position**2) + (b * position) + c
        index: int = (alphabet.index(symbol) - k) % len(alphabet)
        decode += alphabet[index] if symbol.isupper() else alphabet[index].lower()
    return decode
 
 
def encode(text: str, a: int = 1, b: int = 1, c: int = 1) -> str:
    encode: str = ""
    for position, symbol in enumerate(text):
        k: int = (a * position**2) + (b * position) + c
        index: int = (alphabet.index(symbol) + k) % len(alphabet)
        encode += alphabet[index] if symbol.isupper() else alphabet[index].lower() 
    return encode
input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encode(input_text)
decrypted = decode(encrypted)
text_file = open_files()
str_text_file = open_files().lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted_file = encode(str_text_file)
decrypted_file = decode(encrypted_file)
write = write_files(encrypted_file)
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')
print(f'Зашифрованный текст файла:{encrypted_file}')
print(f'Расшифрованный текст файла:{decrypted_file}')