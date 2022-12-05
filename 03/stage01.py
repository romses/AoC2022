score = 0

f = open("input","r")
lines = f.readlines()

for line in lines:
    line=line.strip()
    bag_seperator = int(len(line)/2)

    left,right=line[:bag_seperator],line[bag_seperator:]
    for char in left:
        if(char in right):
            if ord(char) >= ord('a'):
                score += ord(char)-ord('a') + 1
            else:
               score += ord(char)-ord('A') + 27
            break

print("Score = {}".format(score))