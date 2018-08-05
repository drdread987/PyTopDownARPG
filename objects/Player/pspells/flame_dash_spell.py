import objects.bases


class FlameDashSpell(objects.bases.BaseSpell):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.width = 32
        self.height = 32
        self.image = "res/flame_dash.png"

        self.timeLeft = 60

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        self.timeLeft -= 1
        if self.timeLeft == 0:
            obj_handler.rem_spell(spell=self)
