import string


def is_pangram(sentence):
    alphabet = sentence.lower()
    for elt in string.ascii_lowercase:
        if elt not in alphabet:
            return False
    return True
