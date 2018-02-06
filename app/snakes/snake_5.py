from utils.vector import Vector, up, down, left, right, noop
from base_snake import BaseSnake


class Snake5(BaseSnake):

    def move(self, gamestate):
        kill = self._move_for_kill(gamestate)
        if kill is not None:
            return kill
        for_food = self._move_for_food(gamestate)
        if for_food is not None:
            return for_food
        return up

    def _move_for_kill(self, gamestate):
        # Dumb algo for hitting a snakes head.
        for competitor in gamestate.competitors():
            if competitor.length < gamestate.my_length:
                target = competitor.head
                ordered_directions = self._directions_to(target, gamestate)
                head = gamestate.my_head
                for v in ordered_directions:
                    if v == target or gamestate.is_empty(head + v):
                        return v

    def _move_for_food(self, gamestate):
        target = self._closest_to(gamestate.food, gamestate.my_head)
        ordered_directions = self._directions_to(target, gamestate)
        head = gamestate.my_head
        for v in ordered_directions:
            if gamestate.is_empty(head + v):
                return v

    def _is_healthy(self, gamestate):
        return True

    def _closest_to(self, goals, start):
        def _dist(a, b):
            return abs((a-b).magnitude)
        goals.sort(key=lambda x: _dist(x, start), reverse=False)
        return goals[0]

    def _directions_to(self, goal, gamestate):
        distances = [
            ((goal-gamestate.my_head-left).magnitude, left),
            ((goal-gamestate.my_head-right).magnitude, right),
            ((goal-gamestate.my_head-up).magnitude, up),
            ((goal-gamestate.my_head-down).magnitude, down),
        ]
        distances.sort(key=lambda x: x[0], reverse=False)
        return [d[1] for d in distances]

    def name(self):
        return "Training Snake 5"

    def color(self):
        return "#ee42f4"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
