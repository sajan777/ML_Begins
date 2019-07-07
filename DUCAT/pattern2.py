n = int(input('Enter any input :'))
for i in range(1,n+1,1):
    for k in range(1,n+1,1):
        if i==1 or i==n or k==1 or k==n or i==k or i+k == n+1:
            print('*',end='')

        else:
            print(' ',end='')
    print()

