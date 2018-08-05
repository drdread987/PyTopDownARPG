import objects.bases
import objects.Tools.collision as collide


class Lightning(objects.bases.BaseSpell):

    def __init__(self, x, y, damage):
        super().__init__(x, y)

        self.damage = damage
        self.speed = 30

        self.width = 15
        self.height = 125

        self.image = "res/lightning_warning.png"
        self.launch_timer = 125
        self.launched = False

    def draw(self, object_handler, IL):
        super().draw(object_handler, IL)

        if not self.launched:
            for x in range(1, int(1600/self.height)+1):
                object_handler.draw_object(IL.load_image(self.image), (self.x, self.y + (self.height * x)))

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        if not self.launched:
            if self.launch_timer == 0:
                self.launch()
            else:
                self.launch_timer -= 1
        else:
            self.y += self.speed
            if collide.rect_collide(self.x, self.width, self.y, self.height,
                                    obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                    obj_handler.Units[0][0].height):
                obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")

    def launch(self):

        self.image = "res/lightning.png"
        self.launched = True


