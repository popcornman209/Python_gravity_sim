import turtle, gravity
file = open("saves/"+input("save file: ")+".txt", "r")
lines = file.readlines()
if "p: " in file.read():
    print("WARNING! there is custom python lines in this file.")
    answer = input("would you still like to run? ")
    if answer.lower() not in ["yes","y","t"]:
        exit()
objects = []
runFile = ""
screen = turtle.Screen()
screen.delay(0)
screen.tracer(0, 0)
for line in lines:
    line = line.replace("\n", "")
    if line.startswith("f: "):
        runFile = line[3:]
    elif line.startswith("o: "):
        info = eval(line[3:])
        objects.append(gravity.object(info[0],info[1],info[2],info[3]))
    elif line.startswith("c: "):
        print(line[3:])
    elif line.startswith("p: "):
        exec(line[3:])
    elif line.startswith("v: "):
        temp = eval(line[3:])
        exec(temp[0]+" = "+str(temp[1]))
if runFile:
    exec(open(runFile, "r").read())
else:
    print("save file does not have a run file!")