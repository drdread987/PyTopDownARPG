import objects.objectHandler
import objects.Player.player
import objects.blockable.barrier as barrier
import objects.Units.slime as slime
import pygame
import os


class CharacterCreation(objects.objectHandler.Room):

    def __init__(self, drawing_board):
        super().__init__(drawing_board)

        self.background = self.image_loader.load_image("res/Background_green.png")

        self.width = 2560
        self.height = 1600

        self.scene_key = {(0, 0, 0): ["DOODAD", barrier.GrassSideBlock, None],
                          (0, 0, 3): ["DOODAD", barrier.GrassBottomBlock, None],
                          (0, 0, 8): ["DOODAD", barrier.GrassBottomShortBlock, None],
                          (0, 255, 0): ["UNIT", slime.Slime, None]}
        self.scene_image = self.image_loader.load_image("res/Scenes/scene1.png")

        self.add_unit(objects.Player.player.Player(400, 800, "????", self.image_loader))

        self.load_scene()

    def next_room(self):
        return super().next_room()

    def set_next_room(self, room):
        super().set_next_room(room)

    def end_room(self):
        super().end_room()

    def player_died(self, player):
        super().player_died(player)

        player.alive = True
        player.x = 400
        player.y = 400
        player.currentHealth = player.maxHealth
