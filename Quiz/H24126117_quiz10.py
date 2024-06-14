import os
import random
import msvcrt
import time

# 定義遊戲元素的字符
EMPTY_CELL = ' '
SNAKE_BODY = 'o'
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
OBSTACLE = '#'

# 定義箭頭鍵的鍵碼
KEY_UP = 72
KEY_DOWN = 80
KEY_LEFT = 75
KEY_RIGHT = 77

# 定義遊戲參數
WIDTH = 60  # 增加遊戲屏幕的寬度
HEIGHT = 20  # 固定遊戲屏幕的高度
SPECIAL_FOOD_PROBABILITY = 0.1
OBSTACLE_DENSITY = 0.05

# 初始化蛇的位置和方向
snake = [
    [HEIGHT // 2, WIDTH // 2],
    [HEIGHT // 2, (WIDTH // 2) - 1],
    [HEIGHT // 2, (WIDTH // 2) - 2]
]
snake_direction = KEY_RIGHT

# 生成食物的函數
def generate_food(exclude):
    while True:
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        if [y, x] not in exclude:
            return [y, x]

# 生成障礙物的函數
def generate_obstacles():
    obstacles = []
    total_cells = int(WIDTH * HEIGHT * OBSTACLE_DENSITY)
    remaining_cells = total_cells

    while remaining_cells > 0:
        obstacle_length = min(5, remaining_cells)
        remaining_cells -= obstacle_length

        if random.choice([True, False]):
            # 生成水平障礙物
            x = random.randint(0, WIDTH - obstacle_length)
            y = random.randint(0, HEIGHT - 1)
            new_obstacle = [[y, x + i] for i in range(obstacle_length)]
        else:
            # 生成垂直障礙物
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - obstacle_length)
            new_obstacle = [[y + i, x] for i in range(obstacle_length)]

        # 確保障礙物不與蛇或現有的障礙物重疊
        if not any(cell in snake for cell in new_obstacle) and not any(cell in obstacles for cell in new_obstacle):
            obstacles.extend(new_obstacle)

    return obstacles

# 初始化障礙物
obstacles = generate_obstacles()
# 初始化食物
food = generate_food(snake + obstacles)
special_food = None

# 初始化分數
score_normal = 0
score_special = 0

# 渲染遊戲屏幕的函數
def render_screen():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [y, x] in snake:
                print(SNAKE_BODY, end=' ')
            elif [y, x] == food:
                print(NORMAL_FOOD, end=' ')
            elif special_food and [y, x] == special_food:
                print(SPECIAL_FOOD, end=' ')
            elif [y, x] in obstacles:
                print(OBSTACLE, end=' ')
            else:
                print(EMPTY_CELL, end=' ')
        print()

# 主遊戲循環
while True:
    os.system('echo -e "\033[?25l"')
    
    
    print("\033[H", end='')

    # 渲染遊戲屏幕
    render_screen()

    # 檢查用戶輸入
    if msvcrt.kbhit():
        key = ord(msvcrt.getch())
        if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake_direction = key

    # 移動蛇
    head = snake[0].copy()
    if snake_direction == KEY_UP:
        head[0] -= 1
    elif snake_direction == KEY_DOWN:
        head[0] += 1
    elif snake_direction == KEY_LEFT:
        head[1] -= 1
    elif snake_direction == KEY_RIGHT:
        head[1] += 1

    # 繞過屏幕邊界
    head[0] = head[0] % HEIGHT
    head[1] = head[1] % WIDTH

    # 檢查遊戲結束條件
    if head in snake or head in obstacles:
        break

    snake.insert(0, head)

    # 檢查是否吃到普通食物
    if head == food:
        score_normal += 1
        food = generate_food(snake + obstacles)
    else:
        snake.pop()

    # 檢查是否吃到特殊食物
    if special_food and head == special_food:
        score_special += 1
        special_food = None
        if len(snake) > 1:
            snake.pop()
    elif random.random() < SPECIAL_FOOD_PROBABILITY:
        special_food = generate_food(snake + obstacles)

    # 延遲
    time.sleep(0.1)

# 顯示遊戲結束和分數
print("Game Over!")
print(f"Normal foods eaten: {score_normal}")
print(f"Special foods eaten: {score_special}")


os.system('echo -e "\033[?25h"')