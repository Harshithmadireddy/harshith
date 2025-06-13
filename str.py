'''a=10
b='10'
print(a is b)'''
'''str="python"
print(f"length of {str} is {len(str)}")
#without index
for i in str:
    print(i,end=" ")
print()
#with index
for i in range(len(str)):
    print(str[i],end=" ")'''
#    012345678910
'''str="Python Program"
print(str[1:6])
print(str[0:1])
print(str[7:11])
print(str[10:])
print(str[7:10])
print(str[2:6])
print(str[::-1])
print(str[-9::-1])
print(str[-1:-8:-1])
print(str[-4:-8:-1])
print(str[-7:-12:-1])
print(str[-1:-5:-1])
print(str[-1:-4:-1])'''

'''Sentence="we are learning python"
List=Sentence.split()
print(List)'''

'''str=input("enter a string : ")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.startswith('P'))
print(str.count('P'))
str=str.lower()
print(str.replace('p','j'))
'''
'''Size=int(input("Enter the length of list :"))
Char_list=[]
for i in range(Size):
    ch=input("Enter the characters:")
    Char_list.append(ch)
print(Char_list)    
Str="-".join(Char_list)
print(Str)
'''
'''mail_id=input("enter mail_id: ")
list=mail_id.split('@')
print(f"user name: {list[0]}")
org=list[1]
list=org.split('.')
print(f"Org Name: {list[0]}")'''

'''str="python programs"
print(str.capitalize())
print(str.title())
print(str.casefold())
print(str.startswith('p'))
print(str.find('o'))
print("*".center(15,"*"))
print("*".center(13,"*"))
print("*".center(12,"*"))
print("*".center(11,"*"))
print("*".center(10,"*"))'''

'''str=input(" enter str")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
special_char=0
for ch in str:
    if ch.isupper():
        Uppercase_Alpha+=1
    elif ch.islower():
        Lowercase_Alpha+=1
    elif ch.isdigit():
        Numeric+=1
    else:
        special_char+=1
print(f"{Uppercase_Alpha}")
print(f"{Lowercase_Alpha}")
print(f"{Numeric}")
print(f"{special_char}")
'''
'''str=input("Enter the string :")
U_Vowels,L_Vowels,U_consonants,L_Consonants=0,0,0,0
for ch in str:
    if(ch.isalpha() and ch.isupper()):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Lower Case Vowel count {L_Vowels}")
print(f"Upper Case Vowel count {U_Vowels}")
print(f"Lower Case consonants count {L_Consonants}")
print(f"Upper Case consonants count {U_consonants}")
'''
'''for i in range(1,27):
    print(chr(i+64),"----->",i+64)
print("-------------------")
for i in range(1,27):
    print(chr(i+96),"----->",i+96)
'''

str=input("Enter a string: ")
