'''MENU=["chiken biryani","chiken fry piece","Dragon chicken","Chicken majestic"]
while(1):
    print("|---------------------WELCOME TO TUPLE RESTAURANT---------------------|")
    print("|1.........................MENU OF FOOD ITEMS.........................|")
    print("|2....................TAKE ORDER FROM THE USER........................|")
    print("|3............................BILLING.................................|")
    print("|4....................Deliver the item and Bill..............,........|")
    print("|5.EXIT........................................|")
    print("|----------------------------------------------|")

    choice=int(input("enter your choice:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            guestname=input("enter guest name:")
            Guest.append(guestname)
            print(f'{guestname} is added to guest list')
        elif(choice==2):
            cancelledguest=input("enter cancelled guest name:")
            if(cancelledguest in Guest):
             Guest.remove(cancelledguest)
             print(f'{cancelledguest} is removed from guest list')
            else:
               print(f'{cancelledguest} is not in  guest list')
        elif(choice==3):
            checkguest=input("enter guest name:")   
            if(checkguest in Guest):
              print(f'{checkguest} is attending')
            else:
               print(f'{checkguest} is not attending')
        elif(choice==4):
            if(len(Guest)==0):
              print("list is empty")
            else:
              Guest.sort()
              print("final list")
              print(Guest)
        else:
           print("---ENJOY PARTY---")
           break
    else:
       print("invalid input")'''
n=int(input())
print("|---------------------WELCOME TO TUPLE RESTAURANT---------------------|")
List=['pizza','biryani','maggie','friedrice','peethagudala fry']
Tuple=('100','120','20','100','500')
i=1
while(i<=n):
    word=input("enter the word:")
    index=List.index(word)
    print(f"{word}-{Tuple[index]}")
    i+=1
