import os 

WIDTH = 2000
HEIGHT = 1000

class Mouse(object):
    
    def __init__(self, x, y):
        self.position = PVector(x,y)
        self.on = False

class ParticleSystem(object):
    
    # Creates a new particle system wherever the mouse when clicking 
    def __init__(self, x, y, count = 5):
        self.position = PVector(x,y)
        self.velocity = PVector(0,0)
        self.particles = []
        self.growthRate = .001
        self.gravity=0
        self.mass=500
        self.gType = True
        self.drawType = "dot"
        self.trace = False
        for i in range(count):
            self.addParticle()
            
    # Calculate centroid + mass while moving and displaying all particles in system
    def move(self, x, y):
        self.mass=500
        if len(self.particles)!= 0:
            centroid_x = 0
            centroid_y = 0
            
            self.position.x = x
            self.position.y = y
            for particle in self.particles:
                particle.move()
                particle.display()
                centroid_x+=particle.position.x
                centroid_y=particle.position.y
                self.mass+=particle.mass
            self.gravity=self.mass/len(self.particles)
            
            centroid_x = centroid_x/len(self.particles)
            centroid_y = centroid_y/len(self.particles)
            
            
    # Add particle to system
    def addParticle(self):
        self.particles.append(Particle(self))
        
    # Pop oldest particle 
    def popParticle(self):
        try: 
            first = self.particles[0]
            self.particles = self.particles[1:]
        except: print("already empty")
            
                    
            

class Particle(object):
    
    def __init__(self, system):
        self.mass = 0
        self.system = system
        self.distance = random(100)
        self.angle = radians(random(0,360))
        self.velocity = PVector(random(0,.1),random(0,.1))
        self.position = PVector( system.position.x + self.distance*cos(self.angle),  system.position.y + self.distance*sin(self.angle))
        self.lastfew = []

    def display(self):
        stroke(0)
        fill(color(0))
        if self.system.drawType=="dot": ellipse(self.position.x, self.position.y, self.mass, self.mass)
        if self.system.drawType=="line":
            line(self.previousPosition.x, self.previousPosition.y, self.position.x, self.position.y)
        if self.system.drawType=="lastfew": 
            for prevpos in self.lastfew:
                ellipse(prevpos.x, prevpos.y, 2, 2)
                
                
    def move(self):
        
        self.updateVelocity()
        self.updatePosition()
        self.mass += self.system.growthRate
            
            
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
    systems.append(ParticleSystem(mouseX,mouseY))
            

def draw():
    mouse = Mouse(mouseX, mouseY)
    print("hello")
    if mousePressed:
        mouse.on = True
    else:
        mouse.on = False
    # mouse takes control over top system
    for system in systems:
        system.move(mouse.position.x, mouse.position.y)
        
    
def keyPressed():
    if keyCode == UP:
        systems[0].addParticle()
    if keyCode == DOWN:
        systems[0].popParticle()
        
    # If left/right & g increase/decrease gravity
    # If left/right w/o gincrease/decrease particleGrowthRate
    if keyCode == LEFT:
        systems[0].growthRate-=.001
    if keyCode == RIGHT:
        systems[0].growthRate+=.001
     
        
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
        
    # Press s to save window as shep#.tiff
    if key == "s":
        count=0
        filename=this.dataPath("") + "/shep"+ str(count)+".tiff"
        f = this.dataFile(filename)
        print f
        print f.exists()
        while this.dataFile(filename).isFile():
                count+=1
                filename=this.dataPath("") +"/shep"+ str(count)+".tiff"
            
        save(filename)
        
#def mouseClicked():
 #   systems.append(ParticleSystem(mouseX,mouseY))
