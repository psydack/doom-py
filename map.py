import pygame as pg
from settings import DRAW_DEBUG

_ = 0

mini_map: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [1, _, 2, _, _, _, _, 4, _, _, 5, _, _, _, _, 3],
    [1, _, _, _, _, _, _, 4, _, 5, _, _, _, _, _, 4],
    [1, _, _, _, 2, 2, 3, 3, _, 5, 2, 2, 2, _, _, 5],
    [1, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 3, 3, _, _, _, _, 1, _, _, _, _, _, _, _, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
]


class Map:
    def __init__(self, game) -> None:
        self.game = game
        self.mini_map: list[list[int]] = mini_map
        self.world_map: dict = {}
        self.get_map()

    def get_map(self) -> None:
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self) -> None:
        if DRAW_DEBUG:
            self.draw_debug()

    def draw_debug(self) -> None:
        [pg.draw.rect(self.game.screen,
                      'darkgray',
                      (pos[0] * 100, pos[1] * 100, 100, 100),
                      2)
         for pos in self.world_map]
