values = [
    line.strip() for line in open('day_1').readlines()
]

max_calories = 0
calories = 0

calories_list = []

for line in values:
    if not line:
        if calories > max_calories:
            max_calories = calories
        calories_list.append(calories)
        calories = 0
        continue

    calories += int(line)

print(max_calories)
print(sum(sorted(calories_list)[-3:]))
