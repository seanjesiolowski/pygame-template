import sys

import pygame


class Game:
    """Main game class."""

    def __init__(self, width=800, height=600, fps=60):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.running = True
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.background_color = (30, 30, 30)

    def handle_events(self):
        """Handle user input and events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Update game state. Game logic here."""

        pass

    def draw(self):
        """Draw everything to the screen. Draw code here."""

        self.screen.fill(self.background_color)
        # Add draw code here
        pygame.display.flip()

    def run(self):
        """Run the main game loop."""

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        self.quit()

    @staticmethod
    def quit():
        """Quit the game."""

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
