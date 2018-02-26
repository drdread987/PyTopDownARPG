
class Base:

    def __init__(self):

        self.spell_cast = []

        self.name = None
        self.cooldown = 0
        self.maxCooldown = 0

        self.description = ""

    def cast_ability(self, obj_handler, stats, x, y):

        for spell in self.spell_cast:
            obj_handler.add_spell(spell(x, y, ))
