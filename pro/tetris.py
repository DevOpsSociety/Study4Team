import pygame
import random

# 화면 및 블록 설정
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# 색상 지정
BLACK = (0, 0, 0)
CYAN   = (0, 255, 255)     # I
YELLOW = (255, 255, 0)     # O
PURPLE = (128, 0, 128)     # T
GREEN  = (0, 255, 0)       # S
RED    = (255, 0, 0)       # Z
ORANGE = (255, 165, 0)     # L
BLUE   = (0, 0, 255)       # J

# (모양, 색) 튜플로 SHAPES 정의
SHAPES = [
    ([[1, 1, 1, 1]], CYAN),              # I
    ([[1, 1], [1, 1]], YELLOW),          # O
    ([[0, 1, 0], [1, 1, 1]], PURPLE),    # T
    ([[0, 1, 1], [1, 1, 0]], GREEN),     # S
    ([[1, 1, 0], [0, 1, 1]], RED),       # Z
    ([[1, 0, 0], [1, 1, 1]], ORANGE),    # L
    ([[0, 0, 1], [1, 1, 1]], BLUE),      # J
]

# 블록 클래스
class Block:
    def __init__(self):
        self.shape, self.color = random.choice(SHAPES)
        self.x = 3
        self.y = 0

    def draw(self, surface):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    block_x = (self.x + col_idx) * BLOCK_SIZE
                    block_y = (self.y + row_idx) * BLOCK_SIZE
                    rect = pygame.Rect(block_x, block_y, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(surface, (0, 0, 0), rect)
                    inner_rect = rect.inflate(-4, -4)
                    pygame.draw.rect(surface, self.color, inner_rect)

    def can_move(self, dx, dy, grid):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x = self.x + col_idx + dx
                    new_y = self.y + row_idx + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return False
                    if new_y >= 0 and grid[new_y][new_x]:
                        return False
        return True

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, direction, grid):
        if direction == 'left':
            rotated = list(zip(*self.shape[::-1]))[::-1]
        elif direction == 'right':
            rotated = list(zip(*self.shape[::-1]))
        else:
            return

        new_shape = [list(row) for row in rotated]
        old_shape = self.shape
        self.shape = new_shape
        if not self.can_move(0, 0, grid):
            self.shape = old_shape

    def lock_to_grid(self, grid):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    grid_y = self.y + row_idx
                    grid_x = self.x + col_idx
                    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
                        grid[grid_y][grid_x] = self.color

# 초기화 함수들
def create_grid():
    return [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def clear_lines(grid):
    new_grid = [row for row in grid if any(cell is None for cell in row)]
    lines_cleared = GRID_HEIGHT - len(new_grid)
    return [[None for _ in range(GRID_WIDTH)] for _ in range(lines_cleared)] + new_grid

def clone_block(block):
    new_block = Block()
    new_block.shape = [row[:] for row in block.shape]
    new_block.color = block.color
    new_block.x = 3
    new_block.y = 0
    return new_block

def hard_drop(block, grid):
    while block.can_move(0, 1, grid):
        block.move(0, 1)
    block.lock_to_grid(grid)

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris - Full Features")

grid = create_grid()
current_block = Block()
held_block = None
hold_used = False
running = True

def check_game_over(block, grid):
    return not block.can_move(0, 0, grid)

# 게임 루프
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if current_block.can_move(-1, 0, grid):
                    current_block.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                if current_block.can_move(1, 0, grid):
                    current_block.move(1, 0)
            elif event.key == pygame.K_z:
                current_block.rotate('left', grid)
            elif event.key == pygame.K_x:
                current_block.rotate('right', grid)
            elif event.key == pygame.K_SPACE:
                if not hold_used:
                    if held_block is None:
                        held_block = clone_block(current_block)
                        current_block = Block()
                    else:
                        current_block, held_block = clone_block(held_block), clone_block(current_block)
                        hold_used = True
            elif event.key == pygame.K_UP:
                hard_drop(current_block, grid)
                grid = clear_lines(grid)
                current_block = Block()
                hold_used = False
                if check_game_over(current_block, grid):
                    running = False

    if current_block.can_move(0, 1, grid):
        current_block.move(0, 1)
    else:
        current_block.lock_to_grid(grid)
        grid = clear_lines(grid)
        current_block = Block()
        hold_used = False
        if check_game_over(current_block, grid):
            running = False

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = grid[y][x]
            if color:
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, (0, 0, 0), rect)
                inner_rect = rect.inflate(-4, -4)
                pygame.draw.rect(screen, color, inner_rect)

    current_block.draw(screen)
    pygame.display.flip()
    clock.tick(5)

pygame.quit()