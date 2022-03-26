import numpy as np
import matplotlib.pyplot as plt


class WavePlot:
    def __init__(self, plot_colors, y_axis_lim=[-1.1, 1.1]):
        self.fig = plt.figure(figsize=(9, 7))
        self.x = np.arange(0, 10*np.pi, 0.01)
        self.colors = plot_colors
        self.y_axis_lim = y_axis_lim
        self.add_lines()


    def add_lines(self):
        ax1 = self.fig.add_subplot(411)
        ax2 = self.fig.add_subplot(412)
        ax3 = self.fig.add_subplot(413)
        self.ax4 = self.fig.add_subplot(414)
        ax1.set_ylim(self.y_axis_lim)
        ax2.set_ylim(self.y_axis_lim)
        ax3.set_ylim(self.y_axis_lim)
        self.line1, = ax1.plot(self.x, np.cos(self.x), color=self.colors[0])
        self.line2, = ax2.plot(self.x, np.cos(self.x), color=self.colors[1])
        self.line3, = ax3.plot(self.x, np.cos(self.x), color=self.colors[2])
        #self.point,  = self.ax4.plot(self.x, np.cos(self.x), 'r')

    def pin_window(self, window):
        self.win = window

    def animate(self, i):
        self.ax4.clear()
        A = 1
        dt = 0.1
        if self.win.sel_option.value == 0:
            w1 = self.win.ang_freq_scale1.get()
            w2 = self.win.ang_freq_scale2.get()
            k1 = self.win.wave_v_scale1.get()
            k2 = self.win.wave_v_scale2.get()
        else:
            w1 = self.win.sel_option.ang_freq1
            w2 = self.win.sel_option.ang_freq2
            k1 = self.win.sel_option.wave_v1
            k2 = self.win.sel_option.wave_v2
        t = i * dt
        y1 = A*np.cos(w1*t - k1*self.x)
        y2 = np.cos(k2 * self.x - w2 * t)


        # v = (w2 - w1) / (k2 - k1)
        # vg = (w2 + w1) / (k2 + k1)
        # deltg = 10 if v <= 0 else 10


        self.line1.set_data(self.x, y1)
        self.line2.set_data(self.x, y2)
        self.line3.set_data(self.x, y1+y2)
        self.ax4.plot(self.x, y1, color=self.colors[0])
        self.ax4.plot(self.x, y2, color=self.colors[1])
        self.ax4.plot(self.x, y1+y2, color=self.colors[2])
        self.ax4.set_ylim(self.y_axis_lim)
        #self.point.set_data(t * cgc - 10, 0)
        # line1.set_data(x, A*np.sin(x+i/10.0))  # update the data
        # line2.set_ydata(A/2*np.sin(x+i/10.0))
        return self.line1, self.line2, self.line3#, self.point


class PrepOption:
    """
        Class with one set of already prepared options for default settings for waves.
        Parameters for two waves plotting:
            - wave vector
            - angular frequency
            - value for distinguishing a particular set of options
    """
    def __init__(self, wave_v_1, ang_freq_1, wave_v_2, ang_freq_2, val):
        self.wave_v1 = wave_v_1
        self.ang_freq1 = ang_freq_1
        self.wave_v2 = wave_v_2
        self.ang_freq2 = ang_freq_2
        self.value = val
