import turtle
import random

turtle.tracer(1, 0)

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 3



pos_list = []
stamp_list = []
food_pos = []
food_stamp = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos += SQUARE_SIZE
    my_pos = (x_pos, y_pos)
    snake.goto(x_pos, y_pos)
    pos_list.append(my_pos)
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction = UP
    print("Hey, you pressed up!")
def left():
    global direction
    direction = LEFT
    print("Hey, you pressed left!")
def down():
    global direction
    direction = DOWN
    print("Hey, you pressed down!")
def right():
    global direction
    direction = RIGHT
    print("Hey, you pressed right!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def make_food():
    global food_stamps, food_pos
    min_x = -int(SIZE_X/2.5/SQUARE_SIZE) + 1
    max_x = int(SIZE_X/2.5/SQUARE_SIZE) - 1
    min_y = -int(SIZE_Y/2.5/SQUARE_SIZE) - 1
    max_y = int(SIZE_Y/2.5/SQUARE_SIZE) + 1

    food_x = random.randint(min_x, max_x)*SQUARE_SIZE
    food_y = random.randint(min_y, max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    new_food = food.stamp()
    food_pos.append((food_x, food_y))
    food_stamps.append(new_food)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("Hey, you moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("Hey, you moved left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("Hey, you moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("Hey, you moved down!")

    my_pos = snake.pos()
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)
    pos_list.append(my_pos)


    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("Hey, you ate the food!")
        make_food()
        stamp_list.append(stamp_id)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("You fool! you hit the edge! GAME OVER!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("You fool! you hit the edge! GAME OVER!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You fool! you hit the edge! GAME OVER!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("You fool! you hit the edge! GAME OVER!")
        quit()
    turtle.ontimer(move_snake, TIME_STEP)

move_snake()

food = turtle.clone()
food.shape("triangle")
food.hideturtle()
food_pos = [(100, 100)]
food_stamps = []

for f in food_pos:
    food.goto(f[0], f[1])
    new_stamp = food.stamp()
    food_stamps.append(new_stamp)
