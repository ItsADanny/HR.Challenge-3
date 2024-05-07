import pygame as pg


class Car:
    def __init__(self, model: pg.Surface, position: list):
        self.model: pg.Surface = model
        self.tire_type: int = 1  # 0=soft 1=medium 2=hard
        self.position: list = position
        self.rotation: int = 0  # 0-359
