import pygame


class BaseClass:

    def __init__(self):

        self.ability_one = None
        self.ability_two = None
        self.ability_three = None
        self.ability_four = None
        self.ability_five = None
        self.ability_expertise = None

        self.resource = 0
        self.resource_max = 0
        self.resource_name = None

        self.fortitudeMultiplier = 1

    def stat_change(self, player, stats):

        player.maxHealth = 100 + (stats["fortitude"] * self.fortitudeMultiplier)
        player.speed = 3 * (1 + (stats["agility"] / 100))

    def step(self, obj_list):

        for ability in [self.ability_one, self.ability_two, self.ability_three, self.ability_four,
                        self.ability_five, self.ability_expertise]:
            if ability is not None:
                ability.step()

    def get_ability_names(self):

        return [self.ability_one.name, self.ability_two.name, self.ability_three.name, self.ability_four.name,
                self.ability_five.name, self.ability_expertise.name]

    def get_ability_cooldowns(self):

        return [self.ability_one.cooldown, self.ability_two.cooldown, self.ability_three.cooldown,
                self.ability_four.cooldown, self.ability_five.cooldown, self.ability_expertise.cooldown]

    def get_ability_description(self, value, stats):

        if value == 1:
            return self.ability_one.get_description(stats)
        elif value == 2:
            return self.ability_two.get_description(stats)
        elif value == 3:
            return self.ability_three.get_description(stats)
        elif value == 4:
            return self.ability_four.get_description(stats)
        elif value == 5:
            return self.ability_five.get_description(stats)
        elif value == 6:
            return self.ability_expertise.get_description(stats)

    def cast_ability(self, key, stats, obj_handler, x, y, direction):

        if key == 49 and self.ability_one is not None and self.ability_one.cooldown == 0:
            self.ability_one.cast_ability(obj_handler, stats, x, y, direction)
        elif key == 50 and self.ability_two is not None and self.ability_two.cooldown == 0:
            self.ability_two.cast_ability(obj_handler, stats, x, y, direction)
        elif key == 51 and self.ability_three is not None and self.ability_three.cooldown == 0:
            self.ability_three.cast_ability(obj_handler, stats, x, y, direction)
        elif key == 52 and self.ability_four is not None and self.ability_four.cooldown == 0:
            self.ability_four.cast_ability(obj_handler, stats, x, y, direction)
        elif key == 53 and self.ability_five is not None and self.ability_five.cooldown == 0:
            self.ability_five.cast_ability(obj_handler, stats, x, y, direction)
        elif key == 54 and self.ability_expertise is not None and self.ability_expertise.cooldown == 0:
            self.ability_expertise.cast_ability(obj_handler, stats, x, y, direction)

    def draw_cooldown(self, obj_handler):
        counter = 0
        for spell in [self.ability_one, self.ability_two, self.ability_three, self.ability_three, self.ability_four,
                      self.ability_five, self.ability_expertise]:
            if spell is not None:
                if spell.maxCooldown > 0:
                    if spell.cooldown == 0:
                        height = 50
                    else:
                        height = 50 * (spell.cooldown / spell.maxCooldown)
                else:
                    height = 50
                pygame.draw.rect(obj_handler.db, spell.cooldown_colors, [0 + (10 * counter), 800 - height, 10, height])
            counter += 1


