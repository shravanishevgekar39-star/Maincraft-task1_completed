print("ARMSTRONG NUMBER")
num=int(input("enter a three digit number"))
n1=num 
sum=0
temp=0
while(num>0):
    temp=num%10
    sum=sum+temp*temp*temp
    num=num//10
if(n1==sum):
    print("the given number is an armstrong number")
else:
    print("the given number is not an armstrong number")


    
    














