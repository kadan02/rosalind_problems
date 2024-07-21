# https://rosalind.info/problems/sseq/

# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s.

from genome_toolkit import read_fasta


def find_spliced_motif(seq, motif):
    indices = []
    i = 0
    for nt in motif:
        current_i = seq.find(nt, i)
        indices.append(current_i + 1)
        i = current_i + 1
    return indices


data = read_fasta("rosalind_sseq.txt")
seq = list(data.values())

for element in find_spliced_motif(seq[0], seq[1]):
    print(element, end=" ")
