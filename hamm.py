"""
https://rosalind.info/problems/hamm/

Given: Two DNA strings s and tof e qual length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
"""


def hamming_distance(seq1, seq2):
    diff = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            diff += 1
    return diff
