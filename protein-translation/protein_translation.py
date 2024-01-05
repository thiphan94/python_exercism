def proteins(strand):
    protein_list = [strand[i : i + 3] for i in range(0, len(strand), 3)]
    codons = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
    res = []
    for elt in protein_list:
        value = codons[elt]
        if value == "STOP":
            break
        res.append(value)
    return res
