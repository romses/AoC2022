moves={'A X':0 + 3, # loose with scissors (0+3)
       'A Y':3 + 1, # Draw with rock (3+1)
       'A Z':6 + 2, # Win with paper (6+2)
       'B X':0 + 1, # loose with rock (0+1)
       'B Y':3 + 2, # draw with paper (3+2)
       'B Z':6 + 3, # win with scissors (6+3)
       'C X':0 + 2, # loose with paper (0+2)
       'C Y':3 + 3, # draw with scissors (3+3)
       'C Z':6 + 1  # win with rock (6+1)
} 

score = 0

f = open("input","r")
lines = f.readlines()

for line in lines:
  score += moves[line.strip()]

print("You scored {} points".format(score))
