print("PALINDROME CHECK")   
num=int(input("enter the number"))
n1=num
reverse=0
temp=0

while(num>0):
    temp=num%10
    reverse=reverse*10+temp
    num=num//10
print(reverse)
if(reverse==n1):
    print("The given number is a palindrome number")
else:
    print("The given number is not a paindrome number")
    
    
print("LEAP YEAR CHECK")
year=int(input("enter the year"))

temp=year%10
if(temp%4==0):
    print("the year is an leap year")
else:
    print("the year is not an leap year")
    
    














