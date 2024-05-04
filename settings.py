import math

WIDTH: int = 1600
HEIGHT: int = 900
RES: tuple[int, int] = WIDTH, HEIGHT
HALF_WIDTH: int = WIDTH // 2
HALF_HEIGHT: int = HEIGHT // 2
FPS: int = 0
DRAW_DEBUG: bool = False

PLAYER_POS: tuple[float, float] = 1.5, 5  # mini_map
PLAYER_ANGLE: float = 0
PLAYER_SPEED: float = 0.004
PLAYER_ROT_SPEED: float = 0.002

FOV: float = math.pi / 3
HALF_FOV: float = FOV / 2
NUM_RAYS: int = WIDTH // 2
HALF_NUM_RAYS: int = NUM_RAYS // 2
DELTA_ANGLE: float = FOV / NUM_RAYS
MAX_DEPTH: int = 20

SCREEN_DIST: float = HALF_WIDTH * math.tan(HALF_FOV)
SCALE: int = WIDTH // NUM_RAYS
