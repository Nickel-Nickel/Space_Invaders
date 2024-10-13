import pygame as pg
import os

class Highscores:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)
        self.highscores = self.load_high_scores()

    def load_high_scores(self):
        # Load the top 10 high scores from a file.
        filename = "highscores.txt"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                highscores = [int(score.strip()) for score in f.readlines()]
            highscores.sort(reverse=True)
            return highscores[:10]  # Return top 10 high scores
        return []

    def display(self):
        # Display the high scores on the screen.
        self.screen.fill(self.settings.bg_color)
        title = self.font.render("Top 10 High Scores", True, self.text_color)
        title_rect = title.get_rect(center=(self.screen_rect.centerx, 100))
        self.screen.blit(title, title_rect)
        self.highscores = self.load_high_scores()
        # Display each high score
        for i, score in enumerate(self.highscores, start=1):
            score_str = f"{i}. {score}"
            score_image = self.font.render(score_str, True, self.text_color)
            score_rect = score_image.get_rect(center=(self.screen_rect.centerx, 150 + i * 40))
            self.screen.blit(score_image, score_rect)

        # Update the screen
        #pg.display.flip()
