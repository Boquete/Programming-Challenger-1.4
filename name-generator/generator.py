import random

with open("lists/male_names.txt") as f:
    male_names = [n.strip() for n in f.readlines()]

with open("lists/female_names.txt") as f:
    female_names = [n.strip() for n in f.readlines()]

with open("lists/surnames.txt") as f:
    surnames = [n.strip() for n in f.readlines()]

print("Your name is:", random.choice([random.choice(male_names), random.choice(female_names)]).title(),
      random.choice(surnames).title())
