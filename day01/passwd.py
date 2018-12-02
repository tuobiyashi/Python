# import getpass

_username = "helong"
_password = "genius"
username = input("username:")
password = input("password:")
# password1 = getpass.getpass("password1:")

if _username == username and _password == password:
    print("welcom user {name} login...".format(name=username))
else:
    print("Invalid username or password...!")

# print(username, password)
