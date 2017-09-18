import configparser as c
import Settings

config = c.RawConfigParser()

def Read():
    config.read("Settings.cfg")
    Settings.Fullscreen = config.getboolean("ScreenInfo", "Fullscreen")
    if not Settings.Fullscreen:
        Settings.ScreenWidth = 1024
        Settings.ScreenHeight = 768
    else:
        Settings.ScreenWidth = config.getint("ScreenInfo", "ScreenWidth")
        Settings.ScreenHeight = config.getint("ScreenInfo", "ScreenHeight")

    Settings.Fullscreen = config.getboolean("ScreenInfo", "Fullscreen")
    Settings.FPS = config.getint("ScreenInfo", "FPS")
    Settings.Title = config.get("ScreenInfo", "Title")


def Write():
    file = open("Settings.cfg", "w")
    config.set("ScreenInfo", "ScreenWidth", Settings.ScreenWidth)
    config.set("ScreenInfo", "ScreenHeight", Settings.ScreenHeight)
    config.set("ScreenInfo", "Fullscreen", Settings.Fullscreen)
    config.set("ScreenInfo", "FPS", Settings.FPS)

    config.write(file)
    file.close()