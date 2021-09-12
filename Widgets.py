from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

def slider(f, init=10, minval=1, maxval=20, valstep=1):
    # Make a vertically oriented slider to control the amplitude
    axsize = plt.axes([0.07, 0.18, 0.022, 0.5], facecolor='#00ceec')
    size_slider = Slider(
        ax=axsize,
        label="n",
        color='#005784',
        valstep=valstep,
        valmin=minval,
        valmax=maxval,
        valinit=init,
        orientation="vertical"
    )
    size_slider.label.set_color('#00ceec')
    size_slider.label.set_size(20)
    size_slider.valtext.set_color('#00ceec')
    size_slider.valtext.set_size(20)

    # The function to be called anytime a slider's value changes

    # register the update function with each slider
    size_slider.on_changed(f)
    return axsize, size_slider