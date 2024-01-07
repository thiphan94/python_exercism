def to_rna(dna_strand):
    rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    res = ""
    for dna in dna_strand:
        res += rna[dna]
    return res
