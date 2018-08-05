import objects.bases
from objects.Tools.Sprite import AnimatedSprite as AS
import objects.Tools.collision as collide
import objects.Player.pspells.blaze


class FireballSpell(objects.bases.BaseSpell):

    def __init__(self, x, y, direction, damage):
        super().__init__(x, y)

        self.direction = direction
        self.animated = False
        self.animation = self.direction

        self.damage = damage
        self.speed = 5
        self.width = 40
        self.height = 30
        self.image_assigned = False

    def draw(self, object_handler, IL):
        super().draw(object_handler, IL)

        if not self.image_assigned:
            self.image = AS(self.width, self.height, "res/fireball_spritesheet.png", IL,
                            2, ["RIGHT", "LEFT"],
                            [3, 3])
            self.image.new_animation(self.animation)
            self.animated = True

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        if self.image is not None:
            self.image.step()
        for unit in obj_handler.Units:
            if unit[0] != self and unit[0].player is False:
                if collide.rect_collide(self.x, self.width, self.y, self.height,
                                        unit[0].x, unit[0].width, unit[0].y, unit[0].height):
                    unit[0].take_damage(self.damage, "FIRE")
                    new_blaze = objects.Player.pspells.blaze.Blaze()
                    new_blaze.cast_ability(obj_handler, [], unit[0].x, unit[0].y, self.direction, unit[1])
                    obj_handler.rem_spell(spell=self)

        if self.direction == "RIGHT":
            self.x += self.speed
            if self.x > obj_handler.width:
                obj_handler.rem_unit(unit=self)
        elif self.direction == "LEFT":
            self.x -= self.speed
            if self.x < 0:
                obj_handler.rem_unit(unit=self)
