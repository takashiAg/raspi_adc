import matplotlib.pyplot as plt
import numpy as np


class realtime():
    def __init__(self, x_data=[0], y_data=[0], Quantity_data=1):
        self.plt = plt

        self.fig, self.ax = self.plt.subplots(1, 1)

        self.Quantity_data = Quantity_data
        self.lines = []
        for i in range(Quantity_data):
            self.line, = self.ax.plot(x_data, y_data)
            self.lines.append(self.line)

    def plot(self, x_data_input, y_data_input):
        y_data = np.array(y_data_input)
        x_data = np.array(x_data_input)
        if y_data.size == 1:
            y_data = [y_data]

        for i in range(self.Quantity_data):
            self.lines[i].set_data(x_data, y_data[i])

        y_min = y_data.min()
        y_max = y_data.max()

        self.ax.set_xlim((x_data.min(), x_data.max()))
        self.ax.set_ylim((y_min, y_max))

    def pause(self):
        self.plt.pause(.000000000001)
