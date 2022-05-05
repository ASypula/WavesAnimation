import numpy as np
import matplotlib.pyplot as plt

import sys
np.set_printoptions(threshold=sys.maxsize)

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
        self.w_p, self.k_p = 0, 0
        self.max_x = max_x
        self.max_x_p = max_x
        self.max_x_g = max_x

        # TODO: changes
        self.changed_params = True      # indicates whether any parameters: w or k were changed during given iteration
        self.previous_params = [0, 0, 0, 0, 0, 0]
        self.curr_y = 0
        self.idx_y_vel_g = 0
        self.min_idx = 0
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

        self.point4_p, = ax4.plot([], [], 'r', **kw1)

        # a dot for group velocity moving in the y-axis
        self.point4_g_mv, = ax4.plot([], [], 'blue', **kw1)

        # a dot for group velocity with constant y-axis value
        self.point4_g_st, = ax4.plot([], [], 'black', **kw1)


    def pin_window(self, window):
        self.win = window

    def animate(self, i):
        """ Method for waves animation
            waves' parameters are continuously being taken from the values
            set by the user through GUI
            @param i: consecutive integers starting from 0 -> frames numeration """

        # taking waves' w and k from the scales if custom options selected
        if self.win.sel_option.value == 0:
            w1 = self.win.ang_freq_scale1.get()
            w2 = self.win.ang_freq_scale2.get()
            w3 = self.win.ang_freq_scale3.get()
            k1 = self.win.wave_v_scale1.get()
            k2 = self.win.wave_v_scale2.get()
            k3 = self.win.wave_v_scale3.get()


        # taking waves' w and k from the selected preset option
        else:
            w1 = self.win.sel_option.ang_freq1
            w2 = self.win.sel_option.ang_freq2
            w3 = self.win.sel_option.ang_freq3
            k1 = self.win.sel_option.wave_v1
            k2 = self.win.sel_option.wave_v2
            k3 = self.win.sel_option.wave_v3
      
        dt = 0.1
        t = i * dt
        y1 = self.A*np.cos(k1 * self.x - w1 * t)
        y2 = self.A*np.cos(k2 * self.x - w2 * t)
        y3 = self.A*np.cos(k3 * self.x - w3 * t)

        sum_y = y1 + y2 + y3

        if not w1 and not w2 and not w3:
            v_g = 0
        else:
            v_g = calc_group_vel(w1, w2, w3, k1, k2, k3)

        point_g = (v_g*t) % self.max_x
        y_val = np.searchsorted(self.x, point_g)

        # TODO: changes
        new_params = [w1, w2, w3, k1, k2, k3]
        self.just_changed = not np.array_equal(self.previous_params, new_params)
        print(f"{t}, {self.just_changed}")
        if self.just_changed:
            self.curr_y = sum_y[self.idx_y_vel_g]
            self.min_idx = 0
        else:
            absolute_val_array = get_array(sum_y, self.curr_y, self.min_idx, 3, 10)
            self.min_idx = absolute_val_array.argmin()
            #print(f"Previous: {self.curr_val}")
            self.curr_val = sum_y[self.min_idx]
            print(f"Idx: {self.min_idx}")
            print(sum_y[self.min_idx-5: self.min_idx+5])
            print(f"Current value = {self.curr_val}")
        point_p = self.x[self.min_idx%len(self.x)]




        #     while i < 10:
        #         if sum_y[self.idx_y_vel_g] == self.curr_y:
        #             break    
        #         self.idx_y_vel_g += 1
        #         i+=1
        #     if self.idx_y_vel_g == len(sum_y):
        #         self.idx_y_vel_g = 0
        #     self.curr_y = sum_y[self.idx_y_vel_g]

        self.previous_params = new_params
        self.min_idx = self.min_idx%len(self.x)
        # if k1+k2+k3 == 0:
        #     point_p = 0
        # else:
        #     point_p = t*(w1+w2+w3/(k1+k2+k3))
        point_p = self.x[self.min_idx]   

        # setting data for all waves
        self.line1.set_data(self.x, y1)
        self.line2.set_data(self.x, y2)
        self.line3.set_data(self.x, y3)
        self.line4.set_data(self.x, sum_y)

        #self.point4_p_mv.set_data(point_p, sum_y[y_val])
        self.point4_p.set_data(point_p, 0)
        self.point4_g_mv.set_data(point_g, sum_y[y_val])
        self.point4_g_st.set_data(point_g, 0)

        return self.line1, self.line2, self.line3, self.line4, self.point4_p

def get_array(arr, value, idx, interval, fill_val):
    result_arr = np.abs(arr - value)
    if idx-interval < 0:
        beg = idx + interval
        end = len(arr)+idx - interval
        result_arr[beg+1:end] = fill_val
    elif idx + interval >= len(arr):
        beg = interval + idx - len(arr)
        end = idx - interval
        result_arr[beg+1:end] = fill_val
    else:
        result_arr[:idx] = fill_val
        # result_arr[:idx - interval] = fill_val
        result_arr[idx + interval+1:] = fill_val
    return result_arr


def calc_group_vel(w1, w2, w3, k1, k2, k3):
    """ w(k) = ak + b ; a - group velocity"""
    w = np.array([w1, w2, w3])
    k = np.array([k1, k2, k3])
    a, b = np.polyfit(k, w, 1)
    return a


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
