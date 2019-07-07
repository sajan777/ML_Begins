input_val = 'y'
dict = {}
temp_list = []
while(input_val):

    print('1. Enter Student name and subject marks: ')
    print('2. Access Student total marks')
    print('3. Remove Student from data')
    print('4. Exit')
    take_input = int(input('Enter Choice 1,2,3 : '))

    if(take_input == 1):
        name = input('Enter name ')
        for i in range(0,6):
            marks = int(input("Enter marks "))
            temp_list.append(marks)
        dict[name] = temp_list


    elif(take_input == 2):
        stu_name = input('Enter name whose marks u want: ')
        if stu_name in dict:
            total_marks = sum(temp_list)
            print(stu_name ,':', total_marks)
        else:
            print('Record doesnt exist')


    elif(take_input == 3):
        stu_name1 = input('Whose record u want to delete')
        if stu_name1 in dict:
            dict.pop(stu_name1)
        else:
            print('Reord doesnt exist')

    elif(take_input>4):
        print('you entered wrong input')
        break

    elif(take_input == 4):
        exit(0)


    input_val = input('want to Continue y/n ')
