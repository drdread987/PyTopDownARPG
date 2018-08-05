import objects.Player.pspells.base
import objects.Player.pspells.fireball_spell


class Fireball(objects.Player.pspells.base.Base):

    def __init__(self):
        super().__init__()

        self.description = "Launches a fireball out that deal significant damage to the next target it hits. " \
                           "More resource increases the amount of fireballs launched."
        self.cooldown_colors = [255, 0, 0]

        self.maxCooldown = 60

    def cast_ability(self, obj_handler, stats, x, y, direction, *args):
        super().cast_ability(obj_handler, stats, x, y, direction, *args)

        if len(args) > 0:
            amount = args[0]

            damage = stats["st_damage"] + stats["damage"] + 5

            obj_handler.add_spell(objects.Player.pspells.fireball_spell.FireballSpell(x, y, direction, damage))

            self.cooldown = self.maxCooldown * ((100 - stats["cooldown_recovery"])/100)
