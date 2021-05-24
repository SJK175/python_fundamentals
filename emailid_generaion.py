#this program should convert a name to a valid email address.
firstname = input("firstname :")
lastname = input("lastname :")
domain = "linde.com"

emaillist = ["subhajit.kundu@linde.com"
    ,"barry.wood@linde.com"
    ,"biswajit.ghosh@linde.com"
    ,"therina.foley@linde.com"
    ,"jaydeep.basu@linde.com"
    ,"kundu.subhajit@linde.com"]

email_1 = firstname.strip()+"."+lastname.strip()+"@"+domain
email_2 = lastname.strip()+"."+firstname.strip()+"@"+domain

counter = 0
for e in emaillist:
    if e == email_1:
        counter = counter+1
        for e1 in emaillist:
            if e1 == email_2:
                counter = counter+1
    else:
        counter = counter+0

if counter == 2:
    print("can't suggest any email-id")
elif counter == 1:
    print(f"suggested email is {email_2}")
elif counter == 0:
    print(f"suggested email is {email_1}")
