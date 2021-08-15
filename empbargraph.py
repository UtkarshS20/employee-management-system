import matplotlib.pyplot as plt
import dbase as dbs
def createDepartmentgraph():
    dbs.cur.execute('select count(e.id),d.name from employee e inner join department d\
    on e.department=d.id group by d.name')
    getdata=dbs.cur.fetchall()
    xdst=[]
    ydst=[]
    for val in getdata:
        xdst.append(val[1])
        ydst.append(val[0])
    plt.bar(xdst,ydst,label='Employees',color='b')
    plt.legend()
    plt.xlabel('department')
    plt.ylabel('no. of employees')
    plt.title('employees per department')
    plt.show()
#createDepartmentgraph()
