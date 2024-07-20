"""
https://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
"""

from GenomeToolkit import read_fasta


def gc_content(dataset_file):
    seq_dict = read_fasta(dataset_file)
    ids = list(seq_dict.keys())
    sequences = list(seq_dict.values())
    
    gc_counter_list = []

    for i in sequences:
        gc_counter = 0
        for j in range(len(i)):
            if i[j] == "C" or i[j] == "G":
                gc_counter += 1
        gc_counter_list.append(gc_counter / len(i) * 100)

    max_index = gc_counter_list.index(max(gc_counter_list))
    return str(ids[max_index]) + "\n" + str(gc_counter_list[max_index])


print(gc_content("gc_content.txt"))
