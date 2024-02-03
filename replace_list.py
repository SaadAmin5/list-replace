#replace email id with @gmail.com

list1 = ["john@hotmail.com","sarah@gmail.com","mani.1231997.edu.uk","george@yahoo.com"]

for i in list1:
    new_email=i.replace('hotmail.com', 'gmail.com').replace('yahoo.com', 'gmail.com').replace('.edu.uk', '@gmail.com')
    print(new_email)