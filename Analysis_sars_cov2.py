#LECTURE DE LA SEQUENCE
def read_fasta(file_path):
    sequence = ""
    with open(file_path, "r") as f:
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip().upper()
    return sequence

sequence = read_fasta("MT470152.1.fasta")

print("Longueur du génome :", len(sequence))

#COMPOSITION NUCLEOTIDE
def nucleotide_composition(sequence):
    total = len(sequence)
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G")
    }
    frequencies = {k: v/total for k, v in counts.items()}
    return counts, frequencies

counts, frequencies = nucleotide_composition(sequence)

print("Composition :", counts)
print("Fréquences :", frequencies)

#CALCUL DU GC GLOBAL 
def compute_gc(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    return (g + c) / len(sequence) * 100

gc_global = compute_gc(sequence)

print("GC content global :", round(gc_global, 2), "%")

#GC PAR FENETRE
import matplotlib.pyplot as plt

def sliding_gc(sequence, window_size=500):
    gc_values = []
    positions = []
    for i in range(0, len(sequence), window_size):
        window = sequence[i:i+window_size]
        if len(window) > 0:
            gc = compute_gc(window)
            gc_values.append(gc)
            positions.append(i)
    return positions, gc_values

positions, gc_values = sliding_gc(sequence, window_size=500)

plt.figure(figsize=(10,5))
plt.plot(positions, gc_values)
plt.xlabel("Position dans le génome")
plt.ylabel("GC content (%)")
plt.title("Variabilité du contenu GC - SARS-CoV-2 (France)")
plt.show()

# Séquence France
sequence = read_fasta("MT470152.1.fasta")

# Séquence Wuhan
wuhan_sequence = read_fasta("sequence.fasta")
def compare_sequences(seq1, seq2):
    min_len = min(len(seq1), len(seq2))
    differences = 0
    
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            differences += 1
    
    similarity = (1 - differences / min_len) * 100
    
    return differences, similarity

diff, sim = compare_sequences(sequence, wuhan_sequence)

print("Nombre de différences :", diff)
print("Similarité (%) :", round(sim, 4))

#LOCALISATION DES MUTATIONS 
mutations = []

for i in range(len(sequence)):
    if sequence[i] != wuhan_sequence[i]:
        mutations.append((i+1, wuhan_sequence[i], sequence[i]))

print("Positions mutées :")
for m in mutations:
    print("Position:", m[0], "Wuhan:", m[1], "France:", m[2])