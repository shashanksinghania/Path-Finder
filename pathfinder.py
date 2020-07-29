import pygame

WINDOW_WIDTH = 800
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

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

    def update_neighbours(self):
        pass

    def __lt__(self):
        pass
