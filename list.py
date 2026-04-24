'''list=[[1,2,3],[['a','b','d'],'s','h','j']]
print(list[1][0][1])
print(list[0])
list.append("khan")
print(list)
list.insert(2,13)
print(list)
list2=[1,5,7]
list.extend(list2)
print(list)
n=1
while n<=8:
    print(n)
    n=n+1
n=1
sum=0
while n<=10:
    sum=sum+n
    n=n+1
print(sum)
number=(int(input("enter a number:")))
n=1
while n<=10:
    print(number,"*",n, "=",number*n)
    n=n+1
    '''
'''i=1
while i<=10:
    print(i)
    i+=1
i=100
while i>=1:
    print(i)
    i-=1'''
'''num=int(input("enter te numbe:"))
n=1
while n<=10:
    print(num, "*" ,n, "=" ,num*n )
    n+=1'''
'''num=[1,2,3,4,5]
for i in num:
    print(i)
i="mianmaaz"
for char in i:
    print(char)'''
'''list=[1,2,3,2,4,5]
x=2
idx=0
for el in list:
    if(el==x):
        print("found",idx)
    idx+=1'''
'''for i in range(5):
    print(i)
for i in range(2,8,2):
    print(i)'''
'''n=5
sum=0
for i in range(1,n):
    sum+=i
print(sum)'''
'''n=5
fac=1
for i in range(1,n+1):
    fac*=i
print(fac)'''
#membership operator
#in operator
#not in operator
'''name="mianmaaz"
subname="maaz"
if subname in name:
    print("yes")
else:
    print("no")'''
'''list=[1,4,5,6,3,2]
sublist=4
if sublist not in list:
    print("true")
else:
    print("false")'''
##ID FUNCTION
'''str="maaz"
num=id(str)
print(num)'''
#identity operators
'''x=10
y=10
if x is y:
    print("true")
else:
    print("false")'''
'''x=10
y=10
if x is not y:
    print("true")
else:
    print("false")'''
'''list=[1,2,3,4]
list.append(7)
print(list)
list.append([2,4,3])
print(list)
list.insert(2,7)
print(list)
list.extend([8,9,10])
print(list)'''
'''n=int(input("enter a number:"))
number=[]
for i in range(n):
    x=int(input())
    number.append(x)
print(number)'''
#split method
'''std="i am mian"
num=std.split()
print(num)
num=input("enter a numbers:").split()
print(num)'''
n=int(input("enter the number:"))
sum=0
i=0
while i<n:
    sum+=n
    n-=1
print(sum)





