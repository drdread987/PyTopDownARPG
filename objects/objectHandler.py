import random
import datetime
import pygame
import sys
import objects.ImageLoader


class Room:

    def __init__(self, drawing_board):

        self.Doodads = []  # stored [[doodad, code]...]
        self.Units = []  # stored [[unit, code]...]
        self.Spells = []  # stored [[spell, code]...]

        self.Codes = {}  # stored {code:frames_till_death,...} if -1 then that means the code is still alive
        self.creation_time = datetime.datetime.now()
        self.last_time = datetime.datetime.now()
        self.background = None
        self.draw_time = 0
        self.room_good = True
        self.poss_next_room = None

        self.width = 1200
        self.height = 800

        self.image_loader = objects.ImageLoader.IL()

        self.db = drawing_board

        self.key_box = []
        self.mouse_info = [pygame.mouse.get_pressed(), pygame.mouse.get_pos()]

    def frame_handle(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.handle_keys(event)
            elif event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse(event)

        current_time = datetime.datetime.now()

        delta_time = current_time - self.last_time
        delta_time = delta_time.microseconds

        self.draw_time += delta_time

        self.last_time = current_time
        if self.draw_time > 16666:
            for spell in self.Spells:
                spell[0].step(self, self.key_box, self.mouse_info)
            for unit in self.Units:
                unit[0].step(self, self.key_box, self.mouse_info)
            for doodad in self.Doodads:
                doodad[0].step(self, self.key_box, self.mouse_info)
            self.draw_time = 0

            if delta_time == 0:
                pass
            else:
                fps = 6000000 / float(delta_time)
                print("fps: " + str(fps))

        if self.background is not None:
            self.db.blit(self.background, (0, 0))
        for spell in self.Spells:
            spell[0].draw(self.db, self.image_loader)
        for unit in self.Units:
            unit[0].draw(self.db, self.image_loader)
        for doodad in self.Doodads:
            doodad[0].draw(self.db, self.image_loader)
        pygame.display.flip()

    def add_doodad(self, doodad):

        code = self.gen_code()

        self.Doodads.append([doodad, code])

        return code

    def add_unit(self, unit):
        code = self.gen_code()
        self.Units.append([unit, code])

        return code

    def add_spell(self, spell):

        code = self.gen_code()

        self.Spells.append([[spell, code]])

        return code

    def rem_doodad(self, code=None, doodad=None):

        if code is None and doodad is None:
            return False

        if code is not None:
            counter = 0
            for d in self.Doodads:
                if d[1] == code:
                    del self.Doodads[counter]
                    self.retire_code(code)
                counter += 1
        else:
            counter = 0
            for d in self.Doodads:
                if d[0] == doodad:
                    self.retire_code(d[1])
                    del self.Doodads[counter]
                counter += 1

    def rem_unit(self, code=None, unit=None):

        if code is None and unit is None:
            return False

        if code is not None:
            counter = 0
            for u in self.Units:
                if u[1] == code:
                    del self.Units[counter]
                    self.retire_code(code)
                counter += 1
        else:
            counter = 0
            for u in self.Units:
                if u[0] == unit:
                    self.retire_code(u[1])
                    del self.Units[unit]
                counter += 1

    def rem_spell(self, code=None, spell=None):

        if code is None and spell is None:
            return False

        if code is not None:
            counter = 0
            for s in self.Spells:
                if s[1] == code:
                    del self.Spells[counter]
                    self.retire_code(code)
                counter += 1
        else:
            counter = 0
            for s in self.Spells:
                if s[0] == spell:
                    self.retire_code(s[1])
                    del self.Spells[counter]
                counter += 1

    def gen_code(self):

        code = random.randint(0, 100000)
        while code in self.Codes:
            code = random.randint(0, 100000)
        self.Codes[code] = -1

        return code

    def retire_code(self, code):

        if code in self.Codes:
            self.Codes[code] = 5

    def handle_codes(self):

        for code in self.Codes:

            if self.Codes[code] > 0:
                self.Codes[code] -= 1
            elif self.Codes == 0:
                del self.Codes[code]

    def handle_keys(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key not in self.key_box:
                self.key_box.append(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in self.key_box:
                self.key_box.remove(event.key)

    def handle_mouse(self, event):

        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP or \
                event.type == pygame.MOUSEBUTTONDOWN:

            self.mouse_info = [pygame.mouse.get_pressed(), pygame.mouse.get_pos()]


    def initiate_room(self):

        while self.room_good:

            self.frame_handle()

    def next_room(self):

        return self.poss_next_room

    def set_next_room(self, room):

        self.poss_next_room = room

    def end_room(self):

        self.room_good = False

    def quit_game(self):

        sys.exit()







