num=int(input("Enter Number to Check Armstrong Number: "))
sum=0
p=len(str(num))
n=num
while(num>0):
    sum+=(num%10)**p
    num//=10
if(n==sum):
    print("Number is Armstrong.")
else:
    print("Number is not Armstrong.")