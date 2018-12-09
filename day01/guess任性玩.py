age_of_mine = 25

count = 0
while count < 3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_mine:
        print("yes,you got it.")
        break
    elif guess_age < age_of_mine:
        print("think smaller...")
    else:
        print("think bigger!")
    count += 1
    if count == 3:
        continue_confirm = input("do you want to kepp guessing..?")
        if continue_confirm != 'n':
            count = 0

# if count ==3
# else:
#   print("you have tried too many times..fuck off")
