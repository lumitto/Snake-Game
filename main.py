import turtle
from turtle import Screen

import pygame.mixer

from text import Scoreboard, Gameover, Text
import time
from snake import Snake
from food import Food
from pygame import mixer

# Constants
WIDTH = 600
HEIGHT = 600

TIME = 0.1  # A speed of happening on a screen. More -> slower. 0.21 is optimal.


# Empty main screen
def screen_setup():
    global screen
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)


# Menu session
add_continue = False

pygame.mixer.init()
death = mixer.Sound("sounds/negative_beeps-6008.mp3")
start = mixer.Sound("sounds/game-start-6104.mp3")
press_button = mixer.Sound("sounds/ping-82822.mp3")
eat = mixer.Sound("sounds/coin-collect-retro-8-bit-sound-effect-145251.mp3")
eat_10 = mixer.Sound("sounds/Gachi_-_Stony_74537159 Аудио Извлечено Аудио Извлечено.wav")


def menu():
    start.play()
    screen.clearscreen()
    screen_setup()

    def button_action(x, y):
        button_x_size = range(-30, 30)
        button_y_size_play = range(40 - shift, 65 - shift)
        button_y_size_exit = range(7 - shift, 32 - shift)

        if x in button_x_size and y in button_y_size_play:
            press_button.play()
            time.sleep(0.7)

            game()

        if x in button_x_size and y in button_y_size_exit:
            press_button.play()
            time.sleep(0.7)
            turtle.bye()
            exit()

    # Condition for menu loop
    menu_bool = True

    shift = 30
    # Snake Game text
    snake_game_text_y = 215
    snake_game_text = Text()
    snake_game_text.font_type = "System"
    snake_game_text.print_tx((0, snake_game_text_y), "Snake Game", 50)

    # Print the MENU text on the screen
    menu_text_y = 80 - shift
    menu_text = Text()
    menu_text.print_tx((0, menu_text_y), "MENU", 24)

    # Play game text
    play_text_y = 45 - shift
    play = "Play"
    play_text = Text()
    play_text.print_tx((0, play_text_y), play, 16)

    # Exit text
    exit_text = Text()
    exit_text_y = 10 - shift
    exit_text.print_tx((0, exit_text_y), "Exit", 16)

    screen.listen()

    screen.onclick(button_action)
    while menu_bool:
        screen.update()


def game():
    global add_continue
    add_continue = True

    screen.clearscreen()
    screen_setup()

    def game_over():
        death.play()
        screen.clearscreen()
        screen_setup()
        game_over_text = Gameover()
        replay = Gameover()
        from_go_to_menu = Text()
        game_over_text.refresh("GAME OVER.", 0, 0, 18)
        replay.refresh("To play again press 'K'", 0, -20, 10)
        from_go_to_menu.print_tx((0, -43), "Press 'M' to menu", 10)
        screen.onkey(game, "k")
        global add_continue
        add_continue = False
        screen.onkey(menu, "m")

    # Main part of code
    snake = Snake()
    food = Food()
    score_text = Scoreboard()
    to_menu = Text()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(menu, "m")

    score = 0
    game_is_on = True
    to_menu.print_tx((-240, 280), "Press 'M' to menu.", 8)
    while game_is_on:
        screen.update()
        time.sleep(TIME)
        snake.move_the_snake()

        # Collision with food
        if snake.head.distance(food) < 15:
            score += 1
            if score % 10 == 0:
                eat_10.play()
            else:
                eat.play()
            snake.extend()
            food.refresh()

        # Collision with wall
        if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 305 or snake.head.ycor() < -295:
            # Lose
            game_is_on = False
            game_over()

        # Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                # Lose
                game_is_on = False
                game_over()

        score_text.clear()
        score_text.refresh(score)


# Main part of code
screen_setup()
menu()
