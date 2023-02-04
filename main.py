import random

user_number = int(input("Insert the number: "))
random_number = random.randint(1, user_number)

print(f"Random Number: {random_number}")

i = 1
for i in range(random_number):
    print(f"Yeah, I have cycle! {i+1}")