from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from window import WaveAnimation
from animation_plots import WavePlot

# https://www.youtube.com/watch?v=ePJdV75fT5o
# Liczba fal 2 lub 3 i dla każdej możliwość ustawienia częstości i wektora falowego 
# (omega i k). Zmiana amplitudy i fazy nie jest konieczna. I kilka ciekawych presetów: 
# prędkość grupowa większa, mniejsza lub równa 0. Wydaje mi się, że ta forma prezentacji z nagrania jest idealna 
# (tzn pokazanie przemieszczania stałej fazy i całej grupy za pomocą kropki)


# Wave 1.
k1, w1 = 10., 5.
c1 = w1 / k1

# Wave 2.
k2, w2 = 3., 4.5
c2 = w2 / k2

cg = (w2 - w1) / (k2 - k1)
cgc = (w2 + w1) / (k2 + k1)

deltg = 10 if cg <= 0 else 10.

x = np.arange(0, 10*np.pi, 0.01)        # x-array

anim_plot = WavePlot()
anim_window = WaveAnimation(anim_plot)


ani = animation.FuncAnimation(anim_window.fig, anim_plot.animate, frames=np.arange(1, 200), interval=25, blit=False)
anim_plot.pin_window(anim_window)
#anim_plot.draw()
anim_window.run()
