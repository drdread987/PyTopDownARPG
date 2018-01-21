
def rect_collide(x1, w1, y1, h1, x2, w2, y2, h2):

    if x1 + w1 >= x2 and x1 <= x2 + w2:
        if y1 + h1 >= y2 and y1 <= y2 + h2:
            return True
        else:
            return False
    else:
        return False
