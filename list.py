'''Num_List=[10,20,30,40,50,60,70,80,90]
print(Num_List)
print("accesing the list elements using for loop without indexing")
for i in Num_List:
    print(i)

print("accesing the list elements using for loop with indexing")
for i in range(len(Num_List)):
    print(Num_List[i])
print("accesing the list elements using while loop with indexing")
i=0
while(i<len(Num_List)):
    print(Num_List[i])
    i+=1'''

Color= ['White','Red','blue','Pink']
print(Color)
del Color[2]
print(Color)
del Color
print(Color)
