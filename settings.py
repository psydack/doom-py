import math

RES = WIDTH, HEIGHT = 1600, 900
FPS: int = 0
DRAW_DEBUG: bool = True

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
