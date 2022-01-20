def key_indexer(key_index, key_length):
    return 0 if key_index == (key_length - 1) else key_index + 1


def main():
    text = input("Enter text:").lower()
    key = input("\nEnter the key of encryption:").lower()
    encoded_text, key_index = ("", 0)

    if len(text) == 0:
        print("\nEmpty text!")
        return

    for i in range(len(text)):
        if ord(text[i]) == 32:
            encoded_text += chr(32)
            continue

        encoded_letter_index = ((ord(text[i]) - 96) +
                                (ord(key[key_index]) - 96)) % 26

        encoded_letter_index = 26 if encoded_letter_index == 0 else encoded_letter_index + 26

        encoded_text += chr(encoded_letter_index + 96)
        key_index = key_indexer(key_index, len(key))

    print(f"\nEncrypted text: {encoded_text}")


if __name__ == '__main__':
    main()