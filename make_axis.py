import numpy as np


class axis():
    def __init__(self, sample=100):
        self.axis = []
        self.sample = 100

    def update(self, Value_new):
        while len(self.axis) >= self.sample:
            self.axis = self.axis[1:][:]
        self.axis.append(Value_new)
        return self.axis


class axis_array():
    def __init__(self, Array_length=2, sample=100):
        self._axis = []
        self.axis = []
        for i in range(Array_length):
            self._axis.append(axis())
            self.axis.append([])
        self.sample = 100

    def update(self, Array_value_new):
        for key, Value_new in enumerate(self._axis):
            self._axis[key].update(Array_value_new[key])
            self.axis[key] = np.array(self._axis[key].axis).T

    """"
    def _axis(self):
        Return_value = []
        for key in range(len(self._axis)):
            Return_value.append(self._axis[key].axis)
        return Return_value
    """