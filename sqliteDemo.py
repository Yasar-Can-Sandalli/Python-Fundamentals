import sqlite3

def selectOperasyonları():

    connection  = sqlite3.connect("chinook.db")
    # cursor = connection.execute("Select FirstName,LastName from Customers where  city='Prague' or  country = 'Canada' order by firstName,LastName desc")
    # for row in cursor:
    #     print("Fisrst Name : " + row[0])
    #     print("Last Name : " + row[1])
    #     print("--------------")


    # cursor = connection.execute("Select City,Count(*) from Customers group by City having count(*) > 1 order by count(*)  desc")
    # #! Order by her zaman sona yazılır ___> önce gruplıyıcak ki sonra sıralasın 
    # for row in cursor:
    #     print("City : " + row[0])
    #     print("Count : " + str(row[1]))


    cursor = connection.execute("Select FirstName,LastName from Customers where  FirstName like '%a' ")
    for row in cursor:
        print("Fisrst Name : " + row[0])
        print("Last Name : " + row[1])
        print("--------------")


    connection.close() 
#selectOperasyonları()
def ınsertCustmer():
    connection  = sqlite3.connect("chinook.db")
    connection.execute("Insert into Customers (firstName,lastName,city,email) values ('Yasar Can','Sandalli','Rize','emery67@gmail.com') ")
    connection.commit()
    connection.close()
#ınsertCustmer()

def updateCustomer():
    connection  = sqlite3.connect("chinook.db")
    connection.execute("update Customers set City = 'Kocaeli' where FirstName = 'Yasar Can' ")
    connection.commit()
    connection.close()
#updateCustomer()

def deleteCustomer():
    connection  = sqlite3.connect("chinook.db")
    connection.execute("Delete from  Customers where City ='Kocaeli' or Country='Germany'")
    connection.commit() 
    connection.close()
#deleteCustomer()

def joinOperasyonları():
    connection  = sqlite3.connect("chinook.db")
    cursor = connection.execute("SELECT albums.Title, artists.Name from albums inner join artists on albums.ArtistId = artists.ArtistId order by artists.ArtistId  asc ")
    for row in cursor:
        print(" Title : " + row[0] + " /////   Name : " + row[1])
        print("--------------")
joinOperasyonları()	

        
#? RA-L6NLRNSQYFZDMRMJ