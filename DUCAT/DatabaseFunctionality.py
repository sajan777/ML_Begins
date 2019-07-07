
from pymysql import*
con = connect(db='first',user='root',passwd='sajan',host='localhost')
cur = con.cursor()
ans = 'y'
while(ans):
    print('1.Insert the values in database')
    print('2.Read the value from database')
    print('3.Update the value in database')
    print('4.delete the values in database')
    print('5.Exit')
    i = int(input('Enter your input: '))

    if i==1:
        emp_no = int(input('Enter emp_no'))
        emp_name = input('Enter emp_name')
        salary = int(input('Enter salary'))
        query = "INSERT INTO emp(emp_no,emp_name,salary) VALUES(emp_no,emp_name,salary)"
        cur.execute(query)
        con.commit()
        con.close()
    elif i==2:
        query = "Select * from emp"
        cur.execute(query)
        rus = cur.fetchall()
        print(rus)
        con.close()

    elif i==3:
        eid = int(input('Enter Eid'))
        # new_eid = int(input(''))
        ename = input('Enter new name: ')
        query = "UPDATE emp set emp_name = '%s' where emp_no = '%d'"%(ename,eid)
        i = cur.execute(query)
        if i>=1:
            con.commit()
            print('Record Updated')
        con.close()
    elif i==4:
        eid = int(input('Enter eid whose record u want to delete'))
        query = "DELETE FROM emp WHERE emp_no = '%d'"%(eid)
        i = cur.execute(query)
        if i>=1:
            con.commit()
            print('Record deleted')
        con.close()
    elif i==5:
        exit(0)

    ans =input('Continue y/n')

# Reads the data from database
# from pymysql import*
# con = connect(db='first',user='root',passwd='sajan',host='localhost')
# cur = con.cursor()
# query = "Select * from emp"
# cur.execute(query)
# rus = cur.fetchall()
# print(rus)
# con.close()

#Inserts the data in database
# from pymysql import*
# con = connect(db='first',user='root',passwd='sajan',host='localhost')
# cur = con.cursor()
# query = "INSERT INTO emp(emp_no,emp_name,salary) VALUES(121,'Mohan',90000)"
# cur.execute(query)
# con.commit()
# con.close()

# Update some value in database
# from pymysql import*
# con = connect(db='first',user='root',passwd='sajan',host='localhost')
# cur = con.cursor()
# eid = int(input('Enter Eid'))
# # new_eid = int(input(''))
# ename = input('Enter new name: ')
# query = "UPDATE emp set emp_name = '%s' where emp_no = '%d'"%(ename,eid)
# i = cur.execute(query)
# if i>=1:
#     con.commit()
#     print('Record Updated')
# con.close()

#delete from database
# from pymysql import*
# con = connect(db='first',user='root',passwd='sajan',host='127.0.0.1')
# cur = con.cursor()
# eid = int(input('Enter eid whose record u want to delete'))
# query = "DELETE FROM emp WHERE emp_no = '%d'"%(eid)
# i = cur.execute(query)
# if i>=1:
#     con.commit()
#     print('Record deleted')
# con.close()