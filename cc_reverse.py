def reverse(st):
    r_name = st[::-1]
    return r_name


print(reverse("bollade"))


name = input("what is your name?")
print("Your name reversed is:", name[:: -1])
