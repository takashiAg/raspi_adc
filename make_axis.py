class axis():
    def __init__(self, sample=100):
        self.axis = []
        self.sample = 100
    def update(self, Value_new):
        while len(self.axis) >= self.sample:
            self.axis = self.axis[1:]
        self.axis.append(Value_new)
        return self.axis
