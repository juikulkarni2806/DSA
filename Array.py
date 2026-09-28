arr=[10,34,45,6,8,20,25,19]
max=arr[0]
min=arr[0]
for num in arr:
    if (num>max):
        max=num
    if (num<min):
        min=num
print("Maximum Num: ",max)
print("Minimum Num: ",min)

