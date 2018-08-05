import objects.Player.pspells.base
import objects.bases
import objects.Tools.collision as collide
from random import randint


class Meteor(objects.Player.pspells.base.Base):

    def __init__(self):
        super().__init__()

        self.description = "Calls down a meteor in front of you dealing damage to any targets hit"

        self.maxCooldown = 1200
        self.cooldown_colors = [181, 71, 0]

        self.base_damage = 15
        self.base_mini_damage = 3

    def cast_ability(self, obj_handler, stats, x, y, direction, *args):
        super().cast_ability(obj_handler, stats, x, y, direction, *args)
        if len(args) > 0:
            damage = self.base_damage + stats["aoe_damage"] + stats["damage"]
            mini_damage = self.base_damage + (stats["aoe_damage"]/2) + (stats["damage"]/2)
            minis = args[0]
            if direction == "RIGHT":
                x += 300
            else:
                x -= 300
            obj_handler.add_spell(MeteorSpell(x, 0, 5, damage))

            for n in range(0, minis):
                random_x = randint(-200, 400)
                random_weight = randint(4, 7)
                obj_handler.add_spell(MeteorSpell(x + random_x, 0, random_weight, mini_damage, mini=True))

            self.cooldown = self.maxCooldown * ((100 - stats["cooldown_recovery"]) / 100)

    def step(self):
        super().step()


class MeteorSpell(objects.bases.BaseSpell):
    def __init__(self, x, y, weight, damage, mini=False):
        super().__init__(x, y)
        self.damage = damage

        if mini:
            self.width = 50
            self.height = 86
            self.image = "res/meteor_mini.png"
            self.weight = weight
        else:
            self.width = 200
            self.height = 343
            self.image = "res/meteor.png"
            self.weight = 5

        self.hit_list = []

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        self.y += self.weight * 2
        if self.y > obj_handler.height:
            obj_handler.rem_spell(spell=self)

        for unit in obj_handler.Units:
            if unit[1] not in self.hit_list:
                if collide.rect_collide(self.x, self.width, self.y, self.height, unit[0].x,
                                        unit[0].width, unit[0].y, unit[0].height):
                    unit[0].take_damage(self.damage, "FIRE")
                    self.hit_list.append(unit[1])
