import objects.Player.pclasses.base
import objects.Player.pspells.blaze


class Fire(objects.Player.pclasses.base.BaseClass):

    def __init__(self):
        super().__init__()

        self.resource_name = "Blaze"
        self.resource_max = 10

    def step(self, obj_list):
        super().step(obj_list)
        self.resource = 0
        for spell in obj_list.Spells:
            if isinstance(spell[0], objects.Player.pspells.blaze.Blaze):
                self.resource += 1

