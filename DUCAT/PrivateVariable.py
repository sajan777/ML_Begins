#hackerrank interview warm up challanges
#question 1
# ar = [1,1,2,3,1,3]
# new_arr = []
# arr=list(ar)
# for i in arr:
#     x = ar.count(i)
#     new_arr.append(x)
#     print(new_arr)
#     while i in ar:
#         ar.remove(i)
#     print(ar)
#     arr=ar

#question 2
# def countingValleys(n, s):
#     sea_level = 0
#     count = 0
#     for val in s:
#         if val == 'U':
#             sea_level += 1
#             print(sea_level)
#         elif val == 'D':
#             sea_level -= 1
#             print(sea_level)
#         if(sea_level==0 and val=='U'):
#             count +=1
#     return count
#
# print(countingValleys(7,'DDUUDDUDUUUD'))

#question 3
# def jumpingOnClouds(c):
#     # jump = 0
#     beg = 0
#     coun = 0
#     size = len(c)
#     while (beg < size-1):
#         if ((beg<size-2) and int(c[beg + 1]) == 0 and (int(c[beg+2])==1)):
#             beg += 1
#             coun += 1
#
#         elif((beg<size-2) and int(c[beg+2])==0):
#             beg += 2
#             coun +=1
#
#         elif ((beg<size-2) and int(c[beg + 1]) == 1 and (int(c[beg+2])== 0)):
#             beg += 2
#             coun += 1
#         elif((beg==size-2) and int(c[beg+1])==0):
#             coun+=1
#             break
#     return coun
#
#
# print(jumpingOnClouds('000100'))
#Repeated String
# def repeatedString(s, n):
#     size = len(s)
#     rep_size = n//size
#     rem = n%size
#     count=0
#     count2=0
#     for i in range(size):
#         if s[i] == 'a':
#             count+=1
#         if s[i] == 'a' and i<rem:
#             count2+=1
#     total = count*rep_size+count2
#     return total
#
#
# print(repeatedString('abc',1000000000000))

#Arrays Question 1

# def hourglassSum(arr):
#     row_size = len(arr)
#     col_size = len(arr[0])
#     new_arr=[]
#     for i in range(0,row_size):
#         for j in range(0,col_size):
#             hour_Sum = 0
#             i_temp=i
#             j_temp=j
#             while(j<j_temp+3):
#                 hour_Sum = hour_Sum + arr[i][j]
#                 j+=1
#             i+=1
#             j-=2
#             hour_Sum=hour_Sum+arr[i][j]
#             i+=1
#             j-=1
#             while(j<j_temp+3):
#                 hour_Sum = hour_Sum+arr[i][j]
#                 j+=1
#             new_arr.append(hour_Sum)
#             i-=2
#             j-=2
#         i+=1
#         j-=2
#
#
#             # j=j_temp+1
#     # maxi=max(new_arr)
#
#     return hour_Sum
#
# print(hourglassSum([[1, 2, 3,6], [4, 5, 6,8], [7, 8, 9,2], [10, 11, 12,1]]))
#HourGlass Sum
# def hourglassSum(arr):
#     max = -63
#
#     for i in range(1, 5):
#         for j in range(1, 5):
#             sum = 0
#             sum = sum + arr[i][j]  # for the element itself
#             sum = sum + arr[i - 1][j - 1]  # aboveleftelement
#             sum = sum + arr[i - 1][j]  # elementjustaboveit
#             sum = sum + arr[i - 1][j + 1]  # aboverightelement
#             sum = sum + arr[i + 1][j - 1]  # belowLeftElement
#             sum = sum + arr[i + 1][j]  # elementjustbelowit
#             sum = sum + arr[i + 1][j + 1]  # elementrightbelowit
#             if sum > max:
#                 max = sum
#     return max
#
# print(hourglassSum([[1,1,1,0,0,0],
#                    [0,1,0,0,0,0],
#                    [1,1,1,0,0,0],
#                    [0,0,2,4,4,0],
#                    [0,0,0,2,0,0],
#                    [0,0,1,2,4,0]]))

#Arrays Question 2
# def rotLeft(a, d):
#     new_Arr = []
#     size = len(a)
#     for save in range(d):
#         first_val = a[0]
#         for x in range(0,size):
#             if x!=size-1:
#                 a[x] = a[x+1]
#                 new_Arr = a
#             elif x==size-1:
#                 new_Arr.pop()
#                 new_Arr.append(first_val)
#     return new_Arr
#
# print(rotLeft([1,2,3,4,5],4))

#Array Question 3
# def minimumBribes(q):
#     pass
#
# print(minimumBribes([1,2,3,4,5]))
# Array Question4
# def minimumSwaps(arr):
#     minswap = 0
#     for i in range(len(arr)):
#
#         if(minswap>0 and j>i):
#             i=0
#         # for j in range(i+1,len(arr)):
#         j = i+1
#         if(arr[i]>arr[j]):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             minswap +=1
#             i =0
#         else:
#             pass
#
#     return minswap
# print(minimumSwaps([1,3,5,2,4,6,7]))
#Sorting question 1
# def countSwaps(a):
#     count=0
#     temp=0
#     for i in range(0,len(a)):
#         for x in range(0,len(a)-1):
#             if(a[x]>a[x+1]):
#                 temp = a[x]
#                 a[x] = a[x+1]
#                 a[x+1] = temp
#                 count+=1
#     print('array is soterd in',count,'swaps')
#     print('First Element is',a[0])
#     print('Last Element is',a[len(a)-1])

# countSwaps([4,2,3,1])

#String manipulation question1
def makeAnagram(a, b):
    count =0
    for i in range(0,len(a)):
        t = a[i]
        if a[i] not in b:
            count +=1
        else:
            pass
    for x in range(0,len(b)):
        t1 = b[x]
        if b[x] not in a:
            count+=1
        else:
            pass
    return count

print(makeAnagram('bugexikjevtubidpulaelsbcqlupwetzyzdvjphn','lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk'))