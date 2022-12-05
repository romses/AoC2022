score = 0

f = open("input","r")
lines = f.readlines()

def findbadge(bag1,bag2,bag3):
    reference=bag3
    if (bag1>bag2) and (bag1 > bag3):
        reference = bag1
    if (bag2>bag1) and (bag2 > bag3):
        reference = bag2
    for char in reference:
        if(char in bag1) and (char in bag2) and (char in bag3):
            return(char)


for i in range(0,int(len(lines)/3)):
    elve1=lines[3*i].strip()
    elve2=lines[1+3*i].strip()
    elve3=lines[2+3*i].strip()
    badge = findbadge(elve1,elve2,elve3)
    if ord(badge) >= ord('a'):
        score += ord(badge)-ord('a') + 1
    else:
        score += ord(badge)-ord('A') + 27

print("Score = {}".format(score))