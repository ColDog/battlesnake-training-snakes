class Competitor:

    def __init__(self, head=None, neck=None, length=None):
        self.head = head
        self.neck = neck
        self.length = length

    @property
    def direction(self):
        return self.head - self.neck

    def estimated_next(self):
        return self.head + self.direction
