users = [
    (0, "Bob", "password"),
    (1, "Ralf", "bob123"),
    (2, "Nick", "longpassword"),
    (3, "Leona", "123456")
]


username_mapping = {user[1]: user for user in users}

# print(username_mapping["Bob"])

# for user in users:
#     if user[1] == "Bob":
#         print(user)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your Details is corret")
else:
    print("Your password is incorrect")
