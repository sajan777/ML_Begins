from pymysql import*

con = connect(db='ducat_database',user='root',passwd='sajan',host='localhost')
cur = con.cursor()
empno = (int(input('Empno')))
ename = input('Name')
salary = (int)(input('Salary'))
cur.execute("insert into emp values(%d,%s,%d)"%(empno,ename,salary))
con.commit()
print('Record Saved')
con.close()