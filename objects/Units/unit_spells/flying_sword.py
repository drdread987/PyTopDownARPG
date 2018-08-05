import objects.bases
import objects.Tools.collision as collide


class FlyingSword(objects.bases.BaseSpell):

    def __init__(self, x, y, damage):
        super().__init__(x, y)

        self.damage = damage

        self.speed = 6

        self.image = "res/flying_sword.png"
        self.width = 61
        self.height = 18

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        self.x -= self.speed
        if self.x + self.width < 0:
            obj_handler.rem_spell(spell=self)

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")
