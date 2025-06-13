''''
Num=int(input())
print(f"natural numbers from 1 to num:")
for i in range(1,Num+1):
    print(i*i*i)
'''
Num=int(input("Enter the value of Num :"))
Temp=Num
DigitCount=0
while(Num!=0):
    Num=Num//10
    DigitCount+=1#DigitCount=DigitCount+1
print(f"{Temp} has {DigitCount}digits")