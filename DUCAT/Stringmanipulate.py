name = input('Enter your string: ')
li = name.split()
size = len(li)
new = ''
cal_size = size//2
new = new + '' +li[size//2]
for i in range(0,size):
    if i!=cal_size:
        new = new + ' '+ li[i][0]
print(new)
