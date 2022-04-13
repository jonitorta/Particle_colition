import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib import cm

#Here we define the particle class with.
class Particle():
    #Properties of the particle with a mass and velocity we will implemet
    #acceleration in the future.
    def __init__(self,mass=1,velocity=[1,1],position=[1,1]):
        self.mass = mass
        self.velocity = np.array(velocity)
        self.position = np.array(position)
    #This method computes particle position, frames argument describes how time
    #is discretized this helps to animate better, more frames make a smoother animation
    #times argument is for how many times we call function move, if velocity is m/s then
    #times * frames = seconds particle is moving.
    def move(self,frames=60,times=1,count=1,values=None):
        time_unit=1/frames
        if values is None : values = [self.position]
        if count<=times:
            self.position = time_unit*self.velocity+self.position
            count = count + 1
            values.append(self.position)
            self.move(frames,times,count,values)
        return values
        
#Here we create a random number of particles between 1,20 with random
#mass, velocity and position within an interval.
particles_number= 2 #np.random.randint(1,20)
particles = [
    Particle(
        mass=np.random.uniform(0.1,10),
        velocity=[np.random.uniform(1,3),np.random.uniform(1,3)],
        position=[np.random.uniform(0,2),np.random.uniform(0,2)]
    )
    for i in range(particles_number)
]
#Evolve the system # of times and save position of each particle in a list.
times = 60
positions = [particles[i].move(times=times) for i in range(particles_number)]
#Here we make individual list for x and y positions for each particle.
x_position , y_position = [[] for i in range(particles_number)] , [[] for i in range(particles_number)]
for i in range(particles_number):
    for j in range(times):
        x_position[i].append(positions[i][j][0])
        y_position[i].append(positions[i][j][1])
# initialize a figure, make a color range to color each point





fig, ax = plt.subplots()
ax.set_xlim([0,10])
ax.set_ylim([0,10])

points = []
for j, (col, mar) in enumerate(zip(["green", "blue"], ["o", "x"])):
    newpoint, = ax.plot(x_position[j][0], y_position[j][0], color=col, marker=mar)
    points.append(newpoint)

def animation_frames(i):
    for j in range(0,2):
        points[j].set_data(x_position[j][i], y_position[j][i])        


animation = FuncAnimation(fig, animation_frames, frames=len(x_position[0]), interval=30)
    
plt.show()





pass