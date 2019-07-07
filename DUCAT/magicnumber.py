n = int(input('Enter the number: '))
temp = n
sum = 0
rev = 0
while(temp>0):
    temp1 = temp%10
    temp = temp//10
    sum = sum + temp1
digit = sum
while(digit>0):
    save = digit%10
    rev = rev*10+save
    digit = digit//10

mul = sum*rev
if(mul==n):
    print("Hell yeah magic")
else:
    print("No magic")