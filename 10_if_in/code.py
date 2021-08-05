# friends = ["Rolf", "Bob", "Jen"]
# print("Jen" is friends)

# movies_watched = {"The Matrix", "Green Black", "Her"}
# user_movie = input("Enter here your movie you've watched: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print(f"I haven't watched this {user_movie}")

# number = 7
# user_input = input("Enter 'y' if you like to play: ").lower()

# if user_input == "y":
#     user_number = int(input("Guess our number? "))
#     if user_number == number:
#         print("You guessed correctly")
#     elif number - user_number in (1, -1):
#         print("You were off by one")
#     else:
#         print("Sorry it's wrong!")

number = 7
user_input = input("Enter 'y' if you like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number? "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry it's wrong!")
