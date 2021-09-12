alphabet: str = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def decode(text: str, a: int = 1, b: int = 1, c: int = 1) -> str:
    decode: str = ""
    for position, symbol in enumerate(text, start=1):
        k: int = (a * position**2) + (b * position) + c
        index: int = (alphabet.index(symbol,1) - k) % len(alphabet)
        decode += alphabet[index] if symbol.isupper() else alphabet[index].lower()
    return decode
 
 
def encode(text: str, a: int = 1, b: int = 1, c: int = 1) -> str:
    encode: str = ""
    for position, symbol in enumerate(text,start=1):
        k: int = (a * position**2) + (b * position) + c
        index: int = (alphabet.index(symbol) + k) % len(alphabet)
        encode += alphabet[index] if symbol.isupper() else alphabet[index].lower() 
    return encode
input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encode(input_text)
decrypted = decode(encrypted)
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')