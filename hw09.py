#Description

#This function enacts a scene of Pokemon (All copyrights belong to Nintendo) In which Ash (red turtle, gray body)
#leads pikachu(yellow and off yellow) through a route where he encounters his Rival Gary. When Ash is confronted, the
#music changes to represent the rival encounter music from the games, and after the cheesy dialogue is done, the
#music changes once more to the battle music, as the background undergoes a common transition form the games, 
#dropping the turtles in the battle screen, where they are resized to represent the new viewpoint. Since objects
#cannot be created in the world (apart from turtles) The attacks had to be turtles in a shape reminiscent of the object
#they represent. As such Bolt (a narrow long yellow turtle) symbolized an electric attack and wgun represented a water gun
#attack by being a round blue turtle that splashes on the opponent. In order to launch the attack turtles, the 
#turtles representing pokemon were taught a function that simulates charging and firing an object. To teach the turtles 
#that function as well as the function to simulate fainting the turtles were made into Pokemon, a subclass of turtle containing
#the afformentioned functions. After the fight, all the previously used turtles (with the exception of the hidden turtles
#used to drop backgrounds and dialogue) are led through a simple dance sequence to the pokemon theme music before embarking
#on a path determined by random pen width, color, length, and angle for 19.5 seconds.


#modules used
from time import sleep
from random import randrange

#define Class
class Pokemon(Turtle):
  def fight(self,target):
    world = self.getModelDisplay()
    color = self.getShellColor()
    for s in range(11):
      if s%2 == 0:
        self.setShellColor(color)
        world.repaint()
      elif s%2 == 1:
        self.setShellColor(black)
        world.repaint()
      sleep(.1)
    self.turnToFace(target)
    sleep(.1)
    self.forward(5)
    sleep(.1)
    self.backward(5)
  
  def die(self):
    world = self.getModelDisplay()
    x = self.getXPos()
    y = self.getYPos()
    self.turnToFace(x,400)
    for s in range(10):
      h = self.getHeight()
      self.setHeight(h-5)
      self.forward(5)
      sleep(.1)
  
  def win(self):
    world = self.getModelDisplay()
    color = self.getShellColor()
    for s in range(10):
      self.turn(36)
      world.repaint()
      sleep(.1)
    for s in range(10):
      self.turn(-36)
      world.repaint()
      sleep(.1)
    for s in range(3):
      self.setShellColor(white)
      world.repaint()
      sleep(.1)
      self.setShellColor(color)
      world.repaint()
      sleep(.1)
    
#Function Start
def turtles():
  setMediaPath()
#set background
  pic = Picture('pokemon1.gif')
  w = getWidth(pic)
  h = getHeight(pic)
  world = World(w,h)
  b= makeTurtle(world)
  b.hide()
  b.penUp()
  b.moveTo(0,0)
  b.drop(pic)
#start Music

  route = makeSound('Route10.wav')
  play(route)
  
#enter trainers
  ash = Turtle(world)
  
  ash.setShellColor(red)
  ash.setBodyColor(gray)
  ash.penUp()
  ash.moveTo(0,35)
  ash.turnToFace(400,35)
  
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    
  pika = Pokemon(world)
  pika.setBodyColor(yellow)
  y2 = makeColor(230,230,0)
  pika.setShellColor(y2)
  pika.penUp()
  pika.moveTo(0,35)
  pika.turnToFace(400,35)
  
  for step in range(7):
    ash.forward(9)
    sleep(.1)
    pika.forward(9) 
  ash.turn(90)
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  pika.turn(90)
  for step in range(1):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  
  ash.turn(-90)
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  pika.turn(-90)
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  ash.turn(90)
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  pika.turn(90)
  
  ash.turnLeft()
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  pika.turnLeft()
  for step in range(5):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  
  ash.turnRight()
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  pika.turnRight()
  
  ash.turnLeft()
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  pika.turnLeft()
    
  ash.turn(90)
  for step in range(3):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
  pika.turn(90)
  for step in range(2):
    ash.forward(9)
    sleep(.1)
    pika.forward(9)
# battle start
  
  stopPlaying(route)
  fight = makeSound('RivalBattle.wav')
  play(fight)
  
  sleep(2)
  gary = Turtle(world)
  gary.setShellColor(blue)
  gary.setBodyColor(gray)
  gary.penUp()
  gary.moveTo(245,400)
  gary.turnToFace(245,0)
  
  
  for step in range(4):
    gary.forward(9)
    sleep(.1)
  
  squirtle = Pokemon(world)
  squirtle.setShellColor(blue)
  b2=makeColor(100,150,255)
  squirtle.setBodyColor(b2)
  squirtle.penUp()
  squirtle.moveTo(245,400)
  
  for step in range(8):
    gary.forward(9)
    sleep(.1)
    squirtle.forward(9)
  
  #dialogue
  dia = Turtle(world)
  dia.penUp()
  dia.moveTo(0,256)
  dia.hide()
  text = Picture('textbox.png')
  dia.drop(text)
  squirtle.hide()
  
  #Moving background
  frame1 = Picture('battle transition.png')
  frame2 = Picture('battle transition1.png')
  frame3 = Picture('battle transition2.png')
  frame4 = Picture('battle transition3.png')
  sleep(2)
  stopPlaying(fight)
  battle = makeSound('Battle.wav')
  play(battle)
  
  sleep(2)
  ball = Picture('Pokeball1.png')
  ball1 = Picture('Pokeball2.png')
  ball2 = Picture('Pokeball3.png')
  
  dia.moveTo(190,120)
  
  b.drop(frame1)
  sleep(.2)
  b.drop(frame2)
  sleep(.2)
  b.drop(frame3)
  sleep(.2)
  b.drop(frame4)
  ash.hide()
  pika.hide()
  gary.hide()
  sleep(.1)
  dia.drop(ball)
  sleep(.1)
  dia.moveTo(133,63)
  dia.drop(ball1)
  dia.moveTo(0,0)
  
  fight1 = Picture('battlestart.png')
  fight2 = Picture('battle1.png')
  fight3 = Picture('battle2.png')
  
  dia.drop(fight1)
  
  pika.moveTo(120,290)
  squirtle.moveTo(350,150)
  pika.setWidth(50)
  pika.setHeight(60)
  squirtle.setWidth(50)
  squirtle.setHeight(60)
  pika.turnToFace(squirtle)
  squirtle.turnToFace(pika)
  pika.show()
  squirtle.show()
  
  wgun = Turtle(world)
  wgun.setShellColor(blue)
  wgun.setBodyColor(blue)
  wgun.penUp()
  wgun.hide()
  wgun.moveTo(345,155)
  
  sleep(1)
  
  #attacks
  squirtle.fight(pika)
  sleep(.1)
  wgun.show()
  wgun.turnToFace(pika)
  for step in range(5):
    wgun.forward(50)
    sleep(.1)
  wgun.setWidth(75)
  wgun.setHeight(75)
  world.repaint()
  sleep(.1)
  wgun.hide()
  world.repaint()
  
  b.drop(fight2)
  
  sleep(1)
  bolt = Turtle(world)
  bolt.penUp()
  bolt.moveTo(125,285)
  bolt.hide()
  bolt.setShellColor(yellow)
  bolt.setBodyColor(yellow)
  bolt.setHeight(25)
  bolt.setWidth(10)
  bolt.turnToFace(squirtle)
  
  
  pika.fight(squirtle)
  bolt.show()
  for step in range(5):
    bolt.forward(50)
    sleep(.1)
  bolt.setWidth(75)
  bolt.setHeight(75)
  world.repaint()
  sleep(.1)
  for s in range(5):
    if s%2 ==0:
      bolt.hide()
      world.repaint()
    elif s%2 ==1:
      bolt.show()
      world.repaint()
    sleep(.1)
  
  b.drop(fight3)
  
  squirtle.die()
  stopPlaying(battle)
  
  #victory!
  
  win = makeSound('Victory.wav')
  play(win)
  pika.win()
  sleep(.5)
  b.drop(pic)
  
  #re-initialize start scene
  play(route)
  pika.setWidth(15)
  pika.setHeight(18)
  xa = ash.getXPos()
  ya = ash.getYPos()
  pika.moveTo(xa,ya-27)
  pika.turnToFace(ash)
  squirtle.setWidth(15)
  squirtle.setHeight(18)
  xg = gary.getXPos()
  yg = gary.getYPos()
  squirtle.moveTo(xg,yg+27)
  squirtle.turnToFace(gary)
  ash.show()
  gary.show()
  squirtle.die()
  sleep(.1)
  squirtle.hide()
  sleep(1)
  
  #end story
  text2=Picture('textbox2.png')
  dia.moveTo(0,256)
  dia.drop(text2)
  sleep(2)
  b.drop(pic)
  squirtle.turn(180)
  gary.turn(180)
  for step in range(10):
    gary.forward(9)
    squirtle.forward(9)
    sleep(.1)  
  gary.hide()
  world.repaint()
  sleep(1)
  stopPlaying(route)
  credit1 = Picture('credits1.png')
  credit2 = Picture('credits2.png')
  
  b.drop(credit1)
  theme= makeSound('Theme.wav')
  play(theme)
  
  ash.moveTo(125,100)
  ash.turnToFace(125,0)
  pika.moveTo(250,100)
  pika.turnToFace(250,0)
  bolt.setWidth(15)
  bolt.setHeight(18)
  bolt.show()
  bolt.moveTo(375,100)
  bolt.turnToFace(375,0)
  
  squirtle.show()
  squirtle.setWidth(15)
  squirtle.setHeight(18)
  squirtle.moveTo(125,250)
  squirtle.turnToFace(125,0)
  
  gary.moveTo(250,250)
  gary.turnToFace(250,0)
  gary.show()
  
  wgun.show()
  wgun.moveTo(375,250)
  wgun.setWidth(15)
  wgun.setHeight(18)
  wgun.turnToFace(375,0)
  sleep(.1)
  
  #dance
  gary.moveTo(250,190)
  gary.turn(-90)
  gary.penDown()
  gary.setPenColor(gray)
  gary.setPenWidth(20)
  
  pika.moveTo(125,170)
  pika.setPenWidth(20)
  pika.setPenColor(red)
  pika.penDown()
  
  ash.moveTo(130,0)
  ash.turnToFace(240,340)
  ash.penDown()
  ash.setPenWidth(5)
  
  squirtle.moveTo(350,340)
  squirtle.turnToFace(240,0)
  squirtle.penDown()
  squirtle.setPenWidth(5)
  
  bolt.moveTo(350,0)
  bolt.turnToFace(240,340)
  bolt.penDown()
  bolt.setPenWidth(5)
  
  wgun.moveTo(130,340)
  wgun.turnToFace(240,0)
  wgun.penDown()
  wgun.setPenWidth(5)
  
  for ang in range(16):
    gary.forward(5)
    gary.turn(12)
    pika.forward(25)
    pika.turn(12)
    sleep(.1)
  
  pika.setPenColor(white)
  for ang in range(14):
    gary.forward(5)
    gary.turn(12)
    pika.forward(25)
    pika.turn(12)
    sleep(.1)
  
  for side in range(5):
    for step in range(20):
      bolt.forward(11)
      wgun.forward(11)
      ash.forward(11)
      squirtle.forward(11)
      sleep(.1)
    bolt.turn(144)
    wgun.turn(144)
    ash.turn(144)
    squirtle.turn(144)
  sleep(1)
  
  b.drop(credit2)
  sleep(.1)
  ash.clearPath()
  gary.clearPath()
  squirtle.clearPath()
  bolt.clearPath()
  pika.clearPath()
  wgun.clearPath()
  
  pika.setPenWidth(5)
  gary.setPenWidth(5) 
  
  for t in range(195):
    color1 = makeColor(randrange(256),randrange(256),randrange(256))
    color2 = makeColor(randrange(256),randrange(256),randrange(256))
    color3 = makeColor(randrange(256),randrange(256),randrange(256))
    color4 = makeColor(randrange(256),randrange(256),randrange(256))
    color5 = makeColor(randrange(256),randrange(256),randrange(256))
    color6 = makeColor(randrange(256),randrange(256),randrange(256))
    ash.turn(randrange(361))
    gary.turn(randrange(361))
    squirtle.turn(randrange(361))
    bolt.turn(randrange(361))
    pika.turn(randrange(361))
    wgun.turn(randrange(361))
    ash.forward(randrange(150))
    gary.forward(randrange(150))
    squirtle.forward(randrange(150))
    bolt.forward(randrange(150))
    pika.forward(randrange(150))
    wgun.forward(randrange(150))
    ash.setPenWidth(randrange(15))
    gary.setPenWidth(randrange(15))
    squirtle.setPenWidth(randrange(15))
    bolt.setPenWidth(randrange(15))
    pika.setPenWidth(randrange(15))
    wgun.setPenWidth(randrange(15))
    
    ash.setPenColor(color1)
    gary.setPenColor(color2)
    squirtle.setPenColor(color3)
    bolt.setPenColor(color4)
    pika.setPenColor(color5)
    wgun.setPenColor(color6)
    
    sleep(.1)
  stopPlaying(theme)
    
def legal():
  print "All copyrights belong to Nintendo and Pokemon"  
  print "Please don't sue me nintendo..."
  