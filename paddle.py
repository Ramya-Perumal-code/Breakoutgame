# from turtle import Turtle
# PADDLE_PARTS = [(-60, -300), (-50, -300), (-40, -300), (-30, -300), (-20, -300), (-10, -300), (0, -300), (10, -300),
#                 (20, -300), (30, -300), (40, -300), (50, -300), (60, -300)]
#
# class Paddle(Turtle):
#     # def __init__(self):
#     #     super().__init__()
#     #     self.shape("square")
#     #     self.color("#00CCDD")
#     #     self.shapesize(stretch_wid=0.8, stretch_len=12)
#     #     self.penup()
#     #     self.goto(-30, -350)
#     def __init__(self):
#         super().__init__()
#         self.parts = []
#         self.create_parts()
#         self.right_lead = self.parts[len(PADDLE_PARTS) - 1]
#         self.left_lead = self.parts[0]
#
#     def create_parts(self):
#         """creates a part for all positions in PADDLE_PARTS, adds them to a list called parts to create a paddle """
#         for position in PADDLE_PARTS:
#             part = Turtle(shape="square")
#             part.color("white")
#             part.penup()
#             part.goto(position)
#             part.shapesize(stretch_wid=0.5)
#             self.parts.append(part)
#
#     def move_left(self):
#         """checks x position of right corner of paddle and hinders movement off the screen to right, if still in range,
#              moves all paddle parts 30 pixels to the right"""
#         """checks x position of left corner of paddle and hinders movement off the screen to right, if still in range,
#                moves all paddle parts 30 pixels to the left"""
#         if self.left_lead.xcor() < -580:
#             pass
#         else:
#             for part in self.parts:
#                 new_xcor = part.xcor() - 30
#                 part.goto(y=-300, x=new_xcor)
#
#
#     def move_right(self):
#         """checks x position of right corner of paddle and hinders movement off the screen to right, if still in range,
#                moves all paddle parts 30 pixels to the right"""
#         if self.right_lead.xcor() > 580:
#             pass
#         else:
#             for part in self.parts:
#                 new_xcor = part.xcor() + 30
#                 part.goto(y=-300, x=new_xcor)

from turtle import Turtle

MOVE_DIST = 70


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('light blue')
        self.shape('square')
        self.penup()
        self.shapesize(1, 12)
        self.goto(x=0, y=-435)

    # Avoid the paddle to go off-screen
    def wall_checker(self):
        while self.xcor() > 520:
            self.backward(0.1)

        while self.xcor() < -520:
            self.forward(0.1)

    def move_left(self):
        self.wall_checker()
        self.backward(MOVE_DIST)

    def move_right(self):
        self.wall_checker()
        self.forward(MOVE_DIST)