import objects.objectHandler
import objects.Player.player
import objects.Rooms.MainMenu
import objects.blockable.barrier as barrier
import objects.Units.slime as slime
import objects.Units.green_bee as bee
import objects.Units.jumping_spider as spider
import objects.Units.first_boss as fb
import objects.Units.unit_spells.heart as heart
import objects.Units.unit_spells.buff_stats as buff
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
                          (0, 0, 8): ["DOODAD", barrier.GrassBottomShortBlock, None]}
        self.monsters = {0: [[slime.Slime, 832, 1376, []], [slime.Slime, 992, 1344, []],
                             [slime.Slime, 1280, 1408, []], [slime.Slime, 1472, 1376, []]],
                         1: [[slime.Slime, 832, 1376, []], [slime.Slime, 992, 1344, []],
                             [bee.GreenBee, 1280, 800, []], [bee.GreenBee, 1472, 800, []]],
                         2: [[slime.Slime, 832, 1376, []], [slime.Slime, 992, 1344, []],
                             [bee.GreenBee, 1280, 800, []], [bee.GreenBee, 1472, 800, []],
                             [spider.JumpingSpider, 1280, 1408, []], [spider.JumpingSpider, 1472, 1376, []]],
                         3: [[fb.FirstBoss, 1500, 1350, []]]
                         }
        self.scene_image = self.image_loader.load_image("res/Scenes/scene1.png")

        self.add_unit(objects.Player.player.Player(400, 800, "????", self.image_loader))
        self.load_scene()
        self.spawn_monsters()

    def frame_handle(self):
        super().frame_handle()
        found = False
        for unit in self.Units:
            if unit[0].enemy:
                found = True
                break

        if not found:
            self.level += 1
            if self.difficulty_waiting >= self.max_difficulty_waiting:
                self.add_spell(heart.Heart(1000, 800, 25))
            elif self.difficulty_waiting == self.max_difficulty_waiting-1:
                self.add_spell(buff.BuffStats(1050, 800))
            self.spawn_monsters()

    def next_room(self):
        return super().next_room()

    def set_next_room(self, room):
        super().set_next_room(room)

    def end_room(self):
        super().end_room()

    def load_scene(self):
        super().load_scene()

    def player_died(self, player):
        super().player_died(player)
        self.set_next_room(objects.Rooms.MainMenu.MainMenu(self.original_db))
        self.end_room()


