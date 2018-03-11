import matplotlib.pyplot as plt
import numpy as np


class realtime():
    def __init__(self, x_data=[0], y_data=[0], Quantity_of_data=4):
        self.plt = plt
        self.fig = self.plt.figure()

        self.Quantity_of_data = Quantity_of_data
        self.ax = []
        for Number_of_data in range(Quantity_of_data):
            ax = self.fig.add_subplot(Quantity_of_data, 1, Number_of_data + 1)
            self.ax.append(ax.plot(x_data, y_data))

    def plot(self, x_data, y_data, pause_time=0):
        y_data = np.array(y_data)
        x_data = np.array(x_data)

        for i in range(self.Quantity_of_data):
            self.ax[i].set_data(x_data, y_data[i])
            self.ax.set_xlim((x_data.min(), x_data.max()))
            self.ax.set_ylim((y_data.min(), y_data.max()))

        if pause_time == 0:
            return
        self.plt.pause(pause_time)

    def pause(self):
        self.plt.pause(.01)
