import gravity, random, turtle, math, save#, pyautogui

amount_of_obs = 250
save_key = "p"

screen = turtle.Screen()
screen.delay(0)
screen.tracer(0, 0)
screen.bgcolor(0,0,0)
objects = []

def saveFile():
  file = save.create("saves/"+input("save name: "),"others/collisionSave.py")
  file.addComment(input("decription: "))
  file.addCustomVar("colors", colors)
  for object in objects: file.addObj(object)
  file.close()
screen.onkey(saveFile, save_key)
screen.listen()

colors = []
for i in range(amount_of_obs):
  objects.append(gravity.object(1,(random.randint(-500,500),random.randint(-500,500)),(random.randint(-100,100)/10,random.randint(-100,100)/10),0.5))
  color = (random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
  objects[i].turt.color(color)
  colors.append(color)

obj_ord = []
for i1 in range(len(objects)):
  for i2 in range(len(objects)):
    if i1 != i2 and [i2,i1] not in obj_ord:
      obj_ord.append([i1,i2])
  print(str(round(100*(i1/amount_of_obs)))+"%")

frame = 0
while True:
  frame += 1
  for order in obj_ord:
    if math.sqrt((objects[order[0]].pos[0]-objects[order[1]].pos[0])**2+(objects[order[0]].pos[1]-objects[order[1]].pos[1])**2) > objects[order[0]].size*20:
      objects[order[0]].calculate(objects[order[1]])
      objects[order[1]].calculate(objects[order[0]])
    else:
      objects[order[0]].vel = ((objects[order[0]].vel[0]+objects[order[1]].vel[0])/2,(objects[order[0]].vel[1]+objects[order[1]].vel[1])/2)
      objects[order[1]].vel = objects[order[0]].vel
  avg_pos = (0,0)
  for obj in objects:
    avg_pos = (avg_pos[0]-obj.pos[0],avg_pos[1]-obj.pos[1])
  avg_pos = (avg_pos[0]/len(objects),avg_pos[1]/len(objects))
  for obj in objects:
    obj.move(avg_pos)
  screen.update()
  #myScreenshot = pyautogui.screenshot()
  #myScreenshot.save("photos/img"+str(frame)+".png")