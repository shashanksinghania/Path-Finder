import pygame

# Make a new window with pygame
WINDOW_WIDTH = 800
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

# Colors constants in RGB format
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


# Each spot on the graph is denoted by a cube object
class Cube:
    def __init__(self, row, col, width, total_rows):
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.row = row
        self.column = col
        self.width = width
        self.total_rows = total_rows

    # Setters and getters of cube class
    def is_visited(self):
        return self.color == RED

    def get_pos(self):
        return self.row, self.column

    def is_barrier(self):
        return self.color == BLACK

    def is_start_node(self):
        return self.color == ORANGE

    def is_unvisited(self):
        return self.color == GREEN

    def is_end_node(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_barrier(self):
        self.color = BLACK

    def make_start_node(self):
        self.color = ORANGE

    def visit(self):
        self.color = RED

    def unvisit(self):
        self.color = GREEN

    def make_end_node(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw_itself(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    # Checks and adds all possible neighbours if they are not barriers
    def update_neighbours(self, grid):
        self.neighbours = []
        # Check the spot underneath
        if self.row + 1 < self.total_rows and not grid[self.row + 1][self.column].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.column])
        # Checks the spot above
        if self.row > 0 and not grid[self.row - 1][self.column].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.column])
        # Checks the spot to the right
        if self.column + 1 < self.total_rows and not grid[self.row][self.column + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.column + 1])
        # Checks the spot to the left
        if self.column > 0 and not grid[self.row][self.column - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.column - 1])

    def __lt__(self):
        pass


def heuristic(pos1, pos2):
    # We are using the Manhattan distance to calc the heuristic
    x1, y1 = pos1
    x2, y2 = pos2

    return abs(x2 - x1) + abs(y2 - y1)


def make_grid(rows, grid_width):
    grid = []
    cube_width = grid_width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Cube(i, j, cube_width, rows)
            grid[i].append(spot)
    return grid


def draw_grid_lines(win, rows, win_width):
    cube_width = win_width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * cube_width), (win_width, i * cube_width))
        pygame.draw.line(win, GREY, (i * cube_width, 0), (i * cube_width, win_width))


def draw(win, grid, rows, win_width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw_itself(win)
    draw_grid_lines(win, rows, win_width)
    pygame.display.update()


def get_cube_clicked_pos(pos, rows, win_width):
    cube_width = win_width // rows
    x, y = pos

    # Get which row and column
    row = y // cube_width
    col = x // cube_width
    return row, col


def main(win, win_width):
    NUM_ROWS = 50
    grid = make_grid(NUM_ROWS, win_width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, NUM_ROWS, win_width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                # left btn pressed
                pos = pygame.mouse.get_pos()
                row, col = get_cube_clicked_pos(pos, NUM_ROWS, win_width)
                spot = grid[col][row]
                if not start and spot != end:
                    start = spot
                    start.make_start_node()
                elif not end and spot != start:
                    end = spot
                    end.make_end_node()
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                # right btn pressed
                pos = pygame.mouse.get_pos()
                row, col = get_cube_clicked_pos(pos, NUM_ROWS, win_width)
                spot = grid[col][row]
                if spot == start:
                    start = None
                if spot == end:
                    end = None
                spot.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    pass
    pygame.quit()


main(WIN, WINDOW_WIDTH)
