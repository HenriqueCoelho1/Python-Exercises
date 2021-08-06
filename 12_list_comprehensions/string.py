friends = ["Rolf", "Sam", "Samantha", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]


# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s: ", id(starts_s))
