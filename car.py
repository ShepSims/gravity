import color
class Car(object):
    
    def __init__(self):
        self.c = color(255)
        self.xpos = 100
        self.ypos = 100
        self.speed = 1

    def display(self):
      rectMode(CENTER)
      fill(self.c)
      rect(self.xpos, self.ypos, 20, 10)

    def drive(self):
      self.xpos += self.xspeed
      if self.xpos > width:
          self.xpos = 0
