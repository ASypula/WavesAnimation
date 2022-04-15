import matplotlib.animation as animation
from window import WaveAnimation
from animation_plots import WavePlot

# colors for particular waves, https://matplotlib.org/stable/gallery/color/named_colors.html
colors = ["lightblue", "slateblue", "lightslategray", "black"]
# delay between frames in milliseconds
interval = 100

# Polecenie
# https://www.youtube.com/watch?v=ePJdV75fT5o
# Liczba fal 2 lub 3 i dla każdej możliwość ustawienia częstości i wektora falowego 
# (omega i k). Zmiana amplitudy i fazy nie jest konieczna. I kilka ciekawych presetów: 
# prędkość grupowa większa, mniejsza lub równa 0. Wydaje mi się, że ta forma prezentacji z nagrania jest idealna 
# (tzn pokazanie przemieszczania stałej fazy i całej grupy za pomocą kropki)

anim_plot = WavePlot(colors)
anim_window = WaveAnimation(anim_plot)

loop_frames = []
for i in range(3):
    loop_frames += [x for x in range(1000)]

# https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.animation.FuncAnimation.html
ani = animation.FuncAnimation(anim_window.fig, anim_plot.animate, frames=loop_frames, interval=interval)
anim_plot.pin_window(anim_window)
anim_window.run()

#TODO: kropki nie uciekaja z ekranu
# poczatkowe wartosci - uwaga na dzielenie przez zero
# presety gotowe
