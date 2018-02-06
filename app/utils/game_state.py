from vector import Vector
from utils.competitor import Competitor


class GameState(object):

    def __init__(self, data):
        self.data = data
        self._empty_squares = None
        self._food = None

    def empty_squares(self):
        if self._empty_squares is not None:
            return self._empty_squares

        width = self.data["width"]
        height = self.data["height"]
        empty_squares = {}
        for x in range(0, width):
            for y in range(0, height):
                empty_squares[(x, y)] = True

        for snake in self.data["snakes"]["data"]:
            segments = snake["body"]["data"]
            for segment in segments:
                x = segment["x"]
                y = segment["y"]
                v = (x, y)
                if v in empty_squares:
                    del empty_squares[v]

        self._empty_squares = empty_squares
        return empty_squares

    def is_empty(self, v):
        return (v.x, v.y) in self.empty_squares()

    def competitors(self):
        competition = []
        for snake in self.data["snakes"]["data"]:
            if snake["id"] == self.data["you"]["id"]:
                continue
            segments = snake["body"]["data"]
            competition.append(Competitor(
                head=Vector(segments[0]["x"], segments[0]["y"]),
                neck=Vector(segments[1]["x"], segments[1]["y"]),
                length=len(segments),
            ))
        return competition

    @property
    def my_length(self):
        segments = self.data["you"]["body"]["data"]
        return len(segments)

    @property
    def my_head(self):
        segments = self.data["you"]["body"]["data"]
        p = segments[0]
        return Vector(p["x"], p["y"])

    @property
    def my_neck(self):
        segments = self.data["you"]["body"]["data"]
        p = segments[1]
        return Vector(p["x"], p["y"])

    @property
    def current_direction(self):
        return self.my_head - self.my_neck

    @property
    def board_width(self):
        return self.data["width"]

    @property
    def board_height(self):
        return self.data["height"]

    @property
    def food(self):
        if self._food is None:
            self._food = [Vector(f["x"], f["y"]) for f in self.data["food"]["data"]]
        return self._food
