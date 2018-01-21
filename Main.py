import pygame
import objects.Rooms.MainMenu

if __name__ == "__main__":

    size = 1200, 800
    pygame.init()
    screen = pygame.display.set_mode(size)
    room = objects.Rooms.MainMenu.MainMenu(screen)
    while room is not None:

        room.initiate_room()
        room = room.next_room()


