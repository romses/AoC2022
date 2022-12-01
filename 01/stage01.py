current_calories = 0
max_calories = 0
calories=[]

f = open("input","r")
lines = f.readlines()

for line in lines:
  if len(line)==1:
    if current_calories>max_calories:
      max_calories=current_calories
    calories.append(current_calories)
    current_calories = 0
  else:
    current_calories+=int(line)

calories.sort()

print("The elve carrying the max calories is carrying {} calories".format(calories[-1]))
