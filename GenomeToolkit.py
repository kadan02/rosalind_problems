# Olyan függvények, amelyeket gyakran használok más, komplexebb feladatok megoldásához
#
# Eddig tartalmazza:
# - FASTA fájl beolvasás
# - transzkripció
# - transzláció

codon_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
             "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
             "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
             "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
             "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
             "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
             "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
             "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
             "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
             "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
             "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
             "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
             "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
             "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
             "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
             "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


def read_fasta(fasta_file):
    data = {}
    current_id = None

    with open(fasta_file, "r") as s:
        for line in s:
            line = line.strip()
            if line.startswith(">"):
                current_id = line
                data[current_id] = ""
            else:
                data[current_id] += line

    return data


def transcribe(dna):
    return dna.replace("T", "U")


def translate(rna):
    protein_seq = ""
    start = rna.find("AUG")  # stores the position of the first AUG triplet
    while start + 2 < len(rna):
        kodon = rna[start:start+3]
        if kodon in {"UAG", "UAA", "UGA"}:
            break
        protein_seq += codon_map[kodon]
        start += 3
    return protein_seq
