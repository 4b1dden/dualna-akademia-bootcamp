"""
Simulate projectile motion with VPython.
Code by: Magnus K. Øye, Dated: 08.02-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy
"""

from vpython import *
from math import sin, cos, atan, degrees

initialHeight = 0.25
initialVelocity = 4.8
Angle = 20

# Set up the display window

scene.background = color.white
scene.title = 'Projectile Motion'
scene.x = 0
scene.y = 0
scene.width = 800
scene.height = 600
scene.range = 1
scene.center = vector(1, initialHeight, 0)

# Creating obects

table = box(pos=vector(-1, initialHeight - 0.01, 0), size=vector(2,
            0.01, 1), color=color.cyan)

ball = sphere(pos=vector(0, initialHeight, 0), radius=0.02,
              color=color.green, make_trail=True)

floor = box(pos=vector(0, 0, 0), size=vector(5, 0.01, 1),
            color=color.red)

label1 = label(pos=vec(1, 0.7, 0), text='Current velocity vx: ')
label2 = label(pos=vec(1, 0.6, 0), text='Current velocity vy: ')
label3 = label(pos=vec(1, -0.4, 0), text='Distance: ')
label4 = label(pos=vec(1, -0.6, 0), text='Time: ')
label5 = label(pos=vec(1, -0.5, 0), text='Angle: ')

# Paramaters

t = 0
dt = 0.001
g = -9.8  # m/s^2
gravity = vector(0, g * dt, 0)

# Velocity vector for ball:

ballv = vector(initialVelocity * cos(Angle * pi / 180), initialVelocity
               * sin(Angle * pi / 180), 0)

# Simulate event

while True:
    rate(200)
    ballv = ballv + gravity
    ball.pos += ballv * dt
    velocity = str(ballv)
    position = str(ball.pos)
    y = (position.split(',')[1])[1:-1]
    vx = (velocity.split(',')[0])[1:-1]
    vy = (velocity.split(',')[1])[1:-1]
    label1.text = 'Current velocity vx: ' + vx + ' m/s'
    label2.text = 'Current velocity vy: ' + vy + ' m/s'
    
    # breaks loop when ball hits the ground

    if float(y) <= 0:
        angle = degrees(atan(abs(float(vy) / float(vx))))
        t = format(t, '.3f')
        angle = format(angle, '.3f')
        label3.text = 'Distance: ' + (position.split(',')[0])[1:-1] \
            + ' meter'
        label4.text = 'Time: ' + t + ' sec'
        label5.text = 'Angle: ' + angle + ' degrees'

        print ('Position x =', position.split(',')[0], 'meter, time ='
               , t, 's')

        print ('Angle at impact:', angle)
        break

    t += dt
		