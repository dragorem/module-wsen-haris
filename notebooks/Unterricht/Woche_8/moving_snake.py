WIDTH = 8
HEIGHT = 8

START_SNAKE = [
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
]

def display_snake(snake):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (i, j) in snake:
                print("⬛", end="")
            else:
                print("⬜", end="")
        print()


def move_snake(snake, movement):
    new_head = find_new_head(snake, movement)

    # if the new head is already in snake, we ate our tail
    if new_head in snake:
        return []
    
    return snake[1:] + [new_head]
    

def find_new_head(snake, movement):
    head_row, head_column = snake[-1]

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
        if answer in "asdw":
            return answer


def round(snake):
    movement = user_input()
    new_snake = move_snake(snake, movement)
    return new_snake


def game():
    snake = START_SNAKE

    while snake != []:
        display_snake(snake)
        snake = round(snake)

    print("GAME OVER!")

game()