def translate(text):
    res = ""
    vowel = ["a", "e", "o", "u", "i", "xr", "yt"]
    consonants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    if any(map(text.startswith, vowel)):
        res = text + "ay"
    else:
        cluster = ""
        for elt in text:
            if elt in consonants:
                if 
                cluster += elt
                
            else:
                break
        res = text[len(cluster) : :] + text[: len(cluster)] + "ay"

    return res
