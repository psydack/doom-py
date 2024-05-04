import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self, game)  -> None:
        self.game = game

    def ray_cast(self) -> float:
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            x_hor, y_hor, depth_hor = self.calculate_horizontals(
                cos_a, sin_a, self.game.player.pos, self.game.player.map_pos, self.game.map.world_map)

            x_vert, y_vert, depth_vert = self.calculate_verticals(
                cos_a, sin_a, self.game.player.pos, self.game.player.map_pos, self.game.map.world_map)

            ray_angle += DELTA_ANGLE

            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            if DRAW_DEBUG:
                self.draw_debug(depth, cos_a, sin_a)

            # remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)

            # projection
            proj_height: float = SCREEN_DIST / (depth + 0.0001)

            # draw wall
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.game.screen, color,
                         (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

    def update(self) -> None:
        self.ray_cast()

    def draw_debug(self, depth: float, cos_a: float, sin_a: float) -> None:
        ox, oy = self.game.player.pos
        pg.draw.line(self.game.screen,
                     'yellow',
                     (100 * ox, 100 * oy),
                     (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a),
                     2)

    def calculate_horizontals(self, cos_a: float, sin_a: float, pos: [float, float], map_pos: [int, int], world_map: dict)\
            -> tuple[float, float, float]:
        ox, oy = pos
        _, y_map = map_pos

        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a
        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor in world_map:
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        return x_hor, y_hor, depth_hor

    def calculate_verticals(self, cos_a: float, sin_a: float, pos: [float, float], map_pos: [int, int], world_map: dict)\
            -> tuple[float, float, float]:
        ox, oy = pos
        x_map, _ = map_pos

        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a
        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert in world_map:
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        return x_vert, y_vert, depth_vert
