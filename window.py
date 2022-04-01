from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from animation_plots import PrepOption

SIZE = 1.1

class WaveAnimation:
    def __init__(self, anim_fig):
        self.root = tk.Tk()
        self.root.geometry(f"{int(1200*SIZE)}x{int(700*SIZE)}")
        label = tk.Label(self.root, text="Wave Simulation").place(x=0, y=0)
        self.fig = anim_fig.fig
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().place(x=0*SIZE, y=0*SIZE)
        self.add_scales()
        self.add_example_buttons()
        #TODO: change below prepoption
        self.sel_option=PrepOption(0, 0, 0, 0, 0, 0, 0)

    def add_scales(self, min_wave_v=-1.0, max_wave_v=1.0, min_ang_freq=-1.0, max_ang_freq=1.0):
        """
            Adds scales to the window that control:
                - wave vector: wave_v_scale
                - temporal angular frequency of the waves: ang_freq_scale
            @param min_wave_v: minimum value for wave vector
            @param max_wave_v: maximum value for wave vector
            @param min_ang_freq: minimum value for angular frequency
            @param max_ang_freq: maximum value for angular frequency
        """
        t_intrvl = 0.5
        resol = 0.1
        x_cord_k = int(850*SIZE)
        x_cord_w = int(1000*SIZE)
        y_beg = 350
        y_interval = int(70*SIZE)
        s_text = tk.Label(self.root, text="Setting custom k and w")
        s_text.place(x=x_cord_k-20, y=300)
        slider_len = 150
        #TODO: Adding third wave scales + y cord
        self.wave_v_scale1 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL, label="k1", length=slider_len)
        self.wave_v_scale1.place(x=x_cord_k, y=y_beg)
        self.wave_v_scale2 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL, label="k2", length=slider_len)
        self.wave_v_scale2.place(x=x_cord_k, y=y_beg+y_interval)
        self.wave_v_scale3 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL, label="k3", length=slider_len)
        self.wave_v_scale3.place(x=x_cord_k, y=y_beg+2*y_interval)
        self.ang_freq_scale1 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL, label="w1", length=slider_len)
        self.ang_freq_scale1.place(x=x_cord_w, y=y_beg) 
        self.ang_freq_scale2 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL, label="w2", length=slider_len)
        self.ang_freq_scale2.place(x=x_cord_w, y=y_beg+y_interval)
        self.ang_freq_scale3 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL, label="w3", length=slider_len)
        self.ang_freq_scale3.place(x=x_cord_w, y=y_beg+2*y_interval)

    def add_example_buttons(self):
        x_cord = int(900*SIZE)
        y_interval = int(50*SIZE)
        l_text = tk.Label(self.root, text="Choosing custom or preset options:")
        l_text.place(x=x_cord-50, y=20)
        # l.config(font =("Courier", 14))
        self.var = tk.IntVar()
        # PrepOption(wave_v_1, ang_freq_1, wave_v_2, ang_freq_2, wave_v_3, ang_freq_3, val)
        option0 = PrepOption(0, 0, 0, 0, 0, 0, 0)
        option1 = PrepOption(-1, 1, 2, 2, 1, 1, 1)
        option2 = PrepOption(6, 1, 2, 2, 1, 1, 2)
        option3 = PrepOption(1, 1, 2, 2, 0, 0, 3)
        # button 0 used for custom settings through scales
        text0 = f"Custom parameters"
        text1 = f"k1  = {option1.wave_v1} \tk2  = {option1.wave_v2} \tk3  = {option1.wave_v3} \nw1 = {option1.ang_freq1} \tw2 = {option1.ang_freq2} \tw3 = {option1.ang_freq3}"
        text2 = f"k1  = {option2.wave_v1} \tk2  = {option2.wave_v2} \tk3  = {option2.wave_v3} \nw1 = {option2.ang_freq1} \tw2 = {option2.ang_freq2} \tw3 = {option2.ang_freq3}"
        text3 = f"k1  = {option3.wave_v1} \tk2  = {option3.wave_v2} \tk3  = {option3.wave_v3} \nw1 = {option3.ang_freq1} \tw2 = {option3.ang_freq2} \tw3 = {option3.ang_freq3}"
        opt_but0 = tk.Radiobutton(self.root, text=text0, variable=self.var, value=option0.value, command=self.on_select_button)
        opt_but1 = tk.Radiobutton(self.root, text=text1, variable=self.var, value=option1.value, command=self.on_select_button)
        opt_but2 = tk.Radiobutton(self.root, text=text2, variable=self.var, value=option2.value, command=self.on_select_button)
        opt_but3 = tk.Radiobutton(self.root, text=text3, variable=self.var, value=option3.value, command=self.on_select_button)
        opt_but0.place(x=x_cord, y=y_interval*1)
        opt_but1.place(x=x_cord, y=y_interval*2)
        opt_but2.place(x=x_cord, y=y_interval*3)
        opt_but3.place(x=x_cord, y=y_interval*4)
        self.options = [option0, option1, option2, option3]

    def on_select_button(self):
        self.sel_option = self.options[self.var.get()]

    def run(self):
        tk.mainloop()


