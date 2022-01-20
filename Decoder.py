def key_indexer(key_index, key_length):
    return 0 if key_index == (key_length - 1) else key_index + 1


def main():
    text = input("Encrypted text: ").lower()
    key = input("\nEncryption key: ").lower()
    decoded_text, key_index = ("", 0)

    if len(text) == 0:
        print("\nEmpty text!")
        return

    for i in range(len(text)):
        if ord(text[i]) == 32:
            decoded_text += chr(32)
            continue

        decoded_letter_index = (ord(text[i]) - 96) - (ord(key[key_index]) - 96)
        decoded_letter_index = 26 if decoded_letter_index == 0 else decoded_letter_index + 26

        decoded_text += chr(decoded_letter_index + 96)
        key_index = key_indexer(key_index, len(key))

    print(f"\nDecrypted text: {decoded_text}")


if __name__ == '__main__':
    main()