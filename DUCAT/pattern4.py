for i in range(1,6,1):
    for x in range(6,i-1,-1):
        print(' ',end=' ')

    for k in range(1,i+1,1):
        print('*',end=' ')

    for p in range(1,i,1):
        print('*',end=' ')

    print('\n')