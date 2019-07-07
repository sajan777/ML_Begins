n = int(input('Enter the number to reverse it: '))
rev =0
while(n>0):
    save = n%10
    rev = rev*10+save
    n = n//10
print('reverse of the number: ',rev)