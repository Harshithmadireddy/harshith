Num=int(input("enter a number: "))
#using if-else
if(Num>=-9 and Num<=9):
    print(f"{Num} is digit")
else:
    print(f"{Num} is Number")

  
#ternary
Result="digit" if (Num>=-9 and Num<=9) else " Number" 
print(f"{Num} is {Result}")

