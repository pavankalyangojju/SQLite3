import database


#add a record to the database
# database.add_one("pBar", "smith", "kaada@gmail.com")
# database.add_one("pBar", "smith", "kaada@gmail.com")
# database.add_one("pBar", "smith", "kaada@gmail.com")



#delete database
# database.delete_one('6')


#loikup email address record
database.email_lookup("jona@codemy.com")


#add many records
# stuff = [
#     ('brenda', 'smitherton', 'brenda@smitherton.com'),
#     ('bre', 'smerton', 'bra@smitherton.com')
#     ]
# database.add_many(stuff)

#show all the records
# database.show_all()