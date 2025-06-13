'''set={1,2,4,5,3,6,7}
print(type(set))
set.add(101)
set.update([103,106])
set.remove(1)
set.clear()
set.discard(9)
print(set)
'''

set1={1,2,3,6,4}
set2={5,6,7,8}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set1^set2)

'''dna=(input("enter the dna strian: "))
rna=dna.replace('T','U')
print('converted dna strain: ',rna)'''

str=input("enter the sequence:")
str=str.upper()
total_weight = 0.0
amino_acid_weights = {
    'A': 89.1,   # Alanine
    'C': 121.2,  # Cysteine
    'D': 133.1,  # Aspartic acid
    'E': 147.1,  # Glutamic acid
    'F': 165.2,  # Phenylalanine
    'G': 75.1,   # Glycine
    'H': 155.2,  # Histidine
    'I': 131.2,  # Isoleucine
    'K': 146.2,  # Lysine
    'L': 131.2,  # Leucine
    'M': 149.2,  # Methionine
    'N': 132.1,  # Asparagine
    'P': 115.1,  # Proline
    'Q': 146.2,  # Glutamine
    'R': 174.2,  # Arginine
    'S': 105.1,  # Serine
    'T': 119.1,  # Threonine
    'V': 117.1,  # Valine
    'W': 204.2,  # Tryptophan
    'Y': 181.2   # Tyrosine
}
for amino_acid in str:
    if amino_acid in amino_acid_weights :
        total_weight += amino_acid_weights[amino_acid]
    else:
        print(f"Warning: Molecular weight for {amino_acid} not found in dictionary.")

print(f"Total weight = {total_weight:.2f}")



