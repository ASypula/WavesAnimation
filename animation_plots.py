import numpy as np
import matplotlib.pyplot as plt

class WavePlot:
    def __init__(self, plot_colors, A=1, y_axis_lim=[-1.1, 1.1], y_lim_times=3, max_x=30):
        """
            Class for plotting four waves, three customized and one - resulting from their interference
                @param plot_colors: list with four different colours for according waves
                @param A: waves' amplitude
                @param y_axis_lim: range of y axis
                @param y_lim_times: number of times resulting wave's y axis range is bigger/smaller 
                                    comparing to previous range; resulting range: y_lim_times*y_axis_lim
                @param max_x = upper limit of x axis, starting value is 0 """
        self.fig = plt.figure(figsize=(9, 7))
        self.fig.suptitle("Waves")
        self.x = np.arange(0, 10*np.pi, 0.05)
        self.A = A
        self.colors = plot_colors
        self.y_axis_lim = y_axis_lim
        self.max_x = max_x
        self.add_lines(y_lim_times)

    def add_lines(self, y_lim_times):
        """ Adding subplots to the main window
            First three for customized or preset waves, 
            fourth line for the resulting wave.
            @param y_lim_times: how many times resulting wave's y axis range 
                                differs from the basic range"""
        ax1 = self.fig.add_subplot(411)
        ax2 = self.fig.add_subplot(412)
        ax3 = self.fig.add_subplot(413)
        ax4 = self.fig.add_subplot(414)
        ax1.set_ylim(self.y_axis_lim)
        ax2.set_ylim(self.y_axis_lim)
        ax3.set_ylim(self.y_axis_lim)
        ax4.set_ylim([y_lim_times*y for y in self.y_axis_lim])

        # setting initial waves - cosine functions
        self.line1, = ax1.plot(self.x, np.cos(self.x), color=self.colors[0])
        self.line2, = ax2.plot(self.x, np.cos(self.x), color=self.colors[1])
        self.line3, = ax3.plot(self.x, np.cos(self.x), color=self.colors[2])
        self.line4, = ax4.plot(self.x, np.cos(self.x), color=self.colors[3])

        # setting points for showing phase (point4_p) and group (point4_g) velocity 
        kw1 = dict(alpha=0.5, linestyle='none', marker='o')

        # a dot for group velocity moving in the y-axis
        self.point4_g_mv, = ax4.plot([], [], 'blue', **kw1)

        # a dot for group velocity with constant y-axis value
        self.point4_g_st, = ax4.plot([], [], 'blue', **kw1)

        self.point4_p_mv, = ax4.plot([], [], 'black', **kw1)
        self.point4_p_st, = ax4.plot([], [], 'black', **kw1)


    def pin_window(self, window):
        self.win = window

    def animate(self, i):
        """ Method for waves animation
            waves' parameters are continuously being taken from the values
            set by the user through GUI
            @param i: consecutive integers starting from 0 -> frames numeration """

        # taking waves' w and k from the scales if custom options selected
        if self.win.sel_option.value == 0:
            k1 = self.win.wave_v_scale1.get()
            k2 = self.win.wave_v_scale2.get()
            k3 = self.win.wave_v_scale3.get()
            w1 = self.win.ang_freq_scale1.get()
            w2 = self.win.ang_freq_scale2.get()
            w3 = self.win.ang_freq_scale3.get()


        # taking waves' w and k from the selected preset option
        else:
            k1 = self.win.sel_option.wave_v1
            k2 = self.win.sel_option.wave_v2
            k3 = self.win.sel_option.wave_v3
            w1 = self.win.sel_option.ang_freq1
            w2 = self.win.sel_option.ang_freq2
            w3 = self.win.sel_option.ang_freq3
      
        dt = 0.1
        t = i * dt
        y1 = self.A*np.cos(k1 * self.x - w1 * t)
        y2 = self.A*np.cos(k2 * self.x - w2 * t)
        y3 = self.A*np.cos(k3 * self.x - w3 * t)

        sum_y = y1 + y2 + y3

        if (not w1 and not w2 and not w3) or (not k1 and not k2 and not k3):
            v_g = 0
            v_p = 0
        else:
            v_g = calc_group_vel([w1, w2, w3], [k1, k2, k3])
            v_p = calc_phase_vel([w1, w2, w3], [k1, k2, k3])

        point_g = (v_g*t) % self.max_x
        y_val = np.searchsorted(self.x, point_g)

        point_p = (v_p*t) % self.max_x
        y_val_p = np.searchsorted(self.x, point_p)

        # setting data for all waves
        self.line1.set_data(self.x, y1)
        self.line2.set_data(self.x, y2)
        self.line3.set_data(self.x, y3)
        self.line4.set_data(self.x, sum_y)

        self.point4_p_mv.set_data(point_p, sum_y[y_val_p])
        self.point4_p_st.set_data(point_p, 0)

        self.point4_g_mv.set_data(point_g, sum_y[y_val])
        self.point4_g_st.set_data(point_g, 0)

        return self.line1, self.line2, self.line3, self.line4,


def calc_group_vel(w_arr, k_arr):
    """ w(k) = ak + b ; a - group velocity"""
    w = np.array(w_arr)
    k = np.array(k_arr)
    a, b = np.polyfit(k, w, 1)
    return a


def calc_phase_vel(w_arr, k_arr):
    i, count, sum_v = 0, 0, 0
    while i < len(w_arr):
        if not k_arr[i] == 0:
            sum_v += w_arr[i]/k_arr[i]
            count += 1
        i += 1
    return sum_v/count


class PrepOption:
    """
        Class with one set of already prepared options for default settings for waves.
        Parameters for three waves plotting:
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
