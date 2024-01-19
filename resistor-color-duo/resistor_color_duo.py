def value(colors):
    code = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]

    return int("".join(str(code.index(elt)) for elt in colors[:2]))
