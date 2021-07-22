import vpython
from math import sin, cos

# initial parameters
initialHeight = 0.25
initialVelocity = 10
angle = 20 # degrees

t = 0
dt = 0.001

g = -9.8
gravity_force = vpython.vector(0, g * dt, 0)

ball_velocity = vpython.vector(
    initialVelocity * cos(angle),
    initialVelocity * sin(angle),
    0
)

print(ball_velocity)
