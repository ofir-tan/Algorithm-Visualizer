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
            while menu == '0':
                plt.pause(0.001)
                continue
            menu.wait = True
        # 1. Sort Color's:
        elif menu == '1':
            menu.function_page(s.sort_colors)
            algo.sort_colors()
        elif menu == '2':
            menu.function_page(s.num_islands)
            algo.numIslands()
        elif menu == '3':
            menu.function_page(s.max_profit)
            algo.maxProfit()
        elif menu == '4':
            menu.function_page(s.add_two_huge_numbers)
            algo.add_two_huge_numbers()
        elif menu == '5':
            menu.function_page(s.rotate_image)
            algo.rotate_image()
        elif menu == '6':
            menu.function_page(s.rotated_array)
            algo.rotated_sorted_array()
        elif menu == '7':
            menu.function_page(s.nearest_exit)
            algo.nearest_exit()
        elif menu == '8':
            menu.function_page(s.rotate_list)
            algo.rotate_list()
        elif menu == '9':
            menu.function_page(s.calculate_pi)
            algo.calculate_pi()
        elif menu == '10':
            pass
        # Exit the program:
        elif menu == 'Exit':
            plt.pause(.25)
            plt.close()
            break
        plt.pause(0.0001)

if __name__ == "__main__":
    main()
