from collections import deque

__author__ = "Hendrik Werner"


class Snake():
    def __init__(self, x, y, direction="r"):
        self.body = deque([(y, x)])
        self.direction = direction

    def update_head(self):
        y, x = self.body[-1]
        if self.direction == "u":
            y -= 1
        elif self.direction == "r":
            x += 1
        elif self.direction == "d":
            y += 1
        elif self.direction == "l":
            x -= 1
        self.body.append((y, x))

    def update_tail(self):
        self.body.popleft()

    def update_direction(self, direction):
        if direction not in ["u", "r", "d", "l"]:
            return
        self.direction = direction

    def draw(self, window):
        window.addch(*self.body[-1], "■")
        window.addch(*self.body[0], " ")