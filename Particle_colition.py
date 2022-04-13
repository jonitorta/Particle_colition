import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


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
particles_number=np.random.randint(1,20)
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
position = [particles[i].move(times=times) for i in range(particles_number)]






def update(iterable,coords):
    pass




pass