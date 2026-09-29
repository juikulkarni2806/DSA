num=int(input("Enter Any Number: "))
n=num
sum=0
while (num>0):
    sum = sum*10 +(num%10)
    num//=10
if(n==sum):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
