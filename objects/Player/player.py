import objects.bases
from objects.Tools.collision import rect_collide as collide
from objects.Tools.Sprite import AnimatedSprite as AS
import objects.Player.pclasses.fire


class Player(objects.bases.BaseUnit):

    def __init__(self, x, y, save_name, IL):
        super().__init__(x, y)
        # ###################OBJ VALUES###########################
        self.player = True
        self.enemy = False
        self.alignment = "GOOD"
        self.pclass = objects.Player.pclasses.fire.Fire()
        self.gravity = True
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.double_jumped = False
        self.double_jump_available = True

        self.camera_locked = False

        self.animated = True
        self.animation = "RIGHT"
        self.direction = "RIGHT"
        self.animation_changed = False
        self.width = 25
        self.i_width = self.width
        self.height = 32
        self.i_height = self.height
        self.speed = 3
        self.image = AS(self.i_width, self.i_height, "res/Player/scr1_spritesheet.png", IL,
                        10, ["RIGHT", "LEFT", "RIGHTIDLE", "LEFTIDLE", "INAIRRIGHT", "INAIRLEFT"],
                        [2, 2, 1, 1, 1, 1, 1])
        # ###################OBJ VALUES###########################

        # ###################STATS###########################
        self.stats = {"fortitude": 0,  # towards max health, flat value
                      "agility": 0,  # percentage towards speed
                      "dot_damage": 0,  # flat value damage increase
                      "expertise": 0,  # class based stat
                      "cooldown_recovery": 0,  # percentage towards ability cooldown recovery
                      "aoe_damage": 0,  # flat value damage increase
                      "st_damage": 0,  # flat value damage increase
                      "resource_control": 0,  # percentage towards class resource control,
                      "damage": 0  # pure damage increase
                      }
        # ###################STATS###########################

        self.stat_change()
        self.currentHealth = self.maxHealth

    def stat_change(self):

        self.pclass.stat_change(self, self.stats)

    def load_pclass(self, save_name):

        pass

    def draw(self, object_handler, IL):
        super().draw(object_handler, IL)

        self.pclass.draw_cooldown(object_handler)

    def step(self, obj_handler, keys, mouse_info):
        self.handle_keys(keys, obj_handler)
        self.pclass.step(obj_handler)
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
            if key == 100 or key == 275:
                good = self.move(self.speed, obj_handler)
                if good:
                    self.animation = "RIGHT"
                    self.direction = "RIGHT"
                    self.animation_changed = True
            elif key == 97 or key == 276:
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

            elif key == 115 or key == 274:
                if self.onGround and self.y < obj_handler.height - 32 - self.height:
                    self.y += 3
                    self.onGround = False

            elif key in [49, 50, 51, 52, 53, 54]:
                self.pclass.cast_ability(key, self.stats, obj_handler, self.x, self.y, self.direction)

            key_counter += 1
        delete_keys.sort(reverse=True)
        for key in delete_keys:
            del keys[key]
