import pygame as pg
from vector import Vector
from point import Point
from laser import Laser 
import os

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.filename = "highscores.txt"
        if os.path.isfile(self.filename):
            with open(self.filename, "r") as f:
                self.high_scores = [int(score.strip()) for score in f.readlines()]
                while len(self.high_scores) < 10:        
                    self.high_scores.append(0)
        else:
            self.high_scores = [0] * 10
            
        self.high_score = max(self.high_scores)

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_scores(self):
        with open(self.filename, "w") as f:
            for high_score in self.high_scores:
                f.write(str(high_score) + "\n")

    def update_high_scores(self, new_score):
        self.high_scores.append(new_score)
        self.high_scores = sorted(self.high_scores, reverse=True)[:10]  # Keep only the top 10 scores
        self.high_score = self.high_scores[0]  # Update the highest score

        # Save updated high scores to file
        self.save_high_scores()