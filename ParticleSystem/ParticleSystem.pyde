WIDTH = 500
HEIGHT = 500

class ParticleSystem(object):
    
    def __init__(self, x, y, count = 10):
        self.position = PVector(x,y)
        self.particles = []
        self.gravity = .01
        for i in range(count):
            self.addParticle()
        
    def render(self, x, y):
        self.position.x = x
        self.position.y = y
        
        for particle in self.particles:
            particle.move()
            particle.display()
            
    def addParticle(self):
        self.particles.append(Particle(self))
        
    def popParticle(self):
        self.particles.pop()
        
    def increaseGravity(self):
        self.gravity += .0001
        
    def decreaseGravity(self):
        self.gravity -= .0001
        if self.gravity <= 0:
            self.gravity = .00001
        
                    
            

class Particle(object):
    
    def __init__(self, system):
        self.system = system
        self.distance = random(100)
        self.angle = radians(random(0,360))
        self.velocity = PVector(random(0,5),random(0,5))
        self.position = PVector( system.position.x + self.distance*cos(self.angle),  system.position.y + self.distance*sin(self.angle))
        self.tracer = False

    def display(self):
        stroke(0)
        fill(color(0))
        ellipse(self.position.x, self.position.y, 5, 5)
            
        
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
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
    
    def updateVelocity(self):
        
        self.getDistance()
        # Add xy-components of gravity vector to velocity
        self.velocity.x += cos(self.angle)*self.system.gravity*self.distance**2
        self.velocity.y += sin(self.angle)*self.system.gravity*self.distance**2
        
        # Bounce off of the cursor if particle gets close 
        if self.distance < 10:self.bounce()
        
    def bounce(self):
        self.velocity.x = -self.velocity.x
        self.velocity.y = -self.velocity.y
    
    def trace(self):
        point(self.position.x, self.position.y)
        
systems = []
systems.append(ParticleSystem(0,0, 1))

def setup():
    size(500,500)
    background(color(255))
            

def draw():
    try: 
        current = systems[len(systems)-1]
        if keyPressed:
            if keyCode == UP:
                current.addParticle()
            if keyCode == DOWN:
                current.popParticle()
            if keyCode == LEFT:
                current.decreaseGravity()
            if keyCode == RIGHT:
                current.increaseGravity()
            if key == "c":
                background(color(255))
    except:
        pass
    for system in systems:
        system.render(mouseX, mouseY)
        
    
