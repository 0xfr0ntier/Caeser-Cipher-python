def key_indexer(_key_index, key_length):

    if _key_index == (key_length - 1):
        _key_index = 0
    else:
        _key_index += 1

    return _key_index


text = raw_input("Enter text:\n")
key = raw_input("Enter the key of encryption:\n")
inc_text = ""
key_index = 0


if len(text) == 0:
    print "\nEmpty text!"
    quit()

text.lower()
key.lower()

for i in range(len(text)):
    if ord(text[i]) == 32:
        inc_text += chr(32)
        continue
    inc_letter_index = ((ord(text[i]) - 96) + (ord(key[key_index]) - 96)) % 26

    if inc_letter_index == 0:
        inc_letter_index = 26
    elif inc_letter_index < 0:
        inc_letter_index += 26

    inc_text += chr(inc_letter_index + 96)
    key_index = key_indexer(key_index, len(key))

print "\nEncrypted text:\n" + inc_text
