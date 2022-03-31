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
        label = tk.Label(self.root, text="Wave Simulation").grid(column=0, row=0)
        self.fig = anim_fig.fig
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().place(x=0*SIZE, y=0*SIZE)
        self.add_scales()
        self.add_example_buttons()
        #TODO: change below prepoption
        self.sel_option=PrepOption(0, 0, 0, 0, 0, 0, 0)

    def add_scales(self, min_wave_v=0.0, max_wave_v=2.0, min_ang_freq=0.0, max_ang_freq=2.0):
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
        resol = 0.5
        x_cord = int(900*SIZE)
        y_interval = int(50*SIZE)
        s_text = tk.Label(self.root, text="Setting custom w and k")
        s_text.place(x=x_cord-50, y=20)
        #TODO: Adding third wave scales + y cord
        self.wave_v_scale1 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.wave_v_scale1.place(x=x_cord, y=400)
        self.wave_v_scale2 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.wave_v_scale2.place(x=x_cord, y=460)
        self.wave_v_scale3 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.wave_v_scale3.place(x=x_cord, y=500)
        self.ang_freq_scale1 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.ang_freq_scale1.place(x=x_cord, y=520) 
        self.ang_freq_scale2 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.ang_freq_scale2.place(x=x_cord, y=580)
        self.ang_freq_scale3 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.ang_freq_scale3.place(x=x_cord, y=640)

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
        text1 = f"k1 = {option1.wave_v1} k2 = {option1.wave_v2} k3 = {option1.wave_v3} \nw1 = {option1.ang_freq1} w2 = {option1.ang_freq2} w3 = {option1.ang_freq3}"
        text2 = f"k1 = {option2.wave_v1} k2 = {option2.wave_v2} k3 = {option2.wave_v3} \nw1 = {option2.ang_freq1} w2 = {option2.ang_freq2} w3 = {option2.ang_freq3}"
        text3 = f"k1 = {option3.wave_v1} k2 = {option3.wave_v2} k3 = {option3.wave_v3} \nw1 = {option3.ang_freq1} w2 = {option3.ang_freq2} w3 = {option3.ang_freq3}"
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


