import objects.Player.pclasses.base
import objects.Player.pspells.blaze
import objects.Player.pspells.fireball
import objects.Player.pspells.blaze_spell
import objects.Player.pspells.flame_dash
import objects.Player.pspells.ignite
import objects.Player.pspells.meteor


class Fire(objects.Player.pclasses.base.BaseClass):

    def __init__(self):
        super().__init__()

        self.resource_name = "Blaze"
        self.resource_max = 5

        self.fortitudeMultiplier = 5

        self.ability_one = objects.Player.pspells.fireball.Fireball()
        self.ability_two = objects.Player.pspells.flame_dash.FlameDash()
        self.ability_three = objects.Player.pspells.ignite.Ignite()
        self.ability_four = objects.Player.pspells.meteor.Meteor()
        self.ability_expertise = objects.Player.pspells.blaze.Blaze()

    def stat_change(self, player, stats):
        super().stat_change(player, stats)

        self.resource_max = 5 + int(stats["resource_control"]/5)

    def step(self, obj_list):
        super().step(obj_list)
        self.resource = 0
        for spell in obj_list.Spells:
            if isinstance(spell[0], objects.Player.pspells.blaze_spell.BlazeSpell):
                self.resource += 1
        if self.resource > self.resource_max:
            self.resource = self.resource_max

    def cast_ability(self, key, stats, obj_handler, x, y, direction):
        super().cast_ability(key, stats, obj_handler, x, y, direction)

        if key == 49 and self.ability_one is not None and self.ability_one.cooldown == 0:
            if self.resource == 0:
                self.ability_one.cast_ability(obj_handler, stats, x, y, direction, self.resource)
            else:
                total_height = 30 * self.resource
                tracking_height = 0
                while tracking_height <= total_height:
                    self.ability_one.cast_ability(obj_handler, stats, x, y - (total_height/2) + tracking_height,
                                                  direction, self.resource)
                    tracking_height += 30
        if key == 50 and self.ability_two is not None and self.ability_two.cooldown == 0:
            self.ability_two.cast_ability(obj_handler, stats, x, y, direction, self.resource)

        if key == 52 and self.ability_four is not None and self.ability_four.cooldown == 0:
            self.ability_four.cast_ability(obj_handler, stats, x, y, direction, self.resource)


