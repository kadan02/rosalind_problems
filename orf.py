"""
https://rosalind.info/problems/orf/

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE

"""

from genome_toolkit import transcribe
from genome_toolkit import codon_map


def translate_orf(rna):  # translates all possible open reading frames of a single DNA strand
    proteins = []
    for frame in range(3):
        for i in range(frame, len(rna) - 2, 3):
            if rna[i:i+3] == "AUG":
                protein = ""
                for j in range(i, len(rna) - 2, 3):
                    codon = rna[j:j+3]
                    if codon in {"UAG", "UAA", "UGA"}:
                        proteins.append(protein)
                        break
                    protein += codon_map.get(codon, "")
    return proteins


def reverse_complement(seq):  # return the complement sequence of a DNA sequence
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(seq))


def orf(s):  # returns the set of all possible reading frames of a DNA sequence AND its complement sequence
    orfs = set()
    strands = [s, reverse_complement(s)]

    for strand in strands:
        rna = transcribe(strand)
        proteins = translate_orf(rna)
        orfs.update(proteins)

    return orfs


# Input needs to be DNA
print(orf("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"))
