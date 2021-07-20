from vpython import *
from math import sin, cos, atan, degrees, radians

# SIMULATION CONFIG
RATE = 200

# INITIAL VARIABLES
initialHeight = 0.25
initialVelocity = 4.5
angle = 20

def setup_display_window():
    scene.background = color.white
    scene.title = 'Hod'
    scene.x = 0
    scene.y = 0
    scene.width = 800
    scene.height = 600
    scene.range = 1
    scene.center = vector(1, initialHeight, 0)
    
    return scene

scene = setup_display_window()

label1 = label(pos=vec(1, 0.7, 0), text='Rychlost x: ')
label2 = label(pos=vec(1, 0.6, 0), text='Rychlost y: ')
label3 = label(pos=vec(1, -0.4, 0), text='Vzdialenost: ')
label4 = label(pos=vec(1, -0.6, 0), text='Cas: ')
label5 = label(pos=vec(1, -0.5, 0), text='Uhol: ')

table = box(pos=vector(-1, initialHeight - 0.01, 0), size=vector(2, 0.01, 1), color=color.cyan)

ball = sphere(pos=vector(0, initialHeight, 0), radius=0.02, color=color.green, make_trail=True)

floor = box(pos=vector(0, 0, 0), size=vector(5, 0.01, 1), color=color.red)

# parametrization
t = 0
dt = 0.001
g = -9.8
gravity = vector(0, g * dt, 0)

ball_velocity = vector(
    initialVelocity * cos(radians(angle)),
    initialVelocity * sin(radians(angle)),
    0
)

# main simulation logic loop 
while True:
    rate(RATE)
    ball_velocity = ball_velocity + gravity

    ball.pos += ball_velocity * dt

    ball_pos = ball.pos

    y = ball_pos.y
    label1.text = "Rychlost x: " + str(ball_velocity.x) + "m/s"
    label2.text = "Rychlost y: " + str(ball_velocity.y) + "m/s"

    if float(y) <= 0:
        angle = degrees(atan(abs(float(ball_velocity.y) / float(ball_velocity.x))))
        
        t = format(t, '.3f')
        angle = format(angle, '.3f')

        label3.text = 'Vzdialenost: ' + str(ball_pos.x) + ' metrov'
        label4.text = 'Cas: ' + t + ' sekund'
        label5.text = 'Uhol: ' + angle + ' stupnov'

        break

    t += dt



