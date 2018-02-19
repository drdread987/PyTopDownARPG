import objects.bases
from objects.Tools.collision import rect_collide as collide
from objects.Tools.Sprite import AnimatedSprite as AS


class Player(objects.bases.BaseUnit):

    def __init__(self, x, y, save_name, IL):
        super().__init__(x, y)

        self.level = None

        self.experience = None

        self.pclass = None
        self.gravity = True
        self.maxHealth = 1
        self.currentHealth = self.maxHealth
        self.double_jumped = False
        self.double_jump_available = True

        self.animated = True
        self.animation = "RIGHT"
        self.direction = "RIGHT"
        self.animation_changed = False
        self.width = 32
        self.height = 32
        self.speed = 3
        self.image = AS(self.width, self.height, "res/Player/scr1_spritesheet.png", IL,
                        10, ["RIGHT", "LEFT", "RIGHTIDLE", "LEFTIDLE", "INAIRRIGHT", "INAIRLEFT"],
                        [2, 2, 1, 1, 1, 1, 1])

    def load_pclass(self, save_name):

        pass

    def draw(self, db, IL):
        super().draw(db, IL)

    def step(self, obj_handler, keys, mouse_info):
        self.handle_keys(keys, obj_handler)
        if self.onGround and self.double_jumped and self.double_jump_available:
            self.double_jumped = False
        super().step(obj_handler, keys, mouse_info)

        if self.y > 800:
            self.take_damage(1, "PHYSICAL")
        if not self.onGround:
            if self.direction == "RIGHT":
                self.animation = "INAIRRIGHT"
            else:
                self.animation = "INAIRLEFT"
        elif not self.animation_changed:
            self.animation = self.direction + "IDLE"
        else:
            self.animation_changed = False
        self.image.new_animation(self.animation)
        # print(self.x, self.y)

    def handle_keys(self, keys, obj_handler):
        delete_keys = []
        key_counter = 0
        for key in keys:
            # print(key)
            if key == 100:
                good = True
                for obj in obj_handler.Doodads:
                    if obj[0].obstruction:
                        if collide(self.x + self.width + self.speed, 1, self.y-1, self.height,
                                   obj[0].x, obj[0].width, obj[0].y, obj[0].height):

                            if obj[0].passable:
                                good = True
                            else:
                                self.x = obj[0].x - self.width - 1
                                good = False

                if good:
                    self.x += self.speed
                    self.animation = "RIGHT"
                    self.direction = "RIGHT"
                    self.animation_changed = True
            elif key == 97:
                good = True
                for obj in obj_handler.Doodads:
                    if obj[0].obstruction:
                        if collide(self.x - self.speed, 1, self.y-1, self.height,
                                   obj[0].x, obj[0].width, obj[0].y, obj[0].height):
                            if obj[0].passable:
                                good = True
                            else:
                                self.x = obj[0].x + obj[0].width + 1
                                good = False

                if good:
                    self.x -= self.speed
                    self.animation = "LEFT"
                    self.direction = "LEFT"
                    self.animation_changed = True

            elif key == 32 and self.onGround and not self.jumping:
                self.jumping = True
                self.upwardVelocity = self.upwardVelocityMax
                delete_keys.append(key_counter)
            elif key == 32 and not self.double_jumped and self.double_jump_available:
                self.jumping = True
                self.upwardVelocity = self.upwardVelocityMax
                self.double_jumped = True
                delete_keys.append(key_counter)

            key_counter += 1
        delete_keys.sort(reverse=True)
        for key in delete_keys:
            del keys[key]
