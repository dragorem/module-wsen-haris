import random

WIDTH = 8
HEIGHT = 8

START_SNAKE = [
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
]

START_STATE = {
    "snake": START_SNAKE,
    "food": (3, 5)
}


def sample_new_food(snake):
    possible_positions = []

    for row in range(HEIGHT):
        for column in range(WIDTH):
            position = (row, column)
            if not position in snake:
                possible_positions.append(position)
    
    return random.choice(possible_positions)


def display(state):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (i, j) in state["snake"]:
                print("⬛", end="")
            elif (i, j) == state["food"]:
                print("🍔", end="")
            else:
                print("⬜", end="")
        print()


def move_snake(state, movement):
    snake = state["snake"]
    food = state["food"]
    new_head = find_new_head(snake, movement)

    # if the new head is already in snake, we ate our tail
    if new_head in snake:
        return {
            "snake": [],
            "food": food
        }
    
    if new_head == food:
        new_snake = snake + [new_head]  # snake grows by 1
        new_food = sample_new_food(new_snake)
        return {
            "snake": snake + [new_head],
            "food": new_food,
        }
    
    return {
        "snake": snake[1:] + [new_head], 
        "food": food
    }
    

def find_new_head(snake, movement):
    try:
        head_row, head_column = snake[-1]
    except:
        print(snake)
        raise
    # up
    if movement=="w":
        return (head_row - 1) % HEIGHT, head_column

    # down
    if movement=="s":
        return (head_row + 1) % HEIGHT, head_column
    
    # left
    if movement=="a":
        return head_row, (head_column - 1) % WIDTH
    
    # right
    if movement=="d":
        return head_row, (head_column + 1) % WIDTH


def user_input():
    while True:
        answer = input().lower()
        if answer in "asdw" and answer != "":
            return answer


def one_round(state):
    movement = user_input()
    new_state = move_snake(state, movement)
    return new_state


def game():
    state = START_STATE
    while state["snake"] != []:
        display(state)
        state = one_round(state)

    print("GAME OVER!")

game()