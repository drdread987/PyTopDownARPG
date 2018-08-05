import objects.bases


class BlazeSpell(objects.bases.BaseSpell):

    def __init__(self, x, y, tracking_number):
        super().__init__(x, y)

        self.tracking_number = tracking_number
        self.width = 20
        self.height = 23
        self.image = "res/blaze.png"

    def draw(self, object_handler, IL):
        super().draw(object_handler, IL)

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        found = False
        for s in obj_handler.Units:
            if s[1] == self.tracking_number:
                self.x = s[0].x + (s[0].width / 2) - (self.width / 2)
                self.y = s[0].y + s[0].height - self.height
                found = True
        if not found:
            obj_handler.rem_spell(spell=self)

