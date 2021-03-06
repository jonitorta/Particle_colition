import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib import cm


#Here we define the particle class with.
class Particle():
    #Properties of the particle with a mass and velocity we will implemet
    #acceleration in the future.
    def __init__(self,mass=1,velocity=[1,1],position=[1,1],radius=1):
        self.mass = mass
        self.velocity = np.array(velocity)
        self.position = np.array(position)
        self.radius = radius
    #This method computes particle position, frames argument describes how time
    #is discretized this helps to animate better, more frames make a smoother animation
    def move(self,frames=60,values=None):
        time_unit=1/frames
        if values is None : values = [self.position]
        self.position = time_unit*self.velocity+self.position
        return values

class Box():
    #Box class we can define the heigth and width.
    def __init__(self,height=10,width=10):
        self.heigth = height
        self.width = width

#Here we create a random number of particles between 1,20 with random
#mass, velocity and position within an interval.
particles_number = 10#np.random.randint(20,100)
box=Box()
particles = [
    Particle(
        mass=np.random.uniform(0.1,10),
        velocity=[np.random.uniform(-10,10),np.random.uniform(-10,10)],
        position=[np.random.uniform(-2,2),np.random.uniform(-2,2)],
        radius= np.random.uniform(0.5,3)
    )
    for i in range(particles_number)
]
#Evolve the system # of times and save position of each particle in a list.


def evolve_system(particles,box,times=2000):
    particle_number = len (particles)
    positions = [[] for i in range(particle_number)]
    
    for _ in range(times):
        for i in range(particle_number):
            positions[i].append(particles[i].position)
            particles[i].move()
            
            if particles[i].position[0] < -box.width/2 or particles[i].position[0] > box.width/2:
                setattr(particles[i],"position",np.array(positions[i][-1]))
                setattr(particles[i],"velocity",np.array([-particles[i].velocity[0],particles[i].velocity[1] ]))
            if particles[i].position[1] < -box.heigth/2 or particles[i].position[1] > box.heigth/2:
                setattr(particles[i],"position",np.array(positions[i][-1]))
                setattr(particles[i],"velocity",np.array([particles[i].velocity[0],-particles[i].velocity[1] ]))
                
            
    return positions


times = 1000
positions = evolve_system(particles = particles,
                            box = box,
                            times = times)

#Here we make individual list for x and y positions for each particle.
x_position , y_position = [[] for i in range(particles_number)] , [[] for i in range(particles_number)]
radius = []
for i in range(particles_number):
    radius.append(particles[i].radius)
    for j in range(times):
        x_position[i].append(positions[i][j][0])
        y_position[i].append(positions[i][j][1])






# initialize a figure, make a color range to color each point
fig, ax = plt.subplots()
ax.set_xlim([ -box.width/2*1.10 , box.width/2*1.10 ])
ax.set_ylim([ -box.heigth/2*1.10 , box.heigth/2*1.10 ])
plt.plot([-box.width/2,box.width/2],[box.heigth/2,box.heigth/2],color="black")
plt.plot([-box.width/2,box.width/2],[-box.heigth/2,-box.heigth/2],color="black")
plt.plot([-box.width/2,-box.width/2],[-box.heigth/2,box.heigth/2],color="black")
plt.plot([box.width/2,box.width/2],[-box.heigth/2,box.heigth/2],color="black")

points = []
color = cm.rainbow(np.linspace(0, 1, particles_number))
for j, (col, mar) in enumerate(zip(color, ["o" for i in range(particles_number)])):
    newpoint, = ax.plot(x_position[j][0], y_position[j][0], color=col, marker=mar,ms = radius[j]*4)
    points.append(newpoint)

def animation_frames(i):
    for j in range(particles_number):
        points[j].set_data(x_position[j][i], y_position[j][i])        


animation = FuncAnimation(fig, animation_frames, frames=len(x_position[0]), interval=30)
    
plt.show()





pass