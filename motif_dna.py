"""
https://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.

Sample Dataset: GATATATGCATATACTTATAT
Sample Output: 2 4 10
"""


def find_motif(seq, motif):
    locations = []
    motif_length = len(motif)
    seq_length = len(seq)

    for i in range(seq_length - motif_length + 1):
        if seq[i:i + motif_length] == motif:
            locations.append(i + 1)
            print(i + 1, end=' ')
    return locations



