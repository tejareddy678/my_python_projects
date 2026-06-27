import random as rd
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
spec_char = "!@$%^&*()_+"
digits = "0123456789"
combined = caps + small + spec_char + digits
password = ""
Length = int(input("Enter the length of the password you want: "))
password = password + rd.choice(caps)
password = password + rd.choice(small)
password = password + rd.choice(spec_char)
password = password + rd.choice(digits)
for i in range(1,Length - 4 + 1):
    password = password + rd.choice(combined)
print(f"Your password is \"{password}\"")


