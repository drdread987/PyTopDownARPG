import objects.bases
from random import randint
import objects.Tools.collision as collide


class BuffStats(objects.bases.BaseSpell):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.buffs = ["damage", "fortitude", "agility", "cooldown_recovery"]
        self.width = 25
        self.height = 25
        self.random_select = randint(0, len(self.buffs)-1)

        self.image = "res/" + self.buffs[self.random_select] + ".png"

        self.effect = 5
        self.gravity = True

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].stats[self.buffs[self.random_select]] += self.effect
            obj_handler.Units[0][0].stat_change()
            obj_handler.rem_spell(spell=self)
