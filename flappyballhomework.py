import pgzrun
import random

TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600
gravity = 2000

class Ball():
    def __init__(self, initialx, initialy, color, radius):
        self.x = initialx
        self.y = initialy
        self.vx = 200
        self.vy = 0
        self.radius = radius
        self.color = color
    
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)
        

ball1 = Ball(50,100,"green", 40)
ball2 = Ball(100,100, "red", 60)
ball3 = Ball(200,100, "blue", 90)


def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()
    ball3.draw()

def update(dt):
    uy = ball1.vy
    ball1.vy+=gravity * dt
    ball1.y+=(uy+ball1.vy) * 0.5 * dt
    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.vy = -ball1.vy * 0.9

    ball1.x += ball1.vx * dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = -ball1.vx

    uy = ball2.vy
    ball2.vy+=gravity * dt
    ball2.y+=(uy+ball2.vy) * 0.5 * dt
    if ball2.y > HEIGHT - ball2.radius:
        ball2.y = HEIGHT - ball2.radius
        ball2.vy = -ball2.vy * 0.9

    ball2.x += ball2.vx * dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
        ball2.vx = -ball2.vx
    
    uy = ball3.vy
    ball3.vy+=gravity * dt
    ball3.y+=(uy+ball3.vy) * 0.5 * dt
    if ball3.y > HEIGHT - ball3.radius:
        ball3.y = HEIGHT - ball3.radius
        ball3.vy = -ball3.vy * 0.9

    ball3.x += ball3.vx * dt
    if ball3.x > WIDTH - ball3.radius or ball3.x < ball3.radius:
        ball3.vx = -ball3.vx

    

def on_key_down(key):
    if key == keys.SPACE:
        ball1.vy = -500
        ball2.vy = -600
        ball3.vy = -1000



pgzrun.go()

