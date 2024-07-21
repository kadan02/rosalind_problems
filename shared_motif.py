"""
https://rosalind.info/problems/lcsm/

---------------------------------------------- Finding a Shared Motif ----------------------------------------------

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

------------------------------------------------- Sample Dataset -------------------------------------------------
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

------------------------------------------------- Sample Output -------------------------------------------------
AC
"""
from genome_toolkit import read_fasta


def find_longest_common_motif(fasta_file):
    data = read_fasta(fasta_file)
    sequences = list(data.values())

    sequences.sort(key=len)
    shortest_seq = sequences[0]
    n = len(shortest_seq)
    print("Shortest sequence: " + shortest_seq + " \nLength: " + str(n))

    longest_common_string = ""

    def is_common_substring(sub):
        return all(sub in seq for seq in sequences)

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            current_string = shortest_seq[i:i + length]
            if is_common_substring(current_string) and len(current_string) > len(longest_common_string):
                longest_common_string = current_string
                print("Found new longest common string: " + current_string)

    return longest_common_string


print(find_longest_common_motif("rosalind_lcsm.txt"))
