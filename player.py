from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self) -> None:
        sin_a: float = math.sin(self.angle)
        cos_a: float = math.cos(self.angle)

        speed: float = PLAYER_SPEED * self.game.delta_time
        speed_sin: float = speed * sin_a
        speed_cos: float = speed * cos_a

        angle: float = self.angle

        dx, dy, angle = self.check_input(speed_sin, speed_cos, angle)
        dx, dy = self.check_wall_collision(dx, dy)
        self.x += dx
        self.y += dy
        self.angle = angle % math.tau

    def check_input(self, speed_sin: float, speed_cos: float, angle: float) -> tuple[float, float, float]:
        x: float = 0
        y: float = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            x += speed_cos
            y += speed_sin
        if keys[pg.K_s]:
            x += -speed_cos
            y += -speed_sin
        if keys[pg.K_w]:
            x += speed_sin
            y += -speed_cos
        if keys[pg.K_w]:
            x += -speed_sin
            y += speed_cos

        if keys[pg.K_LEFT]:
            angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            angle += PLAYER_ROT_SPEED * self.game.delta_time

        return x, y, angle

    def check_wall(self, x: int, y: int) -> tuple[int, int]:
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx: float, dy: float) -> tuple[float, float]:
        if not self.check_wall(int(self.x + dx), int(self.y)):
            dx = 0

        if not self.check_wall(int(self.x), int(self.y + dy)):
            dy = 0

        return dx, dy

    def draw(self) -> None:
        if DRAW_DEBUG:
            self.draw_debug()

    def draw_debug(self) -> None:
        x: float = self.x * 100
        y: float = self.y * 100

        pg.draw.circle(self.game.screen, 'green', (x, y), 15)

        pg.draw.line(self.game.screen,
                     'red',
                     (x, y),
                     (x + WIDTH * math.cos(self.angle), y + WIDTH * math.sin(self.angle)),
                     2)

    def update(self) -> None:
        self.movement()

    @property
    def pos(self) -> tuple[float, float]:
        return self.x, self.y

    @property
    def map_pos(self) -> tuple[int, int]:
        return int(self.x), int(self.y)
