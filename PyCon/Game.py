import pygame
import sys
import PyCon
import decimal
import re

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
        # Is the Game running
        self.running = True
        # Initialise Pygame and the Sound Mixer
        pygame.init()
        # Generate a Screen to Display stuff
        self.screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)
        # Initialise the Clock to limit the Gamespeed
        self.clock = pygame.time.Clock()
        # Initialise the CMD Console
        self.console = PyCon.PyCon(self.screen,
                                   (0, 0, ScreenWidth, 200),
                                   functions={"fps": self.get_fps,
                                              "size": self.get_screen_dimensions,
                                              "add": self.add,
                                              "draw": self.draw,
                                              "shutdown": self.shutdown,
                                              "pi": self.pi},
                                   key_calls={},
                                   vari={"A": 100, "B": 200, "C": 300},
                                   syntax={re_function: console_func}
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
        self.close()

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

    def close(self):
        # Close the Game
        self.console.write_history_to_file()
        pygame.quit()
        sys.exit()

    # Test Functions for the communication with the console!
    def get_fps(self):
        """ Shows the FPS! Use: fps"""
        return self.clock.get_fps()

    @staticmethod
    def get_screen_dimensions():
        """ Shows Window Resolution! Use: size"""
        return ScreenSize

    def shutdown(self):
        """CAVE: Shuts the Game Down!!! Use: shutdown"""
        self.running = False

    @staticmethod
    def add(a, b):
        """Simple add Function! Use: add a b"""
        return a + b

    @staticmethod
    def draw(a, b, c):
        """ Simple draw circle Function! Use: draw 400 400 100"""
        return pygame.draw.circle(pygame.display.get_surface(), (0, 0, 255), (a, b), c, 1)

    @staticmethod
    def pi():
        """
        Compute Pi to the current precision. Use: pi
        """
        decimal.getcontext().prec += 2  # extra digits for intermediate steps
        three = decimal.Decimal(3)  # substitute "three=3.0" for regular floats
        lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
        while s != lasts:
            lasts = s
            n, na = n + na, na + 8
            d, da = d + da, da + 32
            t = (t * n) / d
            s += t
        decimal.getcontext().prec -= 2
        return +s  # unary plus applies the new precision

if __name__ == "__main__":
    game = Game()
    game.run()

# # # # # # # # # # # # # # # # # #
# Another Example, this one       #
# lets you call functions like:   #
# name(arg1,arg2,...,argn)        #

re_function = re.compile(r'(?P<name>\S+)(?P<params>[\(].*[\)])')


def console_func(console, match):
    func = console.convert_token(match.group("name"))
    params = console.convert_token(match.group("params"))

    if not isinstance(params, tuple):
        params = [params]

    try:
        out = func(*params)
    except Exception as strerror:
        console.output(strerror)
    else:
        console.output(out)
