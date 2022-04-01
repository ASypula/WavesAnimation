import numpy as np
import matplotlib.animation as animation
from window import WaveAnimation
from animation_plots import WavePlot

colors = ["lightblue", "slateblue", "lightslategray", "black"]
# https://matplotlib.org/stable/gallery/color/named_colors.html

# https://www.youtube.com/watch?v=ePJdV75fT5o
# Liczba fal 2 lub 3 i dla każdej możliwość ustawienia częstości i wektora falowego 
# (omega i k). Zmiana amplitudy i fazy nie jest konieczna. I kilka ciekawych presetów: 
# prędkość grupowa większa, mniejsza lub równa 0. Wydaje mi się, że ta forma prezentacji z nagrania jest idealna 
# (tzn pokazanie przemieszczania stałej fazy i całej grupy za pomocą kropki)



anim_plot = WavePlot(colors)
anim_window = WaveAnimation(anim_plot)


ani = animation.FuncAnimation(anim_window.fig, anim_plot.animate, frames=np.arange(1, 200), interval=25)
anim_plot.pin_window(anim_window)
anim_window.run()
