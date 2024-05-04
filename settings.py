import math

# ratio = 0.5625
WIDTH: int = 1200
HEIGHT: int = 675

RES: tuple[int, int] = WIDTH, HEIGHT
HALF_WIDTH: int = WIDTH // 2
HALF_HEIGHT: int = HEIGHT // 2
FPS: int = 0
DRAW_DEBUG: bool = False

PLAYER_POS: tuple[float, float] = 1.5, 5  # mini_map
PLAYER_ANGLE: float = 0
PLAYER_SPEED: float = 0.002
PLAYER_ROT_SPEED: float = 0.001
PLAYER_SIZE_SCALE: float = 60

MOUSE_SENSITIVITY: float = 0.0003
MOUSE_MAX_REL: int = 50
MOUSE_BORDER_LEFT: int = 100
MOUSE_BORDER_RIGHT: int = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR: tuple[int, int, int] = (40, 30, 30)

FOV: float = math.pi / 3
HALF_FOV: float = FOV / 2
NUM_RAYS: int = WIDTH // 2
HALF_NUM_RAYS: int = NUM_RAYS // 2
DELTA_ANGLE: float = FOV / NUM_RAYS
MAX_DEPTH: int = 20

SCREEN_DIST: float = HALF_WIDTH * math.tan(HALF_FOV)
SCALE: int = WIDTH // NUM_RAYS

TEXTURE_SIZE: int = 256
HALF_TEXTURE_SIZE: int = TEXTURE_SIZE // 2
