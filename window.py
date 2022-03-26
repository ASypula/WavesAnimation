from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from animation_plots import PrepOption

SIZE = 1

class WaveAnimation:
    def __init__(self, anim_fig):
        self.root = tk.Tk()
        self.root.geometry(f"{1200*SIZE}x{800*SIZE}")
        label = tk.Label(self.root, text="Wave Simulation").grid(column=0, row=0)
        self.fig = anim_fig.fig
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().place(x=0*SIZE, y=0*SIZE)
        self.add_scales()
        self.add_example_buttons()
        #TODO: change below prepoption
        self.sel_option=PrepOption(0, 0, 0, 0, 0)

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
        self.wave_v_scale1 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.wave_v_scale1.place(x=900, y=400)
        self.wave_v_scale2 = tk.Scale(master=self.root, from_=min_wave_v, to=max_wave_v, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.wave_v_scale2.place(x=900, y=460)
        self.ang_freq_scale1 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.ang_freq_scale1.place(x=900, y=520) 
        self.ang_freq_scale2 = tk.Scale(master=self.root, from_=min_ang_freq, to=max_ang_freq, tickinterval=t_intrvl, resolution=resol, orient=tk.HORIZONTAL)
        self.ang_freq_scale2.place(x=900, y=580)

    def add_example_buttons(self):
        self.var = tk.IntVar()
        # PrepOption(wave_v_1, ang_freq_1, wave_v_2, ang_freq_2, val)
        option0 = PrepOption(0, 0, 0, 0, 0)
        option1 = PrepOption(-1, 1, 2, 2, 1)
        option2 = PrepOption(6, 1, 2, 2, 2)
        option3 = PrepOption(1, 1, 2, 2, 3)
        #button 0 used for custom settings through scales
        text0 = f"Custom parameters"
        text1 = f"k1 = {option1.wave_v1}, w1 = {option1.ang_freq1}\nk2 = {option1.wave_v2}, w2 = {option1.ang_freq2}"
        text2 = f"k1 = {option2.wave_v1}, w1 = {option2.ang_freq1}\nk2 = {option2.wave_v2}, w2 = {option2.ang_freq2}"
        text3 = f"k1 = {option3.wave_v1}, w1 = {option3.ang_freq1}\nk2 = {option3.wave_v2}, w2 = {option3.ang_freq2}"
        opt_but0 = tk.Radiobutton(self.root, text=text0, variable=self.var, value=option0.value, command=self.on_select_button)
        opt_but1 = tk.Radiobutton(self.root, text=text1, variable=self.var, value=option1.value, command=self.on_select_button)
        opt_but2 = tk.Radiobutton(self.root, text=text2, variable=self.var, value=option2.value, command=self.on_select_button)
        opt_but3 = tk.Radiobutton(self.root, text=text3, variable=self.var, value=option3.value, command=self.on_select_button)
        opt_but0.place(x=900, y=0)
        opt_but1.place(x=900, y=70)
        opt_but2.place(x=900, y=140)
        opt_but3.place(x=900, y=210)
        self.options = [option0, option1, option2, option3]

    def on_select_button(self):
        self.sel_option = self.options[self.var.get()]

    def run(self):
        tk.mainloop()


