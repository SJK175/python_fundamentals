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
