# from turtle import Screen
# from brick import Brick
# from paddle import Paddle
# from ball import Ball
# import time
# import random
#
# screen = Screen()
# screen.setup(width=1200, height=800)
# screen.title("Breakout Game")
# screen.bgcolor("black")
# screen.tracer(0)
# paddle = Paddle()
# ball = Ball()
# colors = ["red", "orange", "Yellow", "green", "purple", "blue"]
# brick_list = []
#
# def create_bricks():
#     times = 0
#     current_pos = - 100
#     while times < 4:
#         for n in range(0, 11):
#             brick = Brick()
#             brick.color(random.choice(colors))
#             brick_list.append(brick)
#             brick.goto(x=-545+n*110, y=current_pos)
#             # print(f"brick's coord : {brick.xcor(), brick.ycor()}")
#         current_pos += 70
#         times += 1
#
#
#
# create_bricks()
# screen.listen()
# screen.onkey(key="Left", fun=paddle.move_left)
# screen.onkey(key="Right", fun=paddle.move_right)
#
#
# def is_collided(a, b):
#     distance = b.distance(a.pos())
#     radius_a = a.shapesize()[0] * 10
#     radius_b = b.shapesize()[0] * 10
#     return radius_a + radius_b >= distance
#
# game_is_on = True
# while game_is_on:
#     time.sleep(0.2)
#     ball.refresh()
#     # print(f"ball's coord :{ball.xcor(),ball.ycor()}")
#     # print(f"brick's coord : {brick.xcor(), brick.ycor()}")
#     # print(ball.distance(brick))
#
#     #Detect collision with bricks
#     for n in brick_list:
#     #     print(f"ball's coord :{ball.xcor(),ball.ycor()}")
#     #     print(f"brick's coord : {brick.xcor(), brick.ycor()}")
#     #     print(brick.brick_list)
#
#         if (ball.distance(n) < 50 and ball.xcor() > 580 or ball.distance(n) < 50 and ball.xcor() < -580
#                 or ball.distance(n) < 50 and ball.ycor() > 370 or ball.distance(n) < 50 and ball.xcor() > -370):
#             # print("Collision")
#             brick_list.remove(n)
#             n.reset()
#             ball.y_bounce()
#
#         # Detect collision with paddle
#         for part in paddle.parts:
#             if ball.distance(part) < 40 and ball.ycor() < -270:
#                 ball.y_bounce()
#                 break
#         if ball.xcor() < -580 or ball.xcor() > 580:
#             print(f"ball's coord when touch paddle:{ball.xcor(), ball.ycor()}")
#             print("ball touched the screen limit")
#             print(f"x_move: {ball.x_move}")
#             print(f"y_move: {ball.y_move}")
#             ball.x_bounce()
#         # print("collision")
#         # print(ball.distance(paddle))
#         # # ball.y_bounce()
#         # print(f"x_move :{ball.x_move}")
#         # print(f"y_move :{ball.y_move}")
#         #
#
#
#     screen.update()
#
# screen.exitonclick()
#
# # while game_on:
# #     time.sleep(ball.move_speed)
# #     screen.update()
# #     ball.refresh()
# #
# #     # Detect collision with wall
# #     if ball.ycor() > 280 or ball.ycor() < -280:
# #         ball.y_bounce()
# #
# #     #Detect collision with paddles
# #     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
# #         ball.x_bounce()
# #
# #     #Detect when the ball goes out of bounds i.e r paddle misses
# #     if ball.xcor() > 380:
# #         ball.reset_position()
# #         scoreboard.l_point()
# #
# #     # Detect when the ball goes out of bounds i.e r paddle misses
# #     if ball.xcor() < -380:
# #         ball.reset_position()
# #         scoreboard.r_point()
# #
# #         self.x_move = 10
# #         self.y_move = 10
# #         self.move_speed = 0.1
# #
# #
# #     def refresh(self):
# #         new_x = self.xcor() + self.x_move
# #         new_y = self.ycor() + self.y_move
# #
# #         self.goto(new_x, new_y)
# #
# #
# #     def y_bounce(self):
# #         self.y_move *= -1
# #
# #
# #     def x_bounce(self):
# #         self.x_move *= -1
# #         self.move_speed *= 0.9
# #
# #
# #     def reset_position(self):
# #         self.goto(0, 0)
# #         self.move_speed = 0.1
# #         self.x_bounce()

import turtle as tr
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from ui import UI
from brick_test import Bricks
import time

screen = tr.Screen()
screen.setup(width=1200, height=1000)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

ui = UI()
ui.header(game_on=False)

score = Scoreboard(lives=5)
bricks = Bricks()
bricks.create_bricks()
paddle = Paddle()
ball = Ball()

game_paused = True
playing_game = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


def play_again():
    screen.clear()
    exec(open("./main.py").read())


screen.listen()
screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)
screen.onkey(key='space', fun=pause_game)
screen.onkey(key='y', fun=play_again)


def check_collision_with_walls():
    global ball, score, playing_game, ui, game_paused

    # detect collision with left and right walls:
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    # detect collision with upper wall
    if ball.ycor() > 435:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    # detect collision with bottom wall
    if ball.ycor() < -440:
        ball.reset()
        score.decrease_lives()
        paddle.goto(0, -435)
        game_paused = True
        if score.lives == 0:
            score.reset()
            playing_game = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return


def check_collision_with_paddle():
    global ball, paddle
    # record x-axis coordinates of ball and paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    # check if ball's distance from paddle is less than width of paddle and ball
    if ball.distance(paddle) < 120 and ball.ycor() < -415:

        if paddle_x > 0:
            if ball_x > paddle_x:
                print(ball.x_move_dist)
                print(ball.y_move_dist)
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def check_collision_with_bricks():
    global ball, score, bricks

    for brick in bricks.all_bricks:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity < 1:
                brick.hideturtle()
                bricks.all_bricks.remove(brick)
            else:
                ball.bounce(x_bounce=False, y_bounce=True)


while playing_game:
    screen.update()
    ui.header(game_on=True)

    if not game_paused:

        time.sleep(0.01)
        ball.move()

        check_collision_with_walls()

        check_collision_with_paddle()

        check_collision_with_bricks()

        if len(bricks.all_bricks) == 0:
            ui.game_over(win=True)
            break

    else:
        ui.paused_status()

tr.mainloop()
