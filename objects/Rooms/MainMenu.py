import objects.objectHandler
import pygame
import objects.MenuItems.Selectables
import objects.Rooms.CharacterCreation


class MainMenu(objects.objectHandler.Room):

    def __init__(self, drawing_board):
        super().__init__(drawing_board)

        self.background = self.image_loader.load_image("res/background.jpg")

        self.add_doodad(objects.MenuItems.Selectables.ClickableFont(600, 400, 400, 100, "QUIT", "Arial", 80,
                                                                    self.quit_game, (0, 0, 255), (0, 0, 125)))
        self.add_doodad(objects.MenuItems.Selectables.ClickableFont(600, 200, 400, 100, "NEW GAME", "Arial", 80,
                                                                    self.new_game, (0, 0, 255), (0, 0, 125)))

    def set_next_room(self, room):
        super().set_next_room(room)

        if room == "NG":
            self.poss_next_room = objects.Rooms.CharacterCreation.CharacterCreation(self.original_db)

    def new_game(self):
        self.poss_next_room = objects.Rooms.CharacterCreation.CharacterCreation(self.original_db)
        self.end_room()




