import sqlite3

#connect to database
# conn = sqlite3.connect('customer.db')

# #create a cursor
# c = conn.cursor()


def show_all():
    #connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    #query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    #commit oue command
    conn.commit()
    #close our connection
    conn.close()
    
    
#Add a new record to the table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first, last, email))
    #commit oue command
    conn.commit()
    #close our connection
    conn.close()

#add many records to table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)",(list))
    #commit oue command
    conn.commit()
    #close our connection
    conn.close()
    
    

#delete record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    #commit our command and close connection
    conn.commit()
    conn.close()
    
    
#lookup with where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    
    for item in items:
        print(item)
        
        
    #commit our command and close connection
    conn.commit()
    conn.close()
    


#delete the database
# c.execute("DELETE from customers WHERE rowid = 1")


# update records
# c.execute("""UPDATE customers SET first_name = 'Bob'
#              WHERE last_name = 'Elder'
#         """)
# decndeding order
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# asending oder
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")
# last_name decndeding order
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid lasr_name DESC")

# last_name start
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%'")
# the database - AND/OR
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%'OR rowid = 2")
# limit data or results
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 1")


############Drop table
# c.execute("DROP TABLE customers")
# conn.commit()




#query the database
# c.execute("SELECT rowid, * FROM customers")

# print(c.fetchone())
# c.fetchmany(3)

# print(c.fetchall())

# items = c.fetchall()
# for item in items:
    # print(item)


# print("NAME " + "\t\t\tEMAIL")
# print("----------" + "\t\t----------")

# for item in items:
#     print(item[0] + " " + item[1] + "\t\t" + item[2])









# many_customers = [
#                     ('wes', 'Brown', 'wes@brown.com'),
#                     ('steph', 'kuewa', 'steph@gmail.com'),
#                     ('dan','pas','dan@pas.com'),
    
#                 ]






# c.execute("INSERT INTO customers VALUES (?,?,?)", many_customers)


# print("Commads excuet ss")
#create a table 
# c.execute("""CREATE TABLE customers(
#         first_name text,
#         last_name text,
#         email text
#     )""")
# # Datatypes:
# #NULL
# #INTEGER
# #REAL
# #TEXT
# #BLOB


#commit our command
# conn.commit()

#close our connection
# conn.close()








