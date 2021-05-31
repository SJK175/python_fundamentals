# code objective :
# this code should convert a name to a valid email address.

# existing email list
emaillist = ["subhajit.kundu@linde.com"
    ,"barry.wood@linde.com"
    ,"biswajit.ghosh@linde.com"
    ,"therina.foley@linde.com"
    ,"jaydeep.basu@linde.com"
    ,"kundu.subhajit@linde.com"
    ,"wood.barry@linde.com"
    ,"subhajit.kundu1@linde.com"
    ,"subhajit.kundu2@linde.com"
    ,"subhajit.kundu3@linde.com"
    ,"x.y@linde.com"
    ,"y.x@linde.com"
    ,"x.y1@linde.com"
    ,"x.y2@linde.com"
    ,"x.y3@linde.com"
    ,"x.y4@linde.com"
    ,"x.y5@linde.com"
    ,"x.y6@linde.com"
    ,"x.y7@linde.com"
    ,"x.y8@linde.com"
    ,"x.y9@linde.com"
    ,"x.y10@linde.com"]

# asking inputs from user
firstname = input("firstname :")
lastname = input("lastname :")
domain = "linde.com"

for i in range (1):
    # validating the inputs
    check_first_name = firstname.strip().isalpha()
    check_last_name = lastname.strip().isalpha()
    if not check_first_name*check_last_name :
        print("name should contain only alphabets")
        break

    # creating two suggested email-ids without adding integers.
    # firstname.lastname@domain (and) lastname.firstname@domain
    # let's call them "primary suggestions"
    email_1 = firstname.strip()+"."+lastname.strip()+"@"+domain
    email_2 = lastname.strip()+"."+firstname.strip()+"@"+domain

    # checking if "primary suggestions" are available.
    counter = 0
    for e in emaillist:
        if e == email_1:
            counter = counter+1
            for e1 in emaillist:
                if e1 == email_2:
                    counter = counter+1
        else:
            counter = counter+0

    # if "primary suggestions" are not available :
    # suggestion : firstname.lastname"N"@domain where N<=10
    if counter == 2:
        k = 1
        while k <= 10:
            email_extension = firstname.strip() + "." + lastname.strip() + str(k) + "@" + domain
            count = 0
            for em in emaillist:
                if em == email_extension:
                    count = count + 1
                else:
                    count = count + 0
            k = k + 1
            if count != 1:
                print(f"suggested: {email_extension}")
                break
        else:
            print("very common name - couldn't suggest an email-id")

    # if "primary suggestions" are available.
    elif counter == 1:
        print(f"suggested email is {email_2}")
    elif counter == 0:
        print(f"suggested email is {email_1}")
