import pygame.font
from colors import GREEN, DARK_BLUE

class Button:
    def __init__(self, ai_game, msg, y_pos):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = DARK_BLUE
        self.text_color = GREEN
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.y = y_pos
        self.rect.center = (self.screen_rect.center[0], self.y)

        self._prep_msg(msg)

    def reset_message(self, msg="You forgot a message bozo"):
        self.msg = msg
        self._prep_msg(msg)

    def reset_height(self, y):
        self.y = y
        self.rect.center = (self.screen_rect.center[0], self.y)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)