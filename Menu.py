import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from tkinter import simpledialog
import Strings as s

BACKGROUND = plt.imread(r"C:\Users\AppTa\Pictures\Algorithm Visualizer\1.jpg")
IMG = plt.imread(r"C:\Users\AppTa\Pictures\Algorithm Visualizer\2.jpg")

def h(string):
    """ hash to map the buttons """
    return str(tuple((string[:2]))).replace(' ', '')

class Menu:
    def __init__(self, state='0', title='Algorithm Visualizer', copyright="None", dpi=150):
        self.state = state
        self.title = None
        self.wait = True
        self.start = False
        self.buttons = []
        self.buttons_map = {}
        self.fig = plt.figure(facecolor='k')
        self.init_figure(title + ' Ver: 2.4.9', copyright, dpi)

    def __eq__(self, char):
        return self.state == char

    def init_figure(self, title, copyright, dpi):
        win = self.fig.canvas.manager.window  # figure window
        screen_res = win.wm_maxsize()  # used for window formatting later
        self.fig.set_dpi(dpi)  # set figure resolution
        percent = .96
        self.fig.set_size_inches(percent * (screen_res[0] / dpi), percent * (screen_res[1] / dpi))
        plot_res = self.fig.get_window_extent().bounds  # window extent for centering
        win.wm_geometry('+{0:1.0f}+{1:1.0f}'. \
                        format((screen_res[0] / 2.0) - (plot_res[2] / 2.0),
                               (screen_res[1] / 2.0) - (plot_res[3] / 2.0)))  # centering plot
        self.fig.canvas.toolbar.pack_forget()  # remove toolbar for clean presentation
        self.fig.canvas.set_window_title(title)
        self.fig.canvas.draw()  # draw before loop
        self.init_title(title)
        self.insert_text(0.82, .02, copyright, size=10)
        self.fig.show()

    #  BUTTONS:
    def create_menu_buttons(self):
        colors = ['#2ff4fc', '#00ceec']
        left_buttons = [s.sort_colors, s.num_islands, s.max_profit, s.add_two_huge_numbers, s.rotate_image]
        for i, button in enumerate(left_buttons, 1):
            location = [round(x, 2) for x in [0.2, 0.8 - i * .1, 0.2, 0.05]]
            self.add_button(str(i) + '. ' + button, location, colors[i % 2],
                            self.menu_event, key_value=str(i))

        right_buttons = [s.rotated_array, s.nearest_exit, s.rotate_list, s.calculate_pi, s.container]
        for i, button in enumerate(right_buttons, len(left_buttons) + 1):
            location = [round(x, 2) for x in [0.6, 1.3 - i * .1, 0.2, 0.05]]
            self.add_button(str(i) + '. ' + button, location, colors[i % 2],
                            self.menu_event, key_value=str(i))

        # for exit button:
        self.add_button('Exit', [.4, 0.1, 0.2, 0.05], '#2ff4fc', self.menu_event, key_value='Exit')

    def initial_page(self, title):
        plt.clf()
        self.buttons = []  # clear buttons
        self.insert_image(BACKGROUND, box=(0, 0, 1, 1))
        # Create menu and buttons:
        self.title.set_text(title)

    def main_page(self, title):

        self.clear_buttons()
        self.insert_image(BACKGROUND, box=(0, 0, 1, 1))
        # Create menu and buttons:
        self.set_title(title)
        self.create_menu_buttons()

    def function_page(self, title):
        # remove buttons:
        self.clear_buttons()
        self.title.set_text(title)
        self.add_button('Back', [.05, .88, 0.07, 0.05], '#00ceec', self.menu_event, key_value='0')
        self.add_button('Reset', [0.9, 0.88, 0.07, 0.05], '#00ceec', self.wait_event)
        self.add_button('Start', [0.8, 0.88, 0.07, 0.05], '#00ceec', self.wait_event)

    def set_title(self, title):
        self.title.set_text(title)

    def text_box(self, text, location=(.5, .5), size=12, color='#00ceec'):
        return self.fig.text(location[0], location[1], text, size=size, ha="center", va="center",
                             bbox=dict(boxstyle="round", ec=(0., 0., 0.),  # RGB of frame
                                       fc=color))  # RGB of background

    def clear_buttons(self):
        for button in self.buttons: button[0].remove()
        self.buttons = []

    def insert_text(self, x, y, title, size=32, color='w'):
        text = self.fig.text(x, y, title, fontsize=size, color=color)
        return text

    def init_title(self, title):
        self.title = self.fig.text(0.5, 0.9, title, size=30, ha="center", va="center",
                                   bbox=dict(boxstyle="square", ec=(0., 0., 0.),  # RGB of frame
                                             fc='#2ff4fc'))  # RGB of background

    def add_button(self, name, location, color, event, key_value='?', font_color='#acc5ff'):
        button_ax = self.fig.add_axes(location)
        button = Button(button_ax, name, color=color, hovercolor=font_color)
        self.buttons.append((button_ax, button))
        self.buttons[-1][1].on_clicked(event)
        # crate map: location button -> function number
        self.buttons_map[h(location)] = key_value

    def insert_image(self, img, box=(0.1, 0.1, .8, .8)):
        newax = self.fig.add_axes(box)
        newax.imshow(img)
        newax.axis('off')

    def get_input(self, title, text):
        return simpledialog.askstring(title=title, prompt=text)

    def menu_event(self, event):
        # key extract for hashmap
        key = str(event.inaxes)
        key = key[4:key.find(';')] + ')'
        self.state = self.buttons_map[key]
        self.wait = False

    def wait_event(self, event):
        self.wait = False
