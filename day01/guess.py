age_of_mine = 25

guess_age = int(input("guess age:"))

if guess_age == age_of_mine:
    print("yes,you got it.")
elif guess_age < age_of_mine:
    print("think smaller...")
else:
    print("think bigger!")
