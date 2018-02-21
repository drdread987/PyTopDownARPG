import objects.bases
from objects.Tools.collision import rect_collide as collide
from objects.Tools.Sprite import AnimatedSprite as AS


class Player(objects.bases.BaseUnit):

    def __init__(self, x, y, save_name, IL):
        super().__init__(x, y)

        self.level = None

        self.experience = None

        self.player = True

        self.pclass = None
        self.gravity = True
        self.maxHealth = 1
        self.currentHealth = self.maxHealth
        self.double_jumped = False
        self.double_jump_available = True

        self.camera_locked = False

        self.animated = True
        self.animation = "RIGHT"
        self.direction = "RIGHT"
        self.animation_changed = False
        self.width = 25
        self.height = 32
        self.speed = 3
        self.image = AS(self.width, self.height, "res/Player/scr1_spritesheet.png", IL,
                        10, ["RIGHT", "LEFT", "RIGHTIDLE", "LEFTIDLE", "INAIRRIGHT", "INAIRLEFT"],
                        [2, 2, 1, 1, 1, 1, 1])

    def load_pclass(self, save_name):

        pass

    def draw(self, object_handler, IL):
        super().draw(object_handler, IL)

    def step(self, obj_handler, keys, mouse_info):
        self.handle_keys(keys, obj_handler)
        if self.onGround and self.double_jumped and self.double_jump_available:
            self.double_jumped = False
        super().step(obj_handler, keys, mouse_info)

        if self.y > obj_handler.height:
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
        if not self.camera_locked:
            obj_handler.shift_room(self.x, self.y)

    def handle_keys(self, keys, obj_handler):
        delete_keys = []
        key_counter = 0
        for key in keys:
            # print(key)
            if key == 100:
                good = self.move(self.speed, obj_handler)
                if good:
                    self.animation = "RIGHT"
                    self.direction = "RIGHT"
                    self.animation_changed = True
            elif key == 97:
                good = self.move(-self.speed, obj_handler)
                if good:
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
