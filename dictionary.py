
# enter your mobile number
#the program should return back the number in alphabet.

user_input = input("enter mobile no: " )
my_dic = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}
output = ""
for i in user_input:
    output = output+" "+my_dic[i]
print(output)

