#35323
'''n=input("Enter the DNA Sample: ")
dna={'A':n.count('A'),'T':n.count('T'),'G':n.count('G'),'C':n.count('C')}
print(dna)
'''
'''n=int(input("enter the no of samples: "))
list=[]
list1=[]
for i in range(n):
    temp=float(input("enter the values: "))
    list.append(temp)
for i in list:
    if i<5:
        list1.append("underexpressed")
    elif i>5 and i<=15:
        list1.append("normal")
    else:
        list1.append("overexpressed")
print("label list",list1)
'''
sequence = input("Enter the DNA sequence: ")

gc_count = 0

for i in sequence:
    if i == 'G' or i == 'C':
        gc_count += 1

gc_percent = (gc_count / len(sequence)) * 100

print("GC Content: ", gc_percent, "%")

if gc_percent > 60:
    print("Classification: High GC")
elif gc_percent >= 40:
    print("Classification: Moderate GC")
else:
    print("Classification: Low GC")
