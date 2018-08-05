import objects.objectHandler
import objects.Player.player
import objects.blockable.barrier as barrier
import objects.Units.slime as slime
import pygame
import os
import sys


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
        self.difficulty = 0
        self.load_scene()

    def frame_handle(self):
        super().frame_handle()
        found = False
        for unit in self.Units:
            if unit[0].enemy:
                found = True
                break

        if not found:
            print("FINISHED LEVEL")
            self.difficulty += 1
            self.load_units()

    def next_room(self):
        return super().next_room()

    def set_next_room(self, room):
        super().set_next_room(room)

    def end_room(self):
        super().end_room()

    def load_scene(self):
        super().load_scene()

    def load_units(self):

        for y in range(int(self.height / 32)):
            for x in range(int(self.width / 32)):
                rgb = (self.scene_image.get_at((x, y)))[:3]
                try:
                    # print(self.scene_key[rgb])
                    key_value = self.scene_key[rgb]
                    if key_value[2] is None:
                        if key_value[0] == "UNIT":
                            self.add_unit(key_value[1](x * 32, y * 32))
                    else:
                        if key_value[0] == "UNIT":
                            self.add_unit(key_value[1](x * 32, y * 32, *key_value[2]))
                except KeyError:
                    if rgb != (255, 255, 255):
                        print("OBJECT NOT IN KEY")
                        print(rgb)
                        sys.exit()

        for unit in self.Units:
            if unit[0].enemy:
                unit[0].maxHealth *= self.difficulty
                unit[0].speed += int(self.difficulty/2)
                unit[0].currentHealth = unit[0].maxHealth

    def player_died(self, player):
        super().player_died(player)

        player.alive = True
        player.x = 400
        player.y = 400
        player.currentHealth = player.maxHealth


