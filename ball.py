# from turtle import Turtle
#
#
# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.goto(0, -330)
#         self.x_move = 10
#         self.y_move = 10
#         self.move_speed = 0.1
#
#     def refresh(self):
#         new_x = self.xcor() + self.x_move
#         new_y = self.ycor() + self.y_move
#
#         self.goto(new_x, new_y)
#
#     def y_bounce(self):
#         if self.xcor() < 580:
#             self.y_move *= -1
#
#     def x_bounce(self):
#         self.x_move *= -1
#         self.y_move *= -1
#
#             # self.x_move *= -1
#         # self.move_speed *= 0.9

from turtle import Turtle

MOVE_DIST = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move_dist = MOVE_DIST
        self.y_move_dist = MOVE_DIST
        self.reset()

    def move(self):
        # move only 10 steps ahead, both vertically and horizontally.
        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            # reverse the horizontal direction
            self.x_move_dist *= -1

        if y_bounce:
            # reverse the vertical direction
            self.y_move_dist *= -1

    def reset(self):
        # ball should go to an initial position,
        self.goto(x=0, y=-415)
        self.y_move_dist = 10



