import matplotlib.pyplot as plt

class realtime():
    def __init__(self, x_data=[0], y_data=[0]):
        self.plt = plt

        self.fig, self.ax = self.plt.subplots(1, 1)

        self.lines, = self.ax.plot(x_data, y_data)


    def plot(self, x_data, y_data):
        self.lines.set_data(x_data, y_data)
        self.ax.set_xlim((x_data.min(), x_data.max()))
        self.ax.set_ylim((y_data.min(), y_data.max()))
        self.plt.pause(.01)

    def pause(self):
        self.plt.pause(.01)

