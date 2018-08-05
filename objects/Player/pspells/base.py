
class Base:

    def __init__(self):
        self.spell_cast = []

        self.name = None
        self.cooldown = 0
        self.maxCooldown = 0
        self.cooldown_colors = [0, 0, 0]

        self.description = ""

    def cast_ability(self, obj_handler, stats, x, y, direction, *args):

        pass

    def step(self):

        if self.cooldown > 0:
            self.cooldown -= 1

