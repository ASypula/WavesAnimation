import matplotlib.animation as animation
from window import WaveAnimation
from animation_plots import WavePlot

# colors for particular waves, https://matplotlib.org/stable/gallery/color/named_colors.html
colors = ["lightblue", "slateblue", "lightslategray", "black"]

# delay between frames in milliseconds
interval = 100
plot_size = (8, 6)

anim_plot = WavePlot(colors)
anim_window = WaveAnimation(anim_plot, plot_size)

loop_frames = []
for i in range(3):
    loop_frames += [x for x in range(1000)]

# documentation for FuncAnimation function https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.animation.FuncAnimation.html
ani = animation.FuncAnimation(anim_window.fig, anim_plot.animate, frames=loop_frames, interval=interval)
anim_plot.pin_window(anim_window)
anim_window.run()
