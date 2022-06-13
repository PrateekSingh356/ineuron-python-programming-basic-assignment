#6. Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("enter the number: "))
sum=0
if n<=0:
    print("wrong input!")
else:
    for i in range(1,n+1):
        sum=sum+i
print("sum ",sum)