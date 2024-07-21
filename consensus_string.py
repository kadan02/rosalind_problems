"""
https://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return any one of them.)

------ Sample Dataset ------
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

------ Sample Output ------
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

"""
from genome_toolkit import read_fasta


def find_consensus_string(fasta_file):  # TODO: Code works, but it's a mess (the prints especially)
    data = read_fasta(fasta_file)
    sequences = list(data.values())

    n = max(len(dna) for dna in sequences)
    profile_matrix = {
        "A": [0]*n,
        "C": [0]*n,
        "G": [0] * n,
        "T": [0] * n,
    }

    for dna in sequences:
        for position, nucleotide in enumerate(dna):
            profile_matrix[nucleotide][position] += 1

    result = []

    for position in range(n):
        max_count = 0
        max_nucleotide = None
        for nucleotide in ["A", "C", "G", "T"]:
            count = profile_matrix[nucleotide][position]
            if count > max_count:
                max_count = count
                max_nucleotide = nucleotide
        result.append(max_nucleotide)

    consensus = "".join(result)
    print(consensus)
    print("A:", end=" ")
    for i in profile_matrix["A"]:
        print(i, end=" ")
    print("\n")
    print("C:", end=" ")
    for i in profile_matrix["C"]:
        print(i, end=" ")
    print("\n")
    print("G:", end=" ")
    for i in profile_matrix["G"]:
        print(i, end=" ")
    print("\n")
    print("T: ", end=" ")
    for i in profile_matrix["T"]:
        print(i, end=" ")
    print("\n")
    return consensus


find_consensus_string("gc_content.txt")