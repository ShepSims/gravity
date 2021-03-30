WIDTH = 2000
HEIGHT = 1000
G = 9.8

class Cluster(object):
    
    def __init__(self, gravityCoefficient, x, y, count = 5):
        self.centroid = PVector(x,y)
        self.particles = []
        self.dots = []
        self.dashes = []
        self.mass = .5
        self.gravity = self.mass*gravityCoefficient
        self.gType = True
        self.drawType = "dot"
        self.trace = False
        for i in range(count):
            self.addParticle()
            
        
    def move(self, x, y):
        self.position.x = x
        self.position.y = y
        if self.drawType=="lastfew": background(color(255))
        for particle in self.particles:
            particle.move()
            particle.display()
            
    # Add a particle to the system
    def addParticle(self):
        self.particles.append(Particle(self))
        
    def popParticle(self):
        try: self.particles.pop()
        except: print("already empty")
        
    # Get average position of particles 
    def get_centroid(self):
        x = 0
        y = 0
        for particle in self.particles:
            x += particle.position.x
            y += particle.position.y
        x=x/self.particles.length
        y=y/self.particles.length
        
    def increaseGravity(self):
        self.gravity += 1
        
    def decreaseGravity(self):
        self.gravity -= 1
        if self.gravity <= 0:
            self.gravity = 1
            
            
                    
            

class Particle(object):
    
    def __init__(self, system):
        self.system = system
        self.distance = random(100)
        self.angle = radians(random(0,360))
        self.velocity = PVector(random(0,.1),random(0,.1))
        self.position = PVector( system.position.x + self.distance*cos(self.angle),  system.position.y + self.distance*sin(self.angle))
        self.lastfew = []

    def display(self):
        stroke(0)
        fill(color(0))
        if self.system.drawType=="dot": ellipse(self.position.x, self.position.y, 2, 2)
        if self.system.drawType=="line":
            line(self.previousPosition.x, self.previousPosition.y, self.position.x, self.position.y)
        if self.system.drawType=="lastfew": 
            for prevpos in self.lastfew:
                print(len(self.lastfew))
                ellipse(prevpos.x, prevpos.y, 2, 2)
                
                
    def move(self):
        
        self.updateVelocity()
        self.updatePosition()
            
            
    def getDistance(self):
        
        # Gets and sets the distance from the center point of the system to the point
        self.distance = sqrt((self.position.x - self.system.position.x)**2 +(self.position.y - self.system.position.y)**2)
        
        # Change of coords
        # d.x being positive means the particle is to the left of the system
        # d.y being positive means the particle is above the system
        
        self.d = PVector(self.system.position.x - self.position.x, self.system.position.y - self.position.y)
        # print("System Pos: " + str(self.system.position.x), str(self.system.position.y), "Part Pos: "+str(self.position.x),  str(self.position.y))
        
        # angle in radians between center and particle 
        self.angle = atan2(self.d.y, self.d.x)
        
    def updatePosition(self):
        
        self.previousPosition = PVector(self.position.x, self.position.x)
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        
        self.lastfew.append(self.position)
        if len(self.lastfew)>14:
            self.lastfew.pop(0)
    
    def updateVelocity(self):
        
        self.getDistance()
        # Add xy-components of gravity vector to velocity
        if self.system.gType:
            self.velocity.x += cos(self.angle)*self.system.gravity/self.distance**2
            self.velocity.y += sin(self.angle)*self.system.gravity/self.distance**2
        else:
            self.velocity.x += cos(self.angle)*self.system.gravity*self.distance**2/10000
            self.velocity.y += sin(self.angle)*self.system.gravity*self.distance**2/10000
        # Bounce off of the cursor if particle gets close 
        #if self.distance < 10:self.bounce()
        
    def bounce(self):
        self.velocity.x = -self.velocity.x
        self.velocity.y = -self.velocity.y
    
    def trace(self):
        point(self.position.x, self.position.y)
        
systems = []

def setup():
    strokeWeight(1)
    size(WIDTH,HEIGHT)
    background(color(255))
    systems.append(ParticleSystem(G, mouseX,mouseY))
            

def draw():
    systems[0].move(mouseX, mouseY)
    
def keyPressed():
    if keyCode == UP:
        systems[0].addParticle()
    if keyCode == DOWN:
        systems[0].popParticle()
    if keyCode == LEFT:
        systems[0].decreaseGravity()
    if keyCode == RIGHT:
        systems[0].increaseGravity()
    if key == "c":
        background(color(255))
    if key == "d":
        systems[0].drawType = "dot"
    if key == "l":
        systems[0].drawType = "line"
    if key == "t":
        systems[0].trace = not systems[0].trace
    if key == "g":
        systems[0].gType = not systems[0].gType
    if key == "f":
        systems[0].drawType = "lastfew"
