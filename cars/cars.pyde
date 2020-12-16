class Car(object):
    
    def __init__(self, c = color(255), xpos = 100, ypos = 100, speed = 1):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.laps = 0
        self.xs = 20
        self.ys = 10

    def display(self):
        stroke(0)
        rectMode(CENTER)
        fill(self.c)
        rect(self.xpos, self.ypos, self.xs, self.ys)

    def drive(self):
        self.laps+=1
        self.xpos += self.speed 
        if self.xpos > width:
            self.xpos = 0
            if self.xs < 30:
                self.xs = self.xs + random(0,1)
            elif self.xs > 30:
                self.xs = self.xs - random(0,1)
            else: self.xs += random(0,1)
            if self.ys < 20:
                self.ys = self.ys + random(0,1)
            elif self.ys > 40:
                self.ys = self.ys - random(0,1)
            else: self.ys += random(0,1)
            self.ys = self.ys + random(-.05,.05)
        if self.laps == 5:
            self.c = color(random(0,255),random(0,255),random(0,255))
            self.laps = 0
            
            
car1 = Car(color(255), 0, 10, 1.2)
car2 = Car(color(255), 0, 20, 4.1)
car3 = Car(color(0,255,255), 0, 30, 2.2)
car4 = Car(color(255), 0, 40, 1)
car5 = Car(color(255), 0, 50, 3.4)
car6 = Car(color(255), 0, 60, 2.5)
car7 = Car(color(255), 0, 90, 8.2)
car8 = Car(color(255), 0, 110, 1.4)
car9 = Car(color(255), 0, 120, 4)
car10 = Car(color(255), 0, 130, 2.3)
car11 = Car(color(255), 0, 140, 2)
car12 = Car(color(255), 0, 150, 3.3)
car13 = Car(color(255), 0, 160, 6.7)
car14 = Car(color(255),0,90,8)
car14 = Car(color(255),0,190,8)


cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, car13, car14]

def setup():
    size(200,200)

def draw():
    background(0)
    for car in cars:
        car.drive()
        car.display()
    
