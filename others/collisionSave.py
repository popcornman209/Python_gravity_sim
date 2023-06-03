import gravity, random, turtle, math#, pyautogui

screen = turtle.Screen()
screen.delay(0)
screen.tracer(0, 0)
screen.bgcolor(0,0,0)

i = 0
for object in objects:
  object.turt.color(colors[i])
  i += 1

obj_ord = []
for i1 in range(len(objects)):
  for i2 in range(len(objects)):
    if i1 != i2 and [i2,i1] not in obj_ord:
      obj_ord.append([i1,i2])
  print(str(round(100*(i1/len(objects))))+"%")

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