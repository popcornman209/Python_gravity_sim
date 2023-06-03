import gravity, random, turtle
screen = turtle.Screen()
screen.delay(0)
screen.tracer(0, 0)
objects = []
for i in range(250):
    objects.append(gravity.object(0.25,(random.randint(-500,500),random.randint(-500,500)),(0,0),0.5))
    objects[i].id = i
    objects[i].turt.color(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)

while True:
    for obj1 in objects:
        for obj2 in objects:
            if obj1.id != obj2.id:
                obj1.calculate(obj2)
    avg_pos = (0,0)
    for obj in objects:
        avg_pos = (avg_pos[0]-obj.pos[0],avg_pos[1]-obj.pos[1])
        avg_pos = (avg_pos[0]/len(objects),avg_pos[1]/len(objects))
    for obj in objects:
        obj.move(avg_pos)
    screen.update()