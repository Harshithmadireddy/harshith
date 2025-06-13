'''Tuple=10,20,30,40,50,60,70,80,90,100
print(Tuple)
print(type(Tuple))
#Tuple unpacking
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10=Tuple
print(n1,type(n1))
print(n2,type(n2))'''

'''Tuple=(('a','b','c'),('A','B','C'),(1,2,3),(-1,-2,-3))
print(Tuple)
for i in Tuple:
    print(i,type(Tuple))'''

'''Tuple=(10,25,5,6,17,30,37)
print(Tuple)
print("maximum number: ",max(Tuple))
print("minimum number: ",min(Tuple))
print("summation: ",sum(Tuple))
print("sorted Tuple: ",sorted(Tuple))
print ("reversed tuple: ",Tuple[::-1])'''

n=int(input("enter the no.of words like to find: "))
List=['marker','jockey','ice','RCB']
Tuple=('Pen','underwere','cream','Lolipop')
i=1
while(i<=n):
    word=input("enter the word:")
    index=List.index(word)
    print(f"{word}-{Tuple[index]}")
    i+=1
