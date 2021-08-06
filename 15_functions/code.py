# def hello():
#     print("Hello!")


# hello()

def age_user_in_seconds():
    user_age = int(input("Enter your age? "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is: {age_seconds}")


print("Welcome!")
age_user_in_seconds()
print("Godbye!")
