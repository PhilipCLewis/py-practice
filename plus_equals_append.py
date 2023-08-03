# Import random below:
import random

# Create random_list below:
random_list = []

for i in range(101):
    random_list.append(random.randint(1, 100))
    # why does += not work in place of append

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
