import objects.Player.pspells.base
import objects.Player.pspells.flame_dash_spell


class FlameDash(objects.Player.pspells.base.Base):

    def __init__(self):
        super().__init__()

        self.description = "Dashes forward leaving a trail of fire behind you"

        self.cooldown_colors = [255, 255, 0]
        self.maxCooldown = 500
        self.baseDistance = 320
        self.stepDistance = 32

        self.obj_handler = None

        self.moveDistance = 0
        self.direction = "RIGHT"

    def cast_ability(self, obj_handler, stats, x, y, direction, *args):
        super().cast_ability(obj_handler, stats, x, y, direction, *args)
        self.obj_handler = obj_handler
        if len(args) < 1:
            pass
        else:
            self.direction = direction
            resource = args[0]
            self.moveDistance = self.baseDistance + (resource * 32)

            self.cooldown = self.maxCooldown * ((100 - stats["cooldown_recovery"]) / 100)

    def step(self):
        super().step()

        while self.moveDistance > 0:

            self.obj_handler.add_spell(objects.Player.pspells.flame_dash_spell.FlameDashSpell(self.obj_handler.Units[0][0].x,
                                                                                              self.obj_handler.Units[0][0].y))

            self.moveDistance -= 32
            if self.direction == "RIGHT":
                self.obj_handler.Units[0][0].move(32, self.obj_handler)
            else:
                self.obj_handler.Units[0][0].move(-32, self.obj_handler)
