"""
------------------------------------------ Transitions and Transversions ----------------------------------------
https://rosalind.info/problems/tran/

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2)

------------------------------------------  Sample Dataset ------------------------------------------
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT

------------------------------------------  Sample Output ------------------------------------------
1.21428571429
"""

from genome_toolkit import read_fasta


def transition_transversion_ratio(fasta_file):
    data = read_fasta(fasta_file)
    sequences = list(data.values())

    transitions = 0
    transversions = 0
    purines = ["A", "G"]
    pyrimidines = ["C", "T"]

    for base1, base2 in zip(sequences[0], sequences[1]):
        if base1 != base2:
            if (base1 in purines and base2 in purines) or (base1 in pyrimidines and base2 in pyrimidines):
                transitions += 1
            else:
                transversions += 1

    return transitions/transversions


print(transition_transversion_ratio("rosalind_tran.txt"))
