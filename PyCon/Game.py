import pygame
import sys
import PyCon

# SETTINGS
# How big should the Window be???
ScreenWidth = 1024
ScreenHeight = 768
ScreenSize = (ScreenWidth, ScreenHeight)
# How fast should the Game run?
FPS = 60


class Game:
    # Initialise The Game
    def __init__(self):
        # Initialise Pygame and the Sound Mixer
        pygame.init()
        # Generate a Screen to Display stuff
        self.screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)
        # Initialise the Clock to limit the Gamespeed
        self.clock = pygame.time.Clock()
        # Is the Game running
        self.running = True
        # Initialise the CMD Console
        self.console = PyCon.PyCon(self.screen,
                                   (0, 0, ScreenWidth, 200),
                                   functions={"fps": self.get_fps,
                                              "size": self.get_screen_dimensions,
                                              "add": self.add,
                                              "draw": self.draw,
                                              "shutdown": self.shutdown
                                              },
                                   key_calls={},
                                   vari={"A": 100, "B": 200, "C": 300},
                                   syntax={}
                                   )

    # The Whole Game
    # Does it need anything else?
    def run(self):
        # THE GAMELOOP
        while self.running:
            self.clock.tick(FPS)
            eventlist = pygame.event.get()
            self.screen.fill((255, 255, 255))
            self.console.process_input(eventlist)
            self.events(eventlist)
            self.console.draw()
            pygame.display.flip()
        # Close the Game
        self.console.write_history_to_file()
        pygame.quit()
        sys.exit()

    # The Events, like Key pressed and stuff
    def events(self, eventlist):
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.console.set_active()
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    # Test Functions for the communication with the console!
    def get_fps(self):
        """ Shows the FPS """
        return self.clock.get_fps()

    def get_screen_dimensions(self):
        """ Shows Window Resolution"""
        return ScreenSize

    def shutdown(self):
        """CAVE: Shuts the Game Down!!!"""
        self.running = False

    def add(self, a, b):
        """Simple add Function "add a b "
        """
        return a + b

    def draw(self, a, b, c):
        """ Simple draw circle Function "draw 400 400 100" """
        return pygame.draw.circle(pygame.display.get_surface(),(0,0,255),(a,b), c, 1)

if __name__ == "__main__":
    game = Game()
    game.run()
