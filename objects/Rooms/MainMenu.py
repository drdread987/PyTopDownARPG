import objects.objectHandler
import pygame
import objects.MenuItems.Selectables
import objects.Rooms.CharacterCreation


class MainMenu(objects.objectHandler.Room):

    def __init__(self, drawing_board):
        super().__init__(drawing_board)

        self.background = pygame.image.load("res/background.png")

        self.add_doodad(objects.MenuItems.Selectables.Quit(400, 600))
        self.add_doodad(objects.MenuItems.Selectables.NewGame(400, 200))

    def set_next_room(self, room):
        super().set_next_room(room)

        if room == "NG":
            self.poss_next_room = objects.Rooms.CharacterCreation.CharacterCreation(self.db)


