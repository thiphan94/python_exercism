plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"


def encode(plain_text):
    word = ""
    res = ""

    for char in plain_text.lower():
        if char.isalnum():
            if char.isalpha():
                word += cipher[plain.index(char)]
            else:
                word += char

            if len(word) == 5:
                res += word + " "
                word = ""

    if word:
        res += word

    return res.strip()


def decode(ciphered_text):
    word = ""
    res = ""

    for char in ciphered_text.lower():
        if char.isalnum():
            if char.isalpha():
                word += cipher[plain.index(char)]
            else:
                word += char

    if word:
        res += word

    return res.strip()
