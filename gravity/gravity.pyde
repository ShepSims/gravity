import os 

WIDTH = 1000
HEIGHT = 1000

class Mouse(object):
    
    def __init__(self, x, y):
        self.position = PVector(x,y)
        self.on = False

class ParticleSystem(object):
    # self.attached == True if the system is the newest 
    # self.position is either the mouse position if self.attached is True, or updated with velocity on each frame if not
    # Array of all particles in system
    # growthRate of particles
    # distance of center of mass from the center of mass of all systems
    # gravity amplifier
    # velocity of system, non-zero only if detached
     # mass of system is mass of all particles in system/3
    # gravity type, False for inverted gravity
    # drawtype choose from dot, line, tracer
    
    # Creates a new particle system wherever the mouse when clicking 
    def __init__(self, x, y, count = 1):
        self.attached = True
        self.position = PVector(x,y)
        self.particles = []
        self.growthRate = .001
        self.distance = 0
        self.gravity=1
        self.velocity = PVector(0,0)
        self.mass=0
        self.gType = True
        self.drawType = "dot"
        self.trace = False
        for i in range(count):
            self.addParticle()
            
    
    def move(self, x, y):
        if self.drawType == "lastfew":
            background(color(255))
        if self.attached == True:
            self.position.x = x
            self.position.y = y
        else:
            self.getVelocity()
            self.position.x += self.velocity.x
            self.position.y += self.velocity.y
            
        self.mass=0
        if len(self.particles)!= 0:
            centroid_x = 0
            centroid_y = 0
            
            for particle in self.particles:
                particle.move()
                particle.display()
                centroid_x+=particle.position.x
                centroid_y+=particle.position.y
                self.mass+=particle.mass/3
            self.gravity=self.mass/len(self.particles)
            
            centroid_x = centroid_x/len(self.particles)
            centroid_y = centroid_y/len(self.particles)
            
            ellipse(centroid_x, centroid_y, self.mass, self.mass)
    
    # Calculate centroid + mass while moving and displaying all particles in system
    # def move(self, x, y):
    #     if self.drawType == "lastfew":
    #         background(color(255))
    #     self.mass=0
    #     if len(self.particles)!= 0:
    #         centroid_x = 0
    #         centroid_y = 0
            
    #         self.position.x = x
    #         self.position.y = y
    #         for particle in self.particles:
    #             particle.move()
    #             particle.display()
    #             centroid_x+=particle.position.x
    #             centroid_y+=particle.position.y
    #             self.mass+=particle.mass/3
    #         self.gravity=self.mass/len(self.particles)
            
    #         centroid_x = centroid_x/len(self.particles)
    #         centroid_y = centroid_y/len(self.particles)
            
    #         ellipse(centroid_x, centroid_y, self.mass, self.mass)
            
         
    # Add particle to system
    def addParticle(self):
        self.particles.append(Particle(self))
        
    def getDistance(self):
        overall = PVector(0,0)
        for system in systems:
            if system != self:
                overall.x += system.position.x
                overall.y += system.position.y
                
        overall.x = overall.x/len(systems)
        overall.y = overall.y/len(systems)
        
        if overall.x == 0:
            overall.x = WIDTH/2
        if overall.y == 0:
            overall.x = HEIGHT/2
            
        print(overall)
        # Gets and sets the distance from the center of mass of the system to the center of mass of all systems
        self.distance = sqrt((self.position.x - overall.x)**2 + (self.position.y - overall.y)**2)
        
        # Change of coords
        # d.x being positive means the particle is to the left of the system
        # d.y being positive means the particle is above the system
        
        self.d = PVector(overall.x - self.position.x, overall.y - self.position.y)
        # print("System Pos: " + str(self.system.position.x), str(self.system.position.y), "Part Pos: "+str(self.position.x),  str(self.position.y))
        
        # angle in radians between center and particle 
        self.angle = atan2(self.d.y, self.d.x)
    
    def getVelocity(self):
        self.getDistance()
        
        self.velocity.x += cos(self.angle)*self.distance
        self.velocity.y += sin(self.angle)*self.distance
        
        print(self.velocity)
        
    # Pop oldest particle 
    def popParticle(self):
        try: 
            first = self.particles[0]
            self.particles = self.particles[1:]
        except: print("already empty")
            
                    
            

class Particle(object):
    
    def __init__(self, system):
        self.mass = 0
        self.age = 0
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
            self.trace()
                
                
    def move(self):
        
        self.updateVelocity()
        self.updatePosition()
        if self.mass >= self.system.growthRate:
            self.mass += self.system.growthRate
        else: 
            self.mass = self.system.growthRate
            
        self.age+=1
            
            
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
        self.previousPosition = PVector(self.position.x, self.position.y)
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        
        self.lastfew.append(self.previousPosition)
        if len(self.lastfew)>10:
            self.lastfew.pop(0)
    
    def updateVelocity(self):
        
        self.getDistance()
        # Add xy-components of gravity vector to velocity
        if self.system.gType:
            self.velocity.x += cos(self.angle)*self.system.gravity*self.system.mass/self.distance**2
            self.velocity.y += sin(self.angle)*self.system.gravity*self.system.mass/self.distance**2
        else:
            self.velocity.x += cos(self.angle)*self.system.gravity*self.distance**2/100000
            self.velocity.y += sin(self.angle)*self.system.gravity*self.distance**2/100000
        # Bounce off of the cursor if particle gets close 
        #if self.distance < 10:self.bounce()
        
    def bounce(self):
        self.velocity.x = -self.velocity.x
        self.velocity.y = -self.velocity.y
    
    def trace(self):
        for i in self.lastfew:
            ellipse(i.x, i.y, 1, 1)
        
systems = []

def setup():
    strokeWeight(1)
    size(WIDTH,HEIGHT)
    background(color(255))
    systems.append(ParticleSystem(mouseX,mouseY))
            

def draw():
    mouse = Mouse(mouseX, mouseY)
    if mousePressed:
        mouse.on = True
    else:
        mouse.on = False
    # mouse takes control over top system
    for system in systems:
        system.move(mouse.position.x, mouse.position.y)
        
    
def keyPressed():
    if keyCode == UP:
        systems[len(systems)-1].addParticle()
    if keyCode == DOWN:
        systems[len(systems)-1].popParticle()
        
    if keyCode == LEFT:
        systems[len(systems)-1].growthRate-=.001
    if keyCode == RIGHT:
        systems[len(systems)-1].growthRate+=.001
     
    # press c
    # clear the screen
    if key == "c":
        background(color(255))
        
        
    # switch to dot draw type
    if key == "d":
        systems[len(systems)-1].drawType = "dot"
        
    # switch to line drawings
    if key == "l":
        systems[len(systems)-1].drawType = "line"
        
        
    if key == "t":
        systems[len(systems)-1].trace = not systems[len(systems)-1].trace
        
        
    if key == "g":
        systems[len(systems)-1].gType = not systems[len(systems)-1].gType
        
        
    if key == "f":
        systems[len(systems)-1].drawType = "lastfew"
        
    if key == "b":
        systems[len(systems)-1].attached = False
        systems.append(ParticleSystem(mouseX,mouseY))
        
        
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
