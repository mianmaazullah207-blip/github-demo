#nested loop
row=int(input("enter the number of rows"))
for i in range(1,row+1):
    for j in range(0,i):
        print("*",end=" ")
    print( )

