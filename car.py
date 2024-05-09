import pygame as pg


class Car(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, position: list):
        super().__init__()
        self.image: pg.Surface = image
        self.tire_type: int = 1  # 0=soft 1=medium 2=hard
        self.position: list = position
        self.rotation: float = 0.0  # 0-359

        self.acceleration: float = 0
        self.max_acceleration: float = 0.05
        self.min_acceleration: float = -0.1
        self.velocity: float = 0.0
        self.max_velocity: float = 20.0
        self.max_backwards_velocity = -3.0
        self.rotation_speed: float = 0.0
        self.max_rotation_speed: float = 2.0

    def render(self, screen: pg.Surface):
        rotated_model = pg.transform.rotate(self.image, self.rotation)
        screen.blit(rotated_model, rotated_model.get_rect(center=self.position))
