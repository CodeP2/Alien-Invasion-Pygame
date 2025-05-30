import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
    
    def screen_settings(self, full_screen=False):
        """Setting controling the game screen."""
        if full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.screen_width = self.screen.get_rect().width
            self.screen_height = self.screen.get_rect().height
            return self.screen
        else:
            return pygame.display.set_mode(
                                        (self.screen_width, self.screen_height))