import random
import pygame
from Vector import Vector
import Constants
from Direction import Direction
from SnakeGame import SnakeGame

SCREEN_SIZE: Vector = Vector.from_axis(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)
BOARD_SIZE: Vector = Vector.from_axis(Constants.BOARD_WIDTH, Constants.BOARD_HEIGHT)
CELL_SIZE: Vector = SCREEN_SIZE // BOARD_SIZE

KEYS_DIRECTIONS: dict[int, Direction] = {
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT,
}

DIRECTION_VECTORS: dict[Direction, Vector] = {
    Direction.UP: Vector.from_axis(0, -1),
    Direction.DOWN: Vector.from_axis(0, 1),
    Direction.LEFT: Vector.from_axis(-1, 0),
    Direction.RIGHT: Vector.from_axis(1, 0),
}

WEIGHTS: dict[str, float] = {
    "food_distance": 0.85,
    "blocked": 0.125,
    "random": 0.025,
}

def vector_to_rect(v: Vector) -> pygame.Rect:
    return pygame.Rect((
        v.x * CELL_SIZE.x,
        v.y * CELL_SIZE.y,
        CELL_SIZE.x,
        CELL_SIZE.y
    ))

def is_in_bounds(v: Vector) -> bool:
    return (v.x >= 0 and v.x < BOARD_SIZE.x and v.y >= 0 and v.y < BOARD_SIZE.y)

def is_blocked(v: Vector, dir: Direction, snake: list[Vector]) -> bool:
    vnext = v + DIRECTION_VECTORS[dir]
    return (not is_in_bounds(vnext) or vnext in snake)

def main():
    pygame.init()
    pygame.display.set_caption("sneik")
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_SIZE.x, SCREEN_SIZE.y))
    running: bool = True
    last_update: int = pygame.time.get_ticks()
    
    game: SnakeGame = SnakeGame()
    bot_on: bool = True

    while (running):
        time: int = pygame.time.get_ticks()
        if (time - last_update >= Constants.FRAME_MS):
            foundFood: bool = False

            if (game.head == game.food):
                foundFood = True
                print("Found food")
                game.create_food()
            
            if (bot_on):
                best_direction: Direction = Direction.RIGHT
                best_score: float = 0
                for d in Direction:
                    score: float = 0
                    food_distance: Vector = game.food - game.head
                    food_distance_s: float = food_distance.length() / BOARD_SIZE.length()
                    score += WEIGHTS["food_distance"] * food_distance_s

                    if (not is_blocked(game.head, d, game.body)):
                        score += WEIGHTS["blocked"]
                    
                    score += WEIGHTS["random"] * random.random() / food_distance.length()

                    print(d.name, round(score, 3), end = ", ")
                    if (score >= best_score):
                        best_score = score
                        best_direction = d
                print("")
                game.direction = DIRECTION_VECTORS[best_direction]

            game.move(foundFood)
            
            if (not is_in_bounds(game.head)):
                game.reset()
            for [index, part] in enumerate(game.body):
                if (game.head == part and
                    index != len(game.body) - 1
                ):
                    game.reset()
            
            screen.fill(Constants.BLACK)
            pygame.draw.rect(screen, Constants.RED, vector_to_rect(game.food))
            for part in (game.body):
                pygame.draw.rect(screen, Constants.GRAY, vector_to_rect(part))
            pygame.display.update()
            last_update = time

        pressed = pygame.key.get_pressed()

        for key in (KEYS_DIRECTIONS):
            if (bot_on):
                break
            if (pressed[key]):
                direction_key: Direction = KEYS_DIRECTIONS[key]
                game.direction = DIRECTION_VECTORS[direction_key]

        for event in (pygame.event.get()):
            if (event.type == pygame.QUIT):
                running = False
            if (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
                bot_on = not bot_on

    pygame.quit()

if (__name__ == "__main__"):
    main()