from enum import Enum
from collections import deque

__author__ = "Hendrik Werner"


class Snake():
    class Direction(Enum):
        Up = 0
        Right = 1
        Down = 2
        Left = 3

        @classmethod
        def from_key(cls, key):
            if key == "w":
                return cls.Up
            if key == "a":
                return cls.Left
            if key == "s":
                return cls.Down
            if key == "d":
                return cls.Right

    def __init__(self, x, y, direction="r"):
        self.body = deque([(y, x)])
        self.direction = direction

    @property
    def head(self):
        return self.body[-1]

    def update_head(self):
        y, x = self.head
        if self.direction == Snake.Direction.Up:
            y -= 1
        elif self.direction == Snake.Direction.Right:
            x += 1
        elif self.direction == Snake.Direction.Down:
            y += 1
        elif self.direction == Snake.Direction.Left:
            x -= 1
        self.body.append((y, x))

    def update_tail(self):
        self.body.popleft()

    def update_direction(self, key):
        if key not in "wasd":
            return
        self.direction = Snake.Direction.from_key(key)

    def draw(self, window):
        window.addch(*self.head, "■")
        window.addch(*self.body[0], " ")
