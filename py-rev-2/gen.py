import random

flag = "camp{YOu_foUnD_A_rIGhT_P4tH!}"

choices = [i for i in range(len(flag))]

out = {}

for i in range(len(flag)):
    choice = random.choice(choices)
    choices.remove(choice)

    out[flag[choice]] = choice

print(out)