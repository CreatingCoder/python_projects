from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.color('white')
        
        self.shapesize(5, 1)
