import objects.objectHandler
import pygame


class CharacterCreation(objects.objectHandler.Room):

    def __init__(self, drawing_board):
        super().__init__(drawing_board)

        self.background = pygame.image.load("res/Temp_background.png")

    def next_room(self):
        return super().next_room()

    def set_next_room(self, room):
        super().set_next_room(room)

    def end_room(self):
        super().end_room()
