from ch2 import scoregrade as grade
f = open("./mathscore.txt", "r")
lines = f.readlines()

f = open("./mathgrade.txt", "w")
for i in lines:
    f.write(i.replace("\n", " "+grade(int(i.split(" ")[1]))+"\n"))
