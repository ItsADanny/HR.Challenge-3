import pygame as pg
import pygame.transform

from car import Car


class Game:
    def __init__(self, width, height, title):
        # PyGame initialization
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        # pg.display.set_icon(pg.image.load("res/icon.png"))

        self.car_1 = Car(pg.image.load("res/textures/car_merc.png").convert_alpha(), [200, 200])

        self.a_down = False
        self.d_down = False

        # Game logic variables
        self.window_width = width
        self.window_height = height
        self.state_stack = []

        self.logo = pg.image.load("res/textures/logo.png")

        self.font_200 = pg.font.Font("res/fonts/F1-regular.ttf", 200)
        self.font_100 = pg.font.Font("res/fonts/F1-regular.ttf", 100)
        self.font_50 = pg.font.Font("res/fonts/F1-regular.ttf", 50)
        self.font_40 = pg.font.Font("res/fonts/F1-regular.ttf", 40)
        self.font_24 = pg.font.Font("res/fonts/F1-regular.ttf", 25)

        self.bg_color = (157, 206, 226)
        self.color_black = (0, 0, 0)
        self.color_red = (255, 0, 0)
        self.color_white = (255, 255, 255)

        self.click_sound = pg.mixer.Sound("res/sfx/click.wav")

        self.clock = pg.time.Clock()
        self.fps = 60

    def start(self):
        play_button = pg.Rect((80, 500), (200, 100))
        quit_button = pg.Rect((1000, 500), (200, 100))

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
            # Play button and text
            pg.draw.rect(self.screen, self.color_black, play_button, border_radius=15)
            if play_button.collidepoint(pg.mouse.get_pos()):
                play_text = self.font_50.render("Play", False, self.color_red).convert()
            else:
                play_text = self.font_50.render("Play", False, self.color_white).convert()
            self.screen.blit(play_text, play_text.get_rect(center=(play_button.centerx, play_button.centery)))
            # Quit button and text
            pg.draw.rect(self.screen, self.color_black, quit_button, border_radius=15)
            if quit_button.collidepoint(pg.mouse.get_pos()):
                quit_text = self.font_50.render("Quit", False, self.color_red).convert()
            else:
                quit_text = self.font_50.render("Quit", False, self.color_white).convert()
            self.screen.blit(quit_text, quit_text.get_rect(center=(quit_button.centerx, quit_button.centery)))
            # Logo
            self.screen.blit(self.logo, self.logo.get_rect(center=(self.window_width / 2, 300)))
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
            # Paused text
            self.screen.blit(paused_text, paused_text.get_rect(center=(self.window_width / 2, 75)))
            # Return button
            pg.draw.rect(self.screen, self.color_black, return_button, border_radius=15)
            if return_button.collidepoint(pg.mouse.get_pos()):
                return_text = self.font_50.render("Return", False, self.color_red).convert()
            else:
                return_text = self.font_50.render("Return", False, self.color_white).convert()
            self.screen.blit(return_text,
                             return_text.get_rect(center=(return_button.centerx, return_button.centery)))
            # Quit button
            pg.draw.rect(self.screen, self.color_black, quit_button, border_radius=15)
            if quit_button.collidepoint(pg.mouse.get_pos()):
                quit_text = self.font_50.render("Quit", False, self.color_red).convert()
            else:
                quit_text = self.font_50.render("Quit", False, self.color_white).convert()
            self.screen.blit(quit_text, quit_text.get_rect(center=(quit_button.centerx, quit_button.centery)))

            # Game icon
            self.screen.blit(self.logo,
                             self.logo.get_rect(center=(self.window_width / 2, self.window_height / 2)))
            # PyGame Render
            pg.display.update()
            self.clock.tick(self.fps)

    def game(self):
        game_text = self.font_50.render("Game", False, self.color_black).convert()
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
                        self.car_1.model = pygame.transform.rotate(self.car_1.model, self.car_1.rotation)
                        self.a_down = True
                    elif event.key == pg.K_d:
                        self.car_1.model = pygame.transform.rotate(self.car_1.model, self.car_1.rotation)
                        self.d_down = True
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.a_down = False
                    elif event.key == pg.K_d:
                        self.d_down = False

            # Update
            if self.d_down:
                self.car_1.rotation = (self.car_1.rotation + 1) % 360
            elif self.a_down:
                if self.car_1.rotation - 1 < 0:
                    self.car_1.rotation = 359
                else:
                    self.car_1.rotation -= 1

            # Render
            print(self.car_1.rotation)
            self.screen.fill(self.bg_color)
            self.screen.blit(game_text, game_text.get_rect(center=(self.window_width / 2, self.window_height / 2)))

            self.screen.blit(self.car_1.model, self.car_1.model.get_rect(center=self.car_1.position))

            pg.display.update()
            self.clock.tick(self.fps)
