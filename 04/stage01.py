f = open("input","r")
lines = f.readlines()

score = 0

def section(input):
  section=[]
  start,stop=input.split("-")  

  for i in range(int(start),int(stop)):
    section.append(i)
  return(section)

for line in lines:
  left,right=line.strip().split(",")
  start1,stop1=left.split("-") 
  start2,stop2=right.split("-") 
  start1=int(start1)
  start2=int(start2)
  stop1=int(stop1)
  stop2=int(stop2)
  if (start1<=start2) and (stop1>=stop2):
    score += 1
  if (start2<=start1) and (stop2>=stop1):
    score += 1
  if(start1==start2) and (stop1==stop2):
    score -=1
print("{} sections are completely overlapping)".format(score))