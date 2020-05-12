class Shape():
    def __init__(self, points, id=None, t=None):
        self.points = points
        self.id = id
        self.type = t
    def __repr__(self):
        return str(self.points)
