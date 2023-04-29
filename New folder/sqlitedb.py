import sqlite3
con=sqlite3.connect("test2.db")
print("secc")

# con.execute("create table stud2(id int primary key,name char(20),class int,div char(5));")
print('success')

con.execute("insert into stud2 values(001,'abin',8,'b');")
'''
con.execute("insert into stud2 values(002,'rahul',9,'c');")
con.execute("insert into stud2 values(003,'rebin',8,'a');")
con.execute("insert into stud2 values(004,'ram',10,'a');")
con.commit()
'''
k=con.execute('select * from stud2;')
for i in k:
    print(i)
#     print('id : ',i[0])
#     print('name : ',i[1])
#     print('class: ',i[2])

'''
con.execute("update stud2 set name='shabeeb' where id=001;")
s=con.execute('select * from stud2;')
for i in s:
    print('id : ',i[0])
    print('name : ',i[1])
    print('class: ',i[2])
    
#con.execute("delete from stud2  where id=001;")
d=con.execute('select * from stud2;')

print(m)
for i in m:
    print('id : ',i[0])
    print('name : ',i[1])
    print('class: ',i[2])
'''
con.close()
