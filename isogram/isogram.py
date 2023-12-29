def is_isogram(string):
    visited = []
    for elt in string:
        if elt.lower() in visited and elt.isalpha():
            return False
        visited.append(elt.lower())
    return True
