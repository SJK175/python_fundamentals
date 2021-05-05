# create a guess game - ask user to guess a single digit number.
# no of times the user will get chance = 3

secret_no = 7
guess_counter = 0
guess_limit = 3

while guess_counter < guess_limit:
    guessed = input("guess the number : ")
    guess_counter = guess_counter + 1
    if int(guessed) == secret_no :
        print("you won the game!")
        break

else :
    print ("you failed to guess the number!")
    

# for loop
# calculate total value of cart items & print the
# total value after giving 10% discount
cart = [100, 150, 200, 50]
bill = 0
discount = 0.1
for item in cart :
    bill = bill + item
print(f"total bill : {bill-bill*discount}" )


# write a program to find the largest no of a list.
my_list = [12,15,100,76,9,104]
max_item = my_list[0]
for i in my_list:
    if i> max_item:
        max_item = i
print(max_item)


