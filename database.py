__author__ = 'mehdi'

import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=Memarnejad; DATABASE=Store Management System DB')
cursor = cnxn.cursor()

#Insert:
def insertIntoEmployee(k):
    try:
        cursor.execute("INSERT INTO employee(fname,lname,fathername,shenasname,nationality,religous,mobile,phone,birthplace,email) VALUES(?,?,?,?,?,?,?,?,?,?)",k)
    except Exception,e:
        '''a= 'DB exception: %s' % e'''
        return 'UnSuccessfull'
    else:
        return 'Successfull'
    finally:
        cnxn.commit()

def insertIntoKala(k):
    try:
        cursor.execute("INSERT INTO Kala(code,name,category,factory,produce,expire,number,shelf,price) VALUES(?,?,?,?,?,?,?,?,?)",k)
    except Exception,e:
        return 'UnSuccessfull'
    else:
        return 'Successfull'
    finally:
        cnxn.commit()

def insertIntoProducer(k):
    try:
        cursor.execute("INSERT INTO Producer(code,Factoryname,category,fax,phone,phone2) VALUES(?,?,?,?,?,?)",k)
    except Exception,e:
        return 'UnSuccessfull'
    else:
        return 'Successfull'
    finally:
        cnxn.commit()

def insertIntoOrder(k):
    try:
        cursor.execute("INSERT INTO Order(code,name,number,date,status) VALUES(?,?,?,?,?)",k)
    except Exception,e:
        return 'UnSuccessfull'
    else:
        return 'Successfull'
    finally:
        cnxn.commit()




#Update:
def updateEmployee(k):
    cursor.execute("UPDATE employee SET fname=?,lname=?,fathername=?,shenasname=?,nationality=?,religous=?,mobile=?,phone=?,birthplace=?,email=? WHERE EID=(?)",(k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8],k[9],k[10],k[0]))
    cnxn.commit()
    return k

def updateKala(k):
    cursor.execute("UPDATE Kala SET code=?,name=(?),category=?,factory=?,produce=?,expire=?,number=?,shelf=?,price=? WHERE id=(?)",(k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8],k[9],k[0]))
    cnxn.commit()

def updateProducer(k):
    cursor.execute("UPDATE Producer SET code=?,Factoryname=?,category=?,fax=?,phone=?,phone2=(?) WHERE id=(?)",(k[1],k[2],k[3],k[4],k[5],k[6],k[0]))
    cnxn.commit()

def updateOrder(k):
    cursor.execute("UPDATE Order SET code=?,name=?,number=?,date=?,status=? WHERE id=(?)",(k[1],k[2],k[3],k[4],k[5],k[0]))
    cnxn.commit()




#Delete:
def deleteEmployee(k):
    cursor.execute("DELETE FROM Employee WHERE id=(?)",k[0])
    cnxn.commit()
#8:
def deleteKala(k):
    cursor.execute("DELETE FROM Kala WHERE code=(?)",k[0])
    cnxn.commit()

def deleteProducer(k):
    cursor.execute("DELETE FROM Producer WHERE id=(?)",k[0])
    cnxn.commit()

def deleteOrder(k):
    cursor.execute("DELETE FROM Order WHERE id=(?)",k[0])
    cnxn.commit()




#Search of Employee:
def searchAllEmployee():
    cursor.execute("select * from employee")
    row = cursor.fetchall()
    return row

def searchByNameEmployee(k):
    cursor.execute("select * from employee where fname=(?) ",k[0])
    row = cursor.fetchall()
    return row

def searchByLNameEmployee(k):
    cursor.execute("select * from employee where lname=(?) ",k[0])
    row = cursor.fetchall()
    return row



#Search of Kala:
def searchKala():
    cursor.execute("select * from Kala")
    row = cursor.fetchall()
    return row

def searchByCodeKala(k):
    cursor.execute("select * from Kala where code=(?)",k[0])
    row = cursor.fetchall()
    return row

def searchByNameKala(k):
    cursor.execute("select * from Kala where name=(?)",k[0])
    row = cursor.fetchall()
    return row

def searchByNumberKala():
    cursor.execute("select * from Kala where number<50")
    row = cursor.fetchall()
    return row

def searchByCategoryKala(k):
    cursor.execute("select * from Kala where Category=(?)",k[0])
    row = cursor.fetchall()
    return row


#Search of Producer:
def searchProducer():
    cursor.execute("select * from Producer")
    row = cursor.fetchall()
    return row

def searchByCodeProducer(k):
    cursor.execute("select * from Producer where code=(?)",k[0])
    row = cursor.fetchall()
    return row

def searchByNameProducer(k):
    cursor.execute("select * from Producer where Factoryname=(?)",k[0])
    row = cursor.fetchall()
    return row



#Search Order:
def searchOrder():
    cursor.execute("select * from Order")
    row = cursor.fetchall()
    return row

def searchByCodeOrder(k):
    cursor.execute("select * from Order where code=(?)",k[0])
    row = cursor.fetchall()
    return row

def searchByNameOrder(k):
    cursor.execute("select * from Order where Factoryname=(?)",k[0])
    row = cursor.fetchall()
    return row


