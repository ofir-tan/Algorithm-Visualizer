import matplotlib

matplotlib.use('TkAgg')
from Menu import *
import tkinter as tk
import Strings as s
from Algorithms import Algorithms

ROOT = tk.Tk()
ROOT.withdraw()

def main():
    menu = Menu(state='0', title='Algorithm Visualizer', copyright=s.COPYRIGHT)
    algo = Algorithms(menu)
    while True:

        # Menu State Machine:
        if menu == '0':
            menu.main_page('$\mathtt{Algorithm\ Visualizer}$')
            while menu == '0': plt.pause(0.00001)
            menu.wait = True
        else:
            menu.function_page()
            # 1. Sort Color's:
            if menu == '1':
                algo.sort_colors()
            elif menu == '2':
                algo.num_islands()
            elif menu == '3':
                algo.max_profit()
            elif menu == '4':
                algo.add_two_huge_numbers()
            elif menu == '5':
                algo.rotate_image()
            elif menu == '6':
                algo.rotated_sorted_array()
            elif menu == '7':
                algo.nearest_exit()
            elif menu == '8':
                algo.rotate_list()
            elif menu == '9':
                algo.calculate_pi()
            elif menu == '10':
                algo.game_of_life()
            # Exit the program:
            elif menu == 'Exit':
                plt.pause(.25)
                plt.close()
                break
            plt.pause(0.0001)

if __name__ == "__main__":
    main()
