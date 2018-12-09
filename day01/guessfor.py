age_of_mine = 25


for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_mine:
        print("yes,you got it.")
        break
    elif guess_age < age_of_mine:
        print("think smaller...")
    else:
        print("think bigger!")
else:
    print("you have tried too many times..fuck off")
