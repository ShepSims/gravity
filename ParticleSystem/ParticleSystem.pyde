WIDTH = 500
HEIGHT = 500

class ParticleSystem(object):
    
    def __init__(self):
        self.active = False
        self.particles = []
        
        
    def render(self, x, y):
        for particle in self.particles:
            particle.update(x,y)
            particle.display()
            
    def activate(self, spawnX, spawnY, count = 10):
        self.active = True
        for i in range(count):
            self.particles.append(Particle(position = PVector(spawnX + random(-50, 50), spawnY+ random(-50, 50))))
            
            

class Particle(object):
    
    def __init__(self, position, acceleration = PVector(0,0), velocity = PVector(1,1)):
        self.acceleration = acceleration
        self.position = position
        self.velocity = velocity

    def display(self):
        stroke(0)
        fill(color(0))
        ellipse(self.position.x, self.position.y, 1, 1)
            
        
    def update(self,x,y):
        if abs(self.position.x - x) < 5 and abs(self.position.y - y) < 5:
            self.respawn()
        if self.position.x < x:
            self.position.x += self.velocity.x
        else:
            self.position.x -= self.velocity.x
            
        if self.position.y < y:
            self.position.y += self.velocity.y
        else:
            self.position.y -= self.velocity.y
            
        if abs(self.position.x - x) > 75 and self.velocity.x < .5:
            self.velocity.x += .1
        elif abs(self.position.x - x) < 75 and self.velocity.x > .1:
            self.velocity.x -= .1
        if abs(self.position.y - y) > 75 and self.velocity.y < .5:
            self.velocity.y += .1     
        elif abs(self.position.y - y) < 75 and self.velocity.y > .1:
            self.velocity.y -= .1
        
    def respawn(self):
        self.position = PVector(random(0,WIDTH),random(0,HEIGHT))
                
            
sys = ParticleSystem()

def setup():
    size(500,500)

def draw():
    background(color(255))
    if mousePressed:
        if not sys.active: sys.activate(mouseX, mouseY, 2000)
    sys.render(mouseX, mouseY)
        
    
