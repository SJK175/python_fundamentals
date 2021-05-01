
#price of a house is $1M. If buyer has good credit score
#he needs to put down 10%.otherwise they need to
#put down 20%. print the down-payment amount.

price = 1000000
good_credit_score = False

if good_credit_score :
    dp = price*0.1
else:
    dp = price*0.2
print(f"downpayment amount ${dp}")

#approve the loan if he's our employee & income > 7lacks -else,
#approve the lone if the yearly income is more than 10lacks
#and credit score is more than 650
#and no criminal record.

our_employee = False
income = 1500000
credit_score = 675
cri_rec = False

if our_employee and income > 700000:
    print("loan approved")
elif not our_employee and income >1000000 and credit_score >650 and not cri_rec:
    print("loan approved")
else :
    print("loan not approved")

#ask users to provide the weight in KG or Lbs
#convert the input to the other unit (eg. Lbs to KG or vice versa)
#01kg = 2.205lbs

w = input("what is your weight in numeric value? :" )
u = input("unit? kg/lbs? :")
c = 2.205
if u.upper() == "KG":
    w1 = float(w)*c
    print(f"your weight is {round(w1,2)} lbs")
elif u.upper() == "LBS":
    w1 = float(w)*(1/c)
    print(f"your weight is {round(w1,2)} kg")
else :
    print("pls check your input")




