#this program should convert a name to a valid email address.

firstname = input("firstname :")
lastname = input("lastname :")
domain = "linde.com"
emaillist = ["subhajit.kundu@linde.com"
    ,"barry.wood@linde.com"
    ,"biswajit.ghosh@linde.com"
    ,"therina.foley@linde.com"
    ,"jaydeep.basu@linde.com"]

email = firstname+"."+lastname+"@"+domain

counter = 0
for e in emaillist:
    if e == email:
        counter = counter+1
    else:
        counter = counter+0

#print(counter)
if counter == 0:
    print(f"suggested email address is : {email}")
else:
    print("this email-id already exists")
