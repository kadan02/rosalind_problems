"""
------------------------------------------------- RNA SPLICING -------------------------------------------------
https://rosalind.info/problems/splc/
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s (Note: Only one solution will exist for the dataset provided.)

------------------------------------------------- Sample Dataset -------------------------------------------------
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
------------------------------------------------- Sample Output -------------------------------------------------
MVYIADKQHVASREAYGHMFKVCA
"""

from genome_toolkit import read_fasta
from genome_toolkit import transcribe
from genome_toolkit import translate


def splice_dna(fasta_file):
    data = read_fasta(fasta_file)
    sequences = list(data.values())
    introns = sequences[1:len(sequences)]
    dna = sequences[0]

    for intron in introns:
        dna = dna.replace(intron, "")

    return translate(transcribe(dna))
