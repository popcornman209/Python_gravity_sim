import turtle,math
def cal(obj1,obj2):
  relPos = (obj1.pos[0]-obj2.pos[0],obj1.pos[1]-obj2.pos[1])
  divAmount = abs(relPos[0])+abs(relPos[1])
  dir = (relPos[0]/divAmount, relPos[1]/divAmount)
  dist = math.sqrt(relPos[0]**2+relPos[1]**2)*-1
  finalVel = (dir[0]*obj2.mass/dist,dir[1]*obj2.mass/dist)
  return(finalVel)
  
class object:
  def __init__(self, mass, startingPosition, startingVelocity, size):
    self.info = [mass, startingPosition, startingVelocity, size]
    self.turt = turtle.Turtle()
    self.mass = mass
    self.vel = startingVelocity
    self.size = size
    self.pos = startingPosition
    self.turt.pu()
    self.turt.goto(self.pos)
    self.turt.shape("circle")
    self.turt.shapesize(size)
  def calculate(self, object2):
    out = cal(self,object2)
    self.vel = (self.vel[0]+out[0],self.vel[1]+out[1])
  def move(self, offset):
    self.pos = self.pos[0]+self.vel[0],self.pos[1]+self.vel[1]
    self.turt.goto(self.pos[0]+offset[0],self.pos[1]+offset[1])