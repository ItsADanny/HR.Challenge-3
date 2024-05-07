import pygame as pg


class Car:
    def __init__(self, model: pg.Surface, position: list):
        self.model: pg.Surface = model
        self.tire_type: int = 1  # 0=soft 1=medium 2=hard
        self.position: list = position
        self.rotation: float = 0.0  # 0-359

    def get_rotated_model(self):
        return pg.transform.rotate(self.model, self.rotation)

    def draw_to_screen(self, screen: pg.Surface):
        rotated_model = pg.transform.rotate(self.model, self.rotation)
        screen.blit(rotated_model, rotated_model.get_rect(center=self.position))
