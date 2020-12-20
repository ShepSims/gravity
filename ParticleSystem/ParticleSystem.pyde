WIDTH = 2000
HEIGHT = 2000

class ParticleSystem(object):
    
    def __init__(self, x, y, count = 10):
        self.position = PVector(x,y)
        self.particles = []
        self.gravity = .02
        self.mass = 10000
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
                    
            

class Particle(object):
    
    def __init__(self, system):
        self.system = system
        self.distance_to_center = random(100)
        self.angle = radians(random(0,360))
        self.mass = 5
        self.velocity = PVector(random(0,5),random(0,5))
        self.momentum = PVector(self.mass * self.velocity.x,self.mass * self.velocity.y)
        self.position = PVector( system.position.x + self.distance_to_center*cos(self.angle),  system.position.y + self.distance_to_center*sin(self.angle))
        self.bounce = False

    def display(self):
        stroke(0)
        fill(color(0))
        ellipse(self.position.x, self.position.y, self.mass, self.mass)
            
        
    def move(self):
        
        self.updatePosition()
        self.updateVelocity()
        
            
            
    def getDistance(self, other_point):
        
        # Gets and sets the distance from the center point of the system to the point
        
        # Change of coords
        # d.x being positive means the particle is to the left of the system
        # d.y being positive means the particle is above the system
        
        self.d = PVector(other_point.position.x - self.position.x, other_point.position.y - self.position.y)
        # print("System Pos: " + str(self.system.position.x), str(self.system.position.y), "Part Pos: "+str(self.position.x),  str(self.position.y))
        
        # angle in radians between other particle and particle 
        self.angle = atan2(self.d.y, self.d.x)
        
    def updatePosition(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.distance_to_center = sqrt((self.position.x - self.system.position.x)**2 +(self.position.y - self.system.position.y)**2)
        self.angle_to_center = PVector(self.distance_to_center.x - self.position.x, self.distance_to_center.y - self.position.y)
        return self.position
    
    def updateVelocity(self):
        
        for particle in self.system.particles if particle.bounce == False:
            if getDistance(particle) < 5:
                self.bounce(self, particle) 
        
        if self.distance_to_center < 10:self.bounce(self, system)
        self.momentum = mass *  (self.velocity.x+self.velocity.y)
        
    # update velocity 
    def bounce(self, particle):
        
        u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
        
        self.velocity.x = self.velocity.x - 2*particle.mass/self.mass*
        self.velocity.y = -self.velocity.y
      
    #  Add xy-components of gravity vector to velocity  
    def gravity(self):

        self.velocity.x += cos(self.angle)*self.system.gravity*self.distance
        self.velocity.y += sin(self.angle)*self.system.gravity*self.distance
        
systems = []
systems.append(ParticleSystem(0,0, 1))

def setup():
    size(500,500)
            

def draw():
    background(color(255))

    try: 
        current = systems[len(systems)-1]
        if keyPressed:
            if keyCode == UP:
                current.addParticle()
            if keyCode == DOWN:
                current.popParticle()
    except:
        pass
    for system in systems:
        system.render(mouseX, mouseY)
        
    
