
result = 0
n= int(input('Enter your number :'))
temp = n
while(temp>0):
    temp1 = temp%10
    temp = temp// 10
    result = result+temp1**3
if(result == n):
    print('Hell yeah')
else:
    print('Nope')