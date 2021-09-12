import codecs
def open_files(): 
    text_file = ''  
    f = codecs.open('D:/proekt_crypto/test_file/text.txt', encoding='utf-8')
    for i in f:
        text_file+=i
    f.close()
    return text_file
def write_files(text):
    f = codecs.open('D:/proekt_crypto/test_file/encode_file_polibiy.txt','w')
    f.write(text)
    f.close()

abc = {"а":"11", "б":"12", "в":"13",
"г":"14", "д":"15", "е":"16", "ж":"21",
"з":"22", "и":"23", "й":"24","к":"25",
"л":"26", "м":"31", "н":"32", "о":"33",
"п":"34", "р":"35", "с":"36", "т":"41",
"у":"42", "ф":"43", "х":"44", "ц":"45",
"ч":"46", "ш":"51", "щ":"52", "ъ":"53",
"ы":"54", "ь":"55", "э":"56", "ю":"61",
"я":"62"}



def encrypt_polibiy(text):
    crypt = ""
    for i in text:
	    if i in abc:
		    crypt += abc[i]
		    crypt += " "
    return crypt
def decrypt_polibiy(text):
    decrypt = ""
    temp = ""
    for i in text:
	    if i != " ":
		    temp += i
	    else:
		    for j in abc:
			    if abc[j] == temp:
				    decrypt += j
		    temp = ""
    return decrypt

input_text = input('Введите текст:').lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted = encrypt_polibiy(input_text)
decrypted = decrypt_polibiy(encrypted)
input_text_file= open_files().lower().replace(',','зпт').replace('.','тчк').replace(' ','')
encrypted_file = encrypt_polibiy(input_text_file)
decrypted_file = decrypt_polibiy(encrypted_file)
print('Квадрат Полибия')
print(f'Ваш текст:{input_text}')
print(f'Зашифрованный текст:{encrypted}')
print(f'Расшифрованный текст:{decrypted}')
print(f'Зашифрованный текст файла:{encrypted_file}')
print(f'Расшифрованный текст файла:{decrypted_file}')