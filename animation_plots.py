import numpy as np
import matplotlib.pyplot as plt


class WavePlot:
    def __init__(self, plot_colors, y_axis_lim=[-1.1, 1.1], y_lim_times=3, max_x=30):
        self.fig = plt.figure(figsize=(9, 7))
        self.fig.suptitle("Waves")
        self.x = np.arange(0, 10*np.pi, 0.01)
        self.colors = plot_colors
        self.y_axis_lim = y_axis_lim
        self.w_p, self.k_p = 0, 0
        self.max_x = max_x
        self.max_x_p = max_x
        self.max_x_g = max_x
        self.add_lines(y_lim_times)


    def add_lines(self, y_lim_times):
        ax1 = self.fig.add_subplot(411)
        ax2 = self.fig.add_subplot(412)
        ax3 = self.fig.add_subplot(413)
        ax4 = self.fig.add_subplot(414)
        ax1.set_ylim(self.y_axis_lim)
        ax2.set_ylim(self.y_axis_lim)
        ax3.set_ylim(self.y_axis_lim)
        ax4.set_ylim([y_lim_times*y for y in self.y_axis_lim])
        self.line1, = ax1.plot(self.x, np.cos(self.x), color=self.colors[0])
        self.line2, = ax2.plot(self.x, np.cos(self.x), color=self.colors[1])
        self.line3, = ax3.plot(self.x, np.cos(self.x), color=self.colors[2])
        self.line4, = ax4.plot(self.x, np.cos(self.x), color=self.colors[3])

        kw1 = dict(alpha=0.5, linestyle='none', marker='o')
        self.point4_p,  = ax4.plot([], [], 'r', **kw1)
        self.point4_g,  = ax4.plot([], [], 'b', **kw1)

    def pin_window(self, window):
        self.win = window

    def animate(self, i):
        A = 1
        dt = 0.1
        if self.win.sel_option.value == 0:
            w1 = self.win.ang_freq_scale1.get()
            w2 = self.win.ang_freq_scale2.get()
            w3 = self.win.ang_freq_scale3.get()
            k1 = self.win.wave_v_scale1.get()
            k2 = self.win.wave_v_scale2.get()
            k3 = self.win.wave_v_scale3.get()
        else:
            w1 = self.win.sel_option.ang_freq1
            w2 = self.win.sel_option.ang_freq2
            w3 = self.win.sel_option.ang_freq3
            k1 = self.win.sel_option.wave_v1
            k2 = self.win.sel_option.wave_v2
            k3 = self.win.sel_option.wave_v3
        t = i * dt
        y1 = A*np.cos(k1 * self.x - w1 * t)
        y2 = A*np.cos(k2 * self.x - w2 * t)
        y3 = A*np.cos(k3 * self.x - w3 * t)

        self.w_c = w1+w2+w3
        self.k_c = k1+k2+k3

        # dw = w_current - w_previous
        self.dw = self.w_c - self.w_p
        self.dk = self.k_c - self.k_p

        # phase velocity
        if self.k_c != 0: 
            v_p = self.w_c/self.k_c
            point_p = v_p*t
            if point_p > self.max_x:
                point_p -= self.max_x_p
                self.max_x_p += self.max_x
        else:
            point_p = 0

        # if self.dk != 0:
        #     v_g = self.dw/self.dk
        #     point_g = v_g*t
        #     if point_g>self.max_x:
        #         point_g -= self.max_x
        #         self.max_x_g+=self.max_x
        # else:
        #     point_g = 1

        #TODO: calculating group velocity
        if k2-k1==0 or self.dk==0:
            v_g = 1
        else:
            v_g = self.dw/self.dk

        point_g = v_g*t

        print(point_g)

        self.point4_p.set_data(point_p, 0)
        self.point4_g.set_data(point_g, -0.25)
        self.line1.set_data(self.x, y1)
        self.line2.set_data(self.x, y2)
        self.line3.set_data(self.x, y3)
        self.line4.set_data(self.x, y1+y2+y3)

        self.w_p = self.w_c
        self.k_p = self.k_c

        return self.line1, self.line2, self.line3, self.line4, self.point4_p


class PrepOption:
    """
        Class with one set of already prepared options for default settings for waves.
        Parameters for two waves plotting:
            - wave vector
            - angular frequency
            - value for distinguishing a particular set of options
    """
    def __init__(self, wave_v_1, ang_freq_1, wave_v_2, ang_freq_2, wave_v_3, ang_freq_3, val):
        self.wave_v1 = wave_v_1
        self.ang_freq1 = ang_freq_1
        self.wave_v2 = wave_v_2
        self.ang_freq2 = ang_freq_2
        self.wave_v3 = wave_v_3
        self.ang_freq3 = ang_freq_3
        self.value = val
