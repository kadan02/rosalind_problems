# https://rosalind.info/problems/prob/

# Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

# Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability
# that a random string constructed with the GC-content found in A[k] will match s exactly.

import math


def gc_prob(s, a):  # s: dna string; a: array of gc_contents
    b = []  # the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.

    for gc in a:
        prob_gc = gc / 2
        prob_at = (1 - gc) / 2
        match_prob = 0

        for nt in s:
            if nt in "GC":
                match_prob += math.log10(prob_gc)
            if nt in "AT":
                match_prob += math.log10(prob_at)

        b.append(match_prob)
    return b


with open("rosalind_prob.txt") as f:
    s = f.readline().strip()
    a = [float(i) for i in f.readline().strip().split()]

for i in gc_prob(s, a):
    print(i, end=" ")

