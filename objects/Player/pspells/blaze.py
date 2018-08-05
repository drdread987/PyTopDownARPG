import objects.Player.pspells.base
import objects.Player.pspells.blaze_spell


class Blaze(objects.Player.pspells.base.Base):

    def __init__(self):
        super().__init__()
        self.description = "Any Time a fire spell hits a target it applies blaze (max 1 per target). " \
                           "This empowers your, other abilities."
        self.cooldown_colors = [255, 255, 255]

    def cast_ability(self, obj_handler, stats, x, y, direction, *args):
        super().cast_ability(obj_handler, stats, x, y, direction)
        if len(args) < 1:
            pass
        else:
            obj_handler.add_spell(objects.Player.pspells.blaze_spell.BlazeSpell(x, y, args[0]))



