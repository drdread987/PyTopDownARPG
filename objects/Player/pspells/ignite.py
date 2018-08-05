import objects.Player.pspells.base
import objects.Player.pspells.blaze_spell


class Ignite(objects.Player.pspells.base.Base):

    def __init__(self):
        super().__init__()

        self.description = "Deals damage to every unit with a blaze on them (per blaze) and destroys the blaze"

        self.cooldown_colors = [255, 125, 0]
        self.maxCooldown = 1000

        self.base_damage = 10
        self.damage_per_blaze = 1

    def cast_ability(self, obj_handler, stats, x, y, direction, *args):
        super().cast_ability(obj_handler, stats, x, y, direction, *args)
        codes = {}
        rem_spells = []
        for s in obj_handler.Spells:
            if isinstance(s[0], objects.Player.pspells.blaze_spell.BlazeSpell):
                if s[0].tracking_number not in codes:
                    codes[s[0].tracking_number] = 1
                else:
                    codes[s[0].tracking_number] += 1
                rem_spells.append(s[0])

        for s in rem_spells:
            obj_handler.rem_spell(spell=s)

        for unit in obj_handler.Units:
            if unit[1] in codes:
                unit[0].take_damage(self.base_damage + (codes[unit[1]] * self.damage_per_blaze) +
                                    stats["aoe_damage"] + stats["damage"], "FIRE")

        self.cooldown = self.maxCooldown * ((100 - stats["cooldown_recovery"]) / 100)

    def step(self):
        super().step()
