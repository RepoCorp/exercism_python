#dna Exercism
from string import maketrans  


def to_rna(dna):
    dna_nucleotides = "GCTA"
    rna_nucleotides = "CGAU"
    transtable = maketrans(dna_nucleotides, rna_nucleotides)
    a = 1
    return dna.translate(transtable)

