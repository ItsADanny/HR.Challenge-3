import pygame as pg
import math

from car import Car


class Game:
    def __init__(self, width, height, title):
        # PyGame initialization
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        # pg.display.set_icon(pg.image.load("res/icon.png"))

        self.player = Car(pg.transform.scale(pg.image.load("res/textures/car_merc.png"), (60, 21)).convert_alpha(),
                          [600, 300])
        self.computer = Car(pg.transform.scale(pg.image.load("res/textures/car_alfa.png"), (60, 21)).convert_alpha(),
                            [500, 200])

        self.a_down = False
        self.d_down = False
        self.w_down = False
        self.s_down = False

        # Game logic variables
        self.window_width = width
        self.window_height = height
        self.state_stack = []

        self.logo = pg.image.load("res/textures/logo.png")
        self.logo_small = pg.transform.scale(self.logo, [175, 175])

        self.font_200 = pg.font.Font("res/fonts/F1-regular.ttf", 200)
        self.font_100 = pg.font.Font("res/fonts/F1-regular.ttf", 100)
        self.font_50 = pg.font.Font("res/fonts/F1-regular.ttf", 50)
        self.font_40 = pg.font.Font("res/fonts/F1-regular.ttf", 40)
        self.font_24 = pg.font.Font("res/fonts/F1-regular.ttf", 25)
        self.font_12 = pg.font.Font("res/fonts/F1-regular.ttf", 12)

        self.bg_color = (157, 206, 226)
        self.color_black = (0, 0, 0)
        self.color_gray = (30, 30, 30)
        self.color_dark_grey = (67, 69, 74)
        self.color_red = (255, 0, 0)
        self.color_white = (255, 255, 255)
        self.color_green = (0, 136, 0)
        self.color_orange = (255, 140, 90)
        self.color_yellow = (255, 222, 89)
        self.color_yellowish_green = (201, 219, 0)

        self.title_text = self.font_100.render("acing", False, self.color_black).convert()
        self.credit_text = self.font_24.render("Game by Joshua (1092067) and Danny (1091749)", False,
                                               self.color_white).convert()

        self.click_sound = pg.mixer.Sound("res/sfx/click.wav")

        self.clock = pg.time.Clock()
        self.fps = 60

    def start(self):
        play_button = pg.Rect((265, 375), (750, 100))
        quit_button = pg.Rect((265, 500), (750, 100))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(pg.mouse.get_pos()):
                        pg.quit()
                        exit(0)
                    elif play_button.collidepoint(pg.mouse.get_pos()):
                        # Go to main game loop
                        self.state_stack.append("GAME")
                        pg.mixer.Sound.play(self.click_sound)
                        self.game()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit(0)
                    else:  # Any key pressed except escape
                        # Go to main game loop
                        self.state_stack.append("GAME")
                        pg.mixer.Sound.play(self.click_sound)
                        self.game()

            # Render
            self.screen.fill(self.bg_color)

            # Grass background
            green_background = pg.Rect((0, 400), (self.screen.get_width(), 400))
            pg.draw.rect(self.screen, self.color_green, green_background)

            # Road
            road_background = pg.Rect((340, 400), (600, 400))
            pg.draw.rect(self.screen, self.color_black, road_background)
            # Road side - Left
            pg.draw.polygon(self.screen, self.color_black, ((340, 400), (340, 720), (250, 720)))
            # Road side - Right
            pg.draw.polygon(self.screen, self.color_black, ((940, 400), (940, 720), (1035, 720)))
            # Road side wall - left
            pg.draw.polygon(self.screen, self.color_red, ((340, 400), (250, 720), (210, 720), (300, 400)))
            # Road side wall - right
            pg.draw.polygon(self.screen, self.color_red, ((940, 400), (1035, 720), (1075, 720), (980, 400)))

            # Play button and text
            pg.draw.rect(self.screen, self.color_dark_grey, play_button, border_radius=15)
            if play_button.collidepoint(pg.mouse.get_pos()):
                play_text = self.font_50.render("Play", False, self.color_red).convert()
            else:
                play_text = self.font_50.render("Play", False, self.color_white).convert()
            self.screen.blit(play_text, play_text.get_rect(center=(play_button.centerx, play_button.centery)))
            # Quit button and text
            pg.draw.rect(self.screen, self.color_dark_grey, quit_button, border_radius=15)
            if quit_button.collidepoint(pg.mouse.get_pos()):
                quit_text = self.font_50.render("Quit", False, self.color_red).convert()
            else:
                quit_text = self.font_50.render("Quit", False, self.color_white).convert()
            self.screen.blit(quit_text, quit_text.get_rect(center=(quit_button.centerx, quit_button.centery)))
            # Logo
            self.screen.blit(self.logo_small, self.logo_small.get_rect(center=((self.window_width / 2) - 155, 92)))
            # Title text
            self.screen.blit(self.title_text, (540, 70))
            # Credit text
            self.screen.blit(self.credit_text, (300, 650))
            # PyGame Render
            pg.display.update()
            self.clock.tick(self.fps)

    def pause(self):
        paused_text = self.font_50.render("Paused", False, self.color_black).convert()
        return_button = pg.Rect((80, 500), (250, 100))
        quit_button = pg.Rect((1000, 500), (200, 100))

        while self.state_stack[-1] == "PAUSE":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(pg.mouse.get_pos()):
                        pg.quit()
                        exit(0)
                    elif return_button.collidepoint(pg.mouse.get_pos()):
                        # Go back to previous state
                        self.state_stack.pop()
                        pg.mixer.Sound.play(self.click_sound)
                        break
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        # Go back to previous state
                        self.state_stack.pop()
                        pg.mixer.Sound.play(self.click_sound)
                        break

            # Update

            # Render
            self.screen.fill(self.bg_color)

            # Grass background
            green_background = pg.Rect((0, 400), (self.screen.get_width(), 400))
            pg.draw.rect(self.screen, self.color_green, green_background)

            # Road
            road_background = pg.Rect((340, 400), (600, 400))
            pg.draw.rect(self.screen, self.color_black, road_background)
            # Road side - Left
            pg.draw.polygon(self.screen, self.color_black, ((340, 400), (340, 720), (250, 720)))
            # Road side - Right
            pg.draw.polygon(self.screen, self.color_black, ((940, 400), (940, 720), (1035, 720)))
            # Road side wall - left
            pg.draw.polygon(self.screen, self.color_red, ((340, 400), (250, 720), (210, 720), (300, 400)))
            # Road side wall - right
            pg.draw.polygon(self.screen, self.color_red, ((940, 400), (1035, 720), (1075, 720), (980, 400)))

            # Paused text
            self.screen.blit(paused_text, paused_text.get_rect(center=(self.window_width / 2, 200)))
            # Return button
            pg.draw.rect(self.screen, self.color_dark_grey, return_button, border_radius=15)
            if return_button.collidepoint(pg.mouse.get_pos()):
                return_text = self.font_50.render("Return", False, self.color_red).convert()
            else:
                return_text = self.font_50.render("Return", False, self.color_white).convert()
            self.screen.blit(return_text,
                             return_text.get_rect(center=(return_button.centerx, return_button.centery)))
            # Quit button
            pg.draw.rect(self.screen, self.color_dark_grey, quit_button, border_radius=15)
            if quit_button.collidepoint(pg.mouse.get_pos()):
                quit_text = self.font_50.render("Quit", False, self.color_red).convert()
            else:
                quit_text = self.font_50.render("Quit", False, self.color_white).convert()
            self.screen.blit(quit_text, quit_text.get_rect(center=(quit_button.centerx, quit_button.centery)))

            # Game icon
            # self.screen.blit(self.logo,
            # self.logo.get_rect(center=(self.window_width / 2, self.window_height / 2)))
            # Logo
            self.screen.blit(self.logo_small, self.logo_small.get_rect(center=((self.window_width / 2) - 155, 92)))
            # Title text
            self.screen.blit(self.title_text, (540, 70))
            # PyGame Render
            pg.display.update()
            self.clock.tick(self.fps)

    def game(self):
        ui_tire_health_20 = pg.Rect((15, 45), (40, 60))
        ui_tire_health_40 = pg.Rect((60, 45), (40, 60))
        ui_tire_health_60 = pg.Rect((105, 45), (40, 60))
        ui_tire_health_80 = pg.Rect((150, 45), (40, 60))
        ui_tire_health_100 = pg.Rect((195, 45), (40, 60))
        
        ui_current_tire_health_bg = pg.Rect((10, 40), (230, 70))
        ui_current_tire_bg = pg.Rect((250, 40), (230, 70))
        ui_current_speed_bg = pg.Rect((490, 40), (230, 70))
        ui_current_position_bg = pg.Rect((1040, 40), (230, 70))

        ui_current_tire_health_text = self.font_24.render("Tire Health", False, self.color_white).convert()
        ui_current_tire_text = self.font_24.render("Current Tire", False, self.color_white).convert()
        ui_current_speed_text = self.font_24.render("Speed (km/h)", False, self.color_white).convert()
        ui_current_position_text = self.font_24.render("Position", False, self.color_white).convert()

        ui_tire_soft = pg.transform.scale(pg.image.load("res/textures/tire_soft.png"), (64, 64))
        ui_tire_medium = pg.transform.scale(pg.image.load("res/textures/tire_medium.png"), (64, 64))
        ui_tire_hard = pg.transform.scale(pg.image.load("res/textures/tire_hard.png"), (64, 64))

        ui_tire_soft_text = self.font_24.render("S", False, (255, 0, 0)).convert()
        ui_tire_medium_text = self.font_24.render("M", False, (221, 179, 0)).convert()
        ui_tire_hard_text = self.font_24.render("H", False, (255, 107, 0)).convert()

        while self.state_stack[-1] == "GAME":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        # Show pause menu
                        self.state_stack.append("PAUSE")
                        self.pause()
                    elif event.key == pg.K_a:
                        self.a_down = True
                    elif event.key == pg.K_d:
                        self.d_down = True
                    elif event.key == pg.K_w:
                        self.w_down = True
                    elif event.key == pg.K_s:
                        self.s_down = True
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.a_down = False
                    elif event.key == pg.K_d:
                        self.d_down = False
                    elif event.key == pg.K_w:
                        self.w_down = False
                    elif event.key == pg.K_s:
                        self.s_down = False

            # Update
            if self.a_down:
                if self.player.velocity != 0.0:  # Can only turn when moving forwards or backwards
                    self.player.rotation = (self.player.rotation + self.player.rotation_speed) % 360
            elif self.d_down:
                if self.player.velocity != 0.0:  # Can only turn when moving forwards or backwards
                    if self.player.rotation - self.player.rotation_speed < 0:
                        self.player.rotation = 360.0 - self.player.rotation_speed
                    else:
                        self.player.rotation -= self.player.rotation_speed

            if self.w_down:  # Accelerate forwards when W is held down
                self.player.acceleration = self.player.max_acceleration
                self.player.velocity = min(self.player.velocity + self.player.acceleration, self.player.max_velocity)
            elif self.s_down:  # Accelerate backwards when S is held down
                self.player.acceleration = self.player.min_acceleration
                self.player.velocity = max(self.player.velocity + self.player.acceleration, self.player.max_backwards_velocity)
            else:  # Slow down when neither W nor S are held down
                if -0.1 < self.player.velocity < 0.1:
                    self.player.acceleration = 0.0
                    self.player.velocity = 0.0
                elif self.player.velocity > 0.1:  # If player is moving forwards
                    self.player.acceleration = self.player.min_acceleration
                else:  # If player is moving backwards
                    self.player.acceleration = self.player.max_acceleration
                self.player.velocity = self.player.velocity + self.player.acceleration
            self.player.position[0] -= self.player.velocity * math.cos(self.player.rotation / 180 * math.pi)
            self.player.position[1] += self.player.velocity * math.sin(self.player.rotation / 180 * math.pi)

            # The player cannot turn at full capacity when not going fast, the turning speed is dependent on the velocity
            self.player.rotation_speed = min(self.player.velocity * 0.5, self.player.max_rotation_speed)

            # Render
            self.screen.fill(self.bg_color)

            # Game map
            # Grass
            map_grass = pg.Rect((0, 120), (self.screen.get_width(), 600))
            pg.draw.rect(self.screen, self.color_green, map_grass)
            # Road
            map_road = pg.Rect((300, 270), (660, 430))
            pg.draw.rect(self.screen, self.color_gray, map_road)
            pg.draw.circle(self.screen, self.color_gray, (300, 480), 220)
            pg.draw.circle(self.screen, self.color_gray, (960, 480), 220)
            # Pit Lane
            map_pitlane = pg.Rect((400, 150), (450, 100))
            pg.draw.rect(self.screen, self.color_gray, map_pitlane)
            pg.draw.polygon(self.screen, self.color_gray, ((400, 150), (195, 300), (300, 400), (400, 250)))
            pg.draw.polygon(self.screen, self.color_gray, ((850, 150), (850, 250), (965, 400), (1065, 300)))
            # Pitstop location
            map_pitstop_white_bg = pg.Rect((575, 170), (100, 60))
            pg.draw.rect(self.screen, self.color_white, map_pitstop_white_bg)
            map_pitstop_grey_bg = pg.Rect((590, 170), (70, 80))
            pg.draw.rect(self.screen, self.color_gray, map_pitstop_grey_bg)
            map_pitstop_field = pg.Rect((585, 180), (80, 40))
            pg.draw.rect(self.screen, self.color_red, map_pitstop_field)
            pitstop_text = self.font_12.render("Pitstop", False, self.color_white).convert()
            self.screen.blit(pitstop_text, pitstop_text.get_rect(center=(map_pitstop_field.centerx, map_pitstop_field.centery)))
            # Center grass
            map_grass = pg.Rect((360, 410), (550, 140))
            pg.draw.rect(self.screen, self.color_green, map_grass)
            pg.draw.circle(self.screen, self.color_green, (360, 480), 70)
            pg.draw.circle(self.screen, self.color_green, (900, 480), 70)

            # Game UI Background
            ui_bg = pg.Rect((0, 0), (self.screen.get_width(), 120))
            pg.draw.rect(self.screen, self.color_dark_grey, ui_bg)
            # Game UI Splitter
            ui_splitter = pg.Rect((0, 120), (self.screen.get_width(), 10))
            pg.draw.rect(self.screen, self.color_gray, ui_splitter)

            # Game UI background for: Tire health, Current tire, Current Speed and Current position
            pg.draw.rect(self.screen, self.color_black, ui_current_tire_health_bg)
            pg.draw.rect(self.screen, self.color_black, ui_current_tire_bg)
            pg.draw.rect(self.screen, self.color_black, ui_current_speed_bg)
            pg.draw.rect(self.screen, self.color_black, ui_current_position_bg)

            # Game UI text for: Tire health, Current tire, Current Speed, Current position and Current tire
            self.screen.blit(ui_current_tire_health_text, (10, 10))
            self.screen.blit(ui_current_tire_text, (250, 10))
            self.screen.blit(ui_current_speed_text, (490, 10))
            self.screen.blit(ui_current_position_text, (1040, 10))

            if self.player.tire_type == 0:  # Soft tires
                self.screen.blit(ui_tire_soft, (335, 42))
                self.screen.blit(ui_tire_soft_text, (358, 61))
            elif self.player.tire_type == 1:  # Medium tires
                self.screen.blit(ui_tire_medium, (335, 42))
                self.screen.blit(ui_tire_medium_text, (353, 60))
            else:  # Hard tires
                self.screen.blit(ui_tire_hard, (335, 42))
                self.screen.blit(ui_tire_hard_text, (356, 61))

            # Game UI: Tire Health (Health bars)
            # 20%
            pg.draw.rect(self.screen, self.color_red, ui_tire_health_20)
            # 40%
            pg.draw.rect(self.screen, self.color_orange, ui_tire_health_40)
            # 60%
            pg.draw.rect(self.screen, self.color_yellow, ui_tire_health_60)
            # 80%
            pg.draw.rect(self.screen, self.color_yellowish_green, ui_tire_health_80)
            # 100%
            pg.draw.rect(self.screen, self.color_green, ui_tire_health_100)

            # The actual speed display
            self.screen.blit(self.font_40.render(f"{int(self.player.velocity * 20)}", False, self.color_white).convert(), (500, 56))

            # Draw the car
            self.player.render(self.screen)
            self.computer.render(self.screen)
            # print(f"{self.player_car.rotation} {math.cos(self.player_car.rotation / 180 * math.pi)}")
            # print(f"{self.player_car.rotation} {math.sin(self.player_car.rotation / 180 * math.pi)}")

            pg.display.update()
            self.clock.tick(self.fps)
