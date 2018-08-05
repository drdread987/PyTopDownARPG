import objects.bases
import objects.Tools.collision as collide


class Heart(objects.bases.BaseSpell):

    def __init__(self, x, y, healing):
        super().__init__(x, y)

        self.width = 25
        self.height = 25
        self.image = "res/heart.png"

        self.gravity = True
        self.healing = healing

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            if obj_handler.Units[0][0].currentHealth + self.healing > obj_handler.Units[0][0].maxHealth:
                obj_handler.Units[0][0].currentHealth = obj_handler.Units[0][0].maxHealth
            else:
                obj_handler.Units[0][0].currentHealth += self.healing

            obj_handler.rem_spell(spell=self)
