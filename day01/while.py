'''
count = 0
while True:
    print("count:", count)
    count += 1  # count=count+1
'''

"""
while True:
    if count == 3:
        break
"""
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

# if count ==3
else:
    print("you have tried too many times..fuck off")
