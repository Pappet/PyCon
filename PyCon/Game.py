import pygame
import sys
import Settings
import Config
import PyCon
import Color


class Game:
    # Initialise The Game
    def __init__(self):
        # Initialise Pygame and the Sound Mixer
        pygame.init()
        Config.Read()
        # Generate a Screen to Display stuff
        self.screen = pygame.display.set_mode((Settings.ScreenWidth, Settings.ScreenHeight), pygame.RESIZABLE)
        # Initialise the CMD Console
        self.console = PyCon.PyCon(self.screen,
                                   (0, 0, Settings.ScreenWidth, 200)
                                   )
        # Initialise the Clock to limit the Gamespeed
        self.clock = pygame.time.Clock()
        # Is the Game running
        self.running = True

    # Generates an new Game
    # Must reset Variables and stuff
    def new(self):
        self.run()

    # The Whole Game
    # Does it need anything else?
    def run(self):
        # THE GAMELOOP
        while self.running:
            eventlist = pygame.event.get()
            self.screen.fill(Color.White)
            self.clock.tick(Settings.FPS)
            self.console.process_input(eventlist)
            self.events(eventlist)
            self.update()
            self.console.draw()
            pygame.display.flip()
        # Close the Game
        self.close()

    def update(self):
        pass

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

    # Close The Game
    def close(self):
        print("Quit")
        Config.Write()
        # Shutdown Pygame and Sys
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
