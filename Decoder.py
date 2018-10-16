def key_indexer(_key_index, key_length):

    if _key_index == (key_length - 1):
        _key_index = 0
    else:
        _key_index += 1

    return _key_index


text = raw_input("Enter the encrypted text:\n")
key = raw_input("Enter the key of encryption:\n")
dec_text = ""
key_index = 0


if len(text) == 0:
    print "\nEmpty text!"
    quit()

text.lower()
key.lower()

for i in range(len(text)):
    if ord(text[i]) == 32:
        dec_text += chr(32)
        continue
    dec_letter_index = (ord(text[i]) - 96) - (ord(key[key_index]) - 96)

    if dec_letter_index < 0:
        dec_letter_index += 26
    elif dec_letter_index == 0:
        dec_letter_index = 26

    dec_text += chr(dec_letter_index + 96)
    key_index = key_indexer(key_index, len(key))

print "\nDecrypted text:\n" + dec_text
