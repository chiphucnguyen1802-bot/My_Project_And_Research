import pygame
from time import sleep
from random import randint

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption('Snake AI Safe Demo')
running = True
GREEN = (0, 255, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

clock = pygame.time.Clock()

# Snake position: tail -> head
snakes = [[5,10]]
direction = "right"

# Spawn táo ở safe zone
apple = [randint(1,18), randint(1,18)]
font_small = pygame.font.SysFont('sans', 20)
font_big = pygame.font.SysFont('sans', 50)
score = 0
pausing = False

# ----- AI: đi gần táo nhưng kiểm tra an toàn -----
def safe_ai(head, apple, current_dir, body):
    hx, hy = head
    ax, ay = apple

    # Tạo danh sách hướng ưu tiên theo khoảng cách
    directions = []
    if abs(ax - hx) > abs(ay - hy):
        if ax > hx: directions.append("right")
        if ax < hx: directions.append("left")
        if ay > hy: directions.append("down")
        if ay < hy: directions.append("up")
    else:
        if ay > hy: directions.append("down")
        if ay < hy: directions.append("up")
        if ax > hx: directions.append("right")
        if ax < hx: directions.append("left")

    # Thêm các hướng còn lại nếu ưu tiên không đi được
    for d in ["up","down","left","right"]:
        if d not in directions:
            directions.append(d)

    # Kiểm tra từng hướng xem có an toàn không
    for d in directions:
        if d == "right" and current_dir != "left":
            nx, ny = hx+1, hy
        elif d == "left" and current_dir != "right":
            nx, ny = hx-1, hy
        elif d == "up" and current_dir != "down":
            nx, ny = hx, hy-1
        elif d == "down" and current_dir != "up":
            nx, ny = hx, hy+1
        else:
            continue

        # An toàn nếu trong lưới và không đụng thân
        if 0 <= nx <= 19 and 0 <= ny <= 19 and [nx, ny] not in body:
            return d

    # Fallback: giữ nguyên hướng
    return current_dir
# ------------------------------------------------------------

while running:
    clock.tick(60)
    screen.fill(BLACK)

    tail_x = snakes[0][0]
    tail_y = snakes[0][1]

    # --- CẬP NHẬT HƯỚNG BẰNG AI trước khi rắn di chuyển ---
    if not pausing:
        direction = safe_ai(snakes[-1], apple, direction, snakes)

    # Draw snake
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))

    # Draw apple
    pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

    # Snake move
    if not pausing:
        if direction == "right":
            snakes.append([snakes[-1][0]+1, snakes[-1][1]])
        if direction == "left":
            snakes.append([snakes[-1][0]-1, snakes[-1][1]])
        if direction == "up":
            snakes.append([snakes[-1][0], snakes[-1][1]-1])
        if direction == "down":
            snakes.append([snakes[-1][0], snakes[-1][1]+1])
        snakes.pop(0)

    # check eat apple
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0,[tail_x,tail_y])
        apple = [randint(1,18), randint(1,18)]
        score += 1

    # check crash with edge
    if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
        pausing = True

    # check crash with body
    for i in range(len(snakes)-1):
        if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
            pausing = True

    # Draw score
    score_txt = font_small.render("Score: " + str(score), True, WHITE)
    screen.blit(score_txt, (5,5))

    # Draw game over
    if pausing:
        game_over_txt = font_big.render("Game over, score: " + str(score), True, WHITE)
        press_space_txt = font_big.render("Press Space to continue", True, WHITE)
        screen.blit(game_over_txt, (50,200))
        screen.blit(press_space_txt, (50,300))

    sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pausing:
                pausing = False
                snakes = [[5,10]]
                direction = "right"
                apple = [randint(1,18), randint(1,18)]
                score = 0

    pygame.display.flip()

pygame.quit()
