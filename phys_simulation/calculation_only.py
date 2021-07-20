import vpython
from math import sin, cos, atan, degrees, radians

initialHeight = 0.25
initialVelocity = 4.5
angle = 20

t = 0
dt = 0.001
g = -9.8
gravity = vpython.vector(0, g * dt, 0)

ball_velocity = vpython.vector(
    initialVelocity * cos(radians(angle)),
    initialVelocity * sin(radians(angle)),
    0
)

ball_position = {
    'x': 0,
    'y': initialHeight
}

while True:
    ball_velocity = ball_velocity + gravity
    print(ball_velocity)
    ball_position['x'] = ball_position['x'] + ball_velocity.x * dt
    ball_position['y'] = ball_position['y'] + ball_velocity.y * dt

    if float(ball_position['y']) <= 0:
        angle = degrees(atan(abs(float(ball_velocity.y) / float(ball_velocity.x))))
        
        t = format(t, '.3f')
        angle = format(angle, '.3f')
        distance = ball_position['x']

        print('distance:', distance)
        print('t:', t)
        print('angle:', angle)

        break

    t += dt

