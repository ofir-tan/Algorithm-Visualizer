import matplotlib.pyplot as plt
import numpy as np
from numpy import random as rd
import Strings as s
from LinkedList import *
from Widgets import slider

class Algorithms:
    def __init__(self, menu):
        self.menu = menu
        self.n = 10  # input size
        self.path = r"C:\Users\AppTa\Pictures\Algorithm Visualizer\{}.jpg"

    def wait(self):
        return self.menu.wait

    def set_wait(self):
        self.menu.wait = True

    def update(self, val):
        self.n = val

    ### [1] Sort Colors ###
    def sort_colors(self) -> None:
        # a. generate input and vialization objects:

        self.menu.title.set_text(s.sort_colors)
        my_slider, _ = slider(self.update, init=self.n, minval=3, maxval=20)
        inst_text_box = self.menu.text_box(s.inst_sort_colors, [0.5, 0.78])
        while self.wait(): plt.pause(0.0001)
        self.set_wait()

        if self.menu != '0':  # menu == '0' -> Back
            n = self.n
            nums = rd.randint(0, 3, n)
            array_ax = self.menu.fig.add_axes((0.1, 0.1, .8, .8))
            array_ax.axis('off')
            n_text_box = self.menu.text_box(f'n = {n}', [.5, .65], size=32)
            iter_text_box = self.menu.text_box(f'Iteration: 0', [.5, .3], size=32)
            array_ax.imshow(nums.reshape((1, n)), cmap='brg')

            # b. algorithm starts here:
            l = f = 0
            r = len(nums) - 1
            while f <= r:
                if nums[f] == 0:
                    nums[l], nums[f] = nums[f], nums[l]
                    l += 1
                elif nums[f] == 2:
                    nums[r], nums[f] = nums[f], nums[r]
                    f -= 1
                    r -= 1
                f += 1
                # draw array:
                array_ax.imshow(nums.reshape((1, n)), cmap='brg')
                iter_text_box.set_text(f'Iteration: {f}')
                plt.pause(.15)
            # c. algorithm ends here
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            array_ax.remove()
            n_text_box.remove()
            iter_text_box.remove()
        inst_text_box.remove()
        my_slider.remove()

    ### [2] Number of Islands ###
    def grid_bfs(self, grid, source, directions=((-1, 0), (1, 0), (0, -1), (0, 1))):
        def in_grid():
            nonlocal xx, yy, grid
            return (0 <= xx < len(grid)) and (0 <= yy < len(grid[xx]))

        # bfs:
        q = [source]  # queue initialization
        grid[source[0]][source[1]] = 1  # mark as visited
        while q:
            x, y = q.pop(0)
            # visit the neighbors:
            for dx, dy in directions:
                xx, yy = x + dx, y + dy
                if in_grid() and grid[xx][yy] == 2:
                    q.append((xx, yy))
                    grid[xx][yy] = 1  # mark as visited

    def num_islands(self):
        # a. generate input and vialization objects:

        self.menu.title.set_text(s.num_islands)
        my_slider, _ = slider(self.update, init=self.n, minval=4, maxval=20)
        inst_text_box = self.menu.text_box(s.inst_num_islands, [0.5, 0.78])
        while self.wait(): plt.pause(0.0001)
        self.set_wait()

        if self.menu != '0':  # menu == '0' -> Back
            iter_text_box = self.menu.text_box(f'Iteration: 0', [.5, .1], size=32)
            grid = rd.choice([0, 2], (self.n, self.n))
            grix_ax = self.menu.fig.add_axes((0.25, .2, .5, .5))
            grix_ax.axis('off')
            grix_ax.imshow(grid, cmap='jet')

            # b. algorithm starts here
            islands = 0
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] == 2:
                        # BFS
                        self.grid_bfs(grid, (x, y))
                        islands += 1
                        # display grid:
                        plt.pause(.15)
                        grix_ax.imshow(grid, cmap='jet')
                        iter_text_box.set_text(f'Islands: {islands}')

            # c. algorithm ends here
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            grix_ax.remove()
            iter_text_box.remove()
        inst_text_box.remove()
        my_slider.remove()

    ### [3] Max Profit ###
    def max_profit(self):
        # a. generate input and vialization objects:

        self.menu.title.set_text(s.max_profit)
        my_slider, _ = slider(self.update, init=self.n, minval=1, maxval=15)
        inst_text_box = self.menu.text_box(s.inst_max_profit, [0.5, 0.78])
        while self.wait(): plt.pause(0.0001)
        self.set_wait()
        if self.menu != '0':  # menu == '0' -> Back
            iter_text_box = self.menu.text_box(f'Iteration: 0', [.5, .1], size=32)
            prices = rd.randint(0, 15, self.n)
            grix_ax = self.menu.fig.add_axes((0.25, .2, .5, .5))
            grix_ax.plot(prices, label='prices')
            grix_ax.grid()
            grix_ax.tick_params(colors='w', which='both', labelsize=12)
            buy_line = grix_ax.axvline(x=0, color='r', label='Buy')
            sell_line = grix_ax.axvline(x=0, color='g', label='Sell')
            grix_ax.legend()

            # b. algorithm starts here:
            max_pro = l = 0
            for r in range(len(prices)):
                max_pro = max(max_pro, prices[r] - prices[l])
                l = r if prices[r] < prices[l] else l
                # update display:
                buy_line.set_xdata(l)
                sell_line.set_xdata(r)
                iter_text_box.set_text(f'iteration: {r}, Max Profit = {max_pro}')
                plt.pause(.15)

            # c. algorithm ends here
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            grix_ax.remove()
            iter_text_box.remove()
        inst_text_box.remove()
        my_slider.remove()

    ### [4] Rotated Sorted Array ###

    def binary_search(self, nums, l, r, target):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    def rotated_sorted_array(self):
        # a. generate input and vialization objects:

        self.menu.title.set_text(s.inst_rotated_array)
        my_slider, _ = slider(self.update, init=self.n, minval=0, maxval=2048, valstep=256)
        inst_text_box = self.menu.text_box(s.inst_rotated_array, [0.5, 0.78])
        while self.wait(): plt.pause(0.0001)
        self.set_wait()

        if self.menu != '0':  # menu == '0' -> Back
            n = self.n
            nums = np.arange(n)
            k = rd.randint(0, n)
            nums = np.r_[nums[k:], nums[:k]]
            target = nums[n // 3]
            iter_text_box = self.menu.text_box(f'Iteration: 0, Target: {target}', [.5, .1], size=32)
            plot_ax = self.menu.fig.add_axes((0.25, .2, .5, .5))
            plot_ax.plot(nums, label='array')
            plot_ax.grid()
            plot_ax.tick_params(colors='w', which='both', labelsize=12)
            plot_ax.axvline(x=n // 3, linewidth=4, linestyle="--", color='b', label='target')
            r_line = plot_ax.axvline(x=0, color='g', label='right ptr')
            l_line = plot_ax.axvline(x=0, color='y', label='left ptr')
            m_line = plot_ax.axvline(x=0, color='r', label='middle ptr')
            plot_ax.legend()

            # b. algorithm starts here:
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
            l = 0
            r = len(nums) - 1
            iteration = 0
            while l <= r:
                m = (l + r) // 2
                # update display:
                m_line.set_xdata(m)
                r_line.set_xdata(r)
                l_line.set_xdata(l)
                iteration += 1
                iter_text_box.set_text(f'iteration: {iteration}, Target: {target}')
                plt.pause(.5)
                ## iteration:

                if nums[m] == target:
                    break

                if nums[m] >= nums[l]:
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1

            # c. algorithm ends here
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            plot_ax.remove()
            iter_text_box.remove()
        inst_text_box.remove()
        my_slider.remove()

    ### [5] Nearest Exit ###
    def nearest_exit(self, ):
        # a. generate input and vialization objects:

        self.menu.title.set_text(s.nearest_exit)
        my_slider, _ = slider(self.update, init=self.n, minval=4, maxval=30)
        inst_text_box = self.menu.text_box(s.inst_nearest_exit, [0.5, 0.78])
        while self.wait(): plt.pause(0.0001)
        self.set_wait()
        if self.menu != '0':  # menu == '0' -> Back
            steps_text_box = self.menu.text_box(f'Steps: 0', [.5, .1], size=32)
            n = self.n
            grid = rd.choice([0, 4], (n, n))
            source = rd.randint(3, n - 3, 2)
            grid[source[0]][source[1]] = 1
            grix_ax = self.menu.fig.add_axes((0.25, .2, .5, .5))
            grix_ax.axis('off')
            grix_ax.imshow(grid)

            # b. algorithm starts here:
            def in_grid():
                nonlocal xx, yy, grid
                return (0 <= xx < len(grid)) and (0 <= yy < len(grid[xx]))

            def print_path(d, p):
                path = []
                while d[p] is not None:
                    path.insert(0, p)
                    p = d[p]
                for i, (x, y) in enumerate(path, 1):
                    grid[x][y] = 3
                    plt.pause(.2)
                    grix_ax.imshow(grid)
                    steps_text_box.set_text(f'Steps: {i}')

            path = {}
            # bfs:
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            q = [source]  # queue initialization
            path[(source[0], source[1])] = None
            exit_found = False
            while q:
                level = len(q)
                while level:
                    level -= 1
                    x, y = q.pop(0)
                    # if we found the exit:
                    if x in [0, len(grid) - 1] or y in [0, len(grid[x]) - 1]:
                        exit_found = True
                        print_path(path, (x, y))
                        q = []
                        break
                    # visit the neighbors:
                    for dx, dy in directions:
                        xx, yy = x + dx, y + dy
                        if in_grid() and grid[xx][yy] == 0 and (xx, yy) not in path:
                            q.append((xx, yy))
                            path[(xx, yy)] = (x, y)

            if not exit_found:
                steps_text_box.set_text("Can't find the exit!")
            # c. algorithm ends here
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            grix_ax.remove()
            steps_text_box.remove()
        inst_text_box.remove()
        my_slider.remove()

    ### [6] Rotate List ###
    def rotate_list(self):
        # a. generate input and vialization objects:

        self.menu.title.set_text(s.rotate_list)
        my_slider, _ = slider(self.update, init=self.n, minval=1, maxval=15)
        inst_text_box = self.menu.text_box(s.inst_rotate_list, [0.5, 0.78], size=20)
        if self.menu != '0':  # menu == '0' -> Back
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            n = self.n
            nums = np.arange(1, n + 1)
            rd.shuffle(nums)
            lst = LinkedList(list(nums))
            k = rd.randint(1, n * 10)
            input_text_box = self.menu.text_box(f"Input: {lst}\nn = {n}, k = {k}", location=(.5, .6), size=20)

            # b. algorithm starts here:
            length = len(lst)
            k = k % length
            if k != 0:
                node = lst[-k]  # get the kth node from the end
                new_head = node.next
                node.next = None
                temp = new_head
                while temp and temp.next: temp = temp.next
                temp.next = lst.head
                lst.head = new_head
            # c. algorithm ends here
            out_text_box = self.menu.text_box(f"Output: {lst}", location=(.5, .4), size=20, color="#2ff4fc")
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            input_text_box.remove()
            out_text_box.remove()
        inst_text_box.remove()
        my_slider.remove()

    ### [7] Add Two Huge Numbers ###
    def add_two_huge_numbers(self):

        # a. generate input and vialization objects:
        MAX = 10
        self.menu.title.set_text(s.add_two_huge_numbers)
        my_slider, _ = slider(self.update, init=self.n, minval=1, maxval=15)
        inst_text_box = self.menu.text_box(s.inst_add_two, [0.5, 0.78])
        while self.wait(): plt.pause(0.0001)
        self.set_wait()
        if self.menu != '0':  # menu == '0' -> Back
            a = LinkedList(list(rd.randint(1, MAX, rd.randint(1, self.n))))
            b = LinkedList(list(rd.randint(1, MAX, rd.randint(1, self.n))))
            input_text_box = self.menu.text_box(f"First List:  {a}\n"
                                                f"Second List: {b}", location=(.5, .6), size=24)

            # b. algorithm starts here:
            a.reverse()
            b.reverse()
            # diplay step one:
            step_text_box = self.menu.text_box("Step 1 - reverse lists:\n"
                                               f"First List:  {a}\n"
                                               f"Second List: {b}", location=(.5, .4), size=24)
            c = prev = None
            rest = 0
            a, b = a.head, b.head
            while a or b:
                value = rest
                if a: value += a.val
                if b: value += b.val

                x = value % MAX
                rest = value // MAX
                c = ListNode(x)
                c.next = prev
                prev = c
                if a: a = a.next
                if b: b = b.next

            if rest:  # if there is a residue
                c = ListNode(rest)
                c.next = prev

            c = LinkedList(head=c)

            # c. algorithm ends here
            out_text_box = self.menu.text_box(f"Sum: {c}", location=(.5, .2), size=24, color="#2ff4fc")
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            input_text_box.remove()
            step_text_box.remove()
            out_text_box.remove()
        my_slider.remove()
        inst_text_box.remove()

        ### [8] Rotate Image ###

    def rotate_image(self):
        # a. generate input and vialization objects:
        self.menu.title.set_text(s.rotate_image)
        inst_text_box = self.menu.text_box(s.inst_rotate_image, [0.5, 0.78])
        matrix = plt.imread(self.path.format("rotate"))
        matrix = matrix.copy()
        grix_ax = self.menu.fig.add_axes((0.25, .2, .5, .5))
        grix_ax.axis('off')
        grix_ax.imshow(matrix)
        while self.wait(): plt.pause(0.00001)
        self.set_wait()

        while self.menu != '0':  # menu == '0' -> Back
            # b. algorithm starts here
            def transpose(m):
                for i in range(len(m)):
                    for j in range(i, len(m[i])):
                        m[i][j], m[j][i] = m[j][i], m[i][j]

            def reverse(m):
                N = len(m)
                for i in range(len(m)):
                    for j in range(len(m[i]) // 2):
                        m[i][j], m[i][N - j - 1] = m[i][N - j - 1], m[i][j]

            transpose(matrix)
            reverse(matrix)
            plt.pause(1)
            grix_ax.imshow(matrix)
            # c. algorithm ends here
        grix_ax.remove()
        inst_text_box.remove()

    ### [9] Calculate Pi ###
    def calculate_pi(self):
        # a. generate input and vialization objects:

        self.menu.title.set_text(s.calculate_pi)
        my_slider, _ = slider(self.update, init=self.n, minval=100000, maxval=10 ** 6, valstep=100000)
        inst_text_box = self.menu.text_box(s.inst_calculate_pi, [0.5, 0.78], size=20)

        if self.menu != '0':  # menu == '0' -> Back
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            plot_ax = self.menu.fig.add_axes((0.25, .2, .5, .5))
            point_text_box = self.menu.text_box(f'Points: 0', [.5, .7], size=20)
            pi_text_box = self.menu.text_box(f'Estimated π: 0', [.5, .1], size=28)
            x = np.arange(0, 1, .001)
            y = np.sqrt(1 - x ** 2)
            plot_ax.plot(x, y)
            plot_ax.axvline(x=1, color='k')
            plot_ax.axhline(y=1, color='k')
            plot_ax.grid()
            plot_ax.tick_params(colors='r', which='both', labelsize=12)

            # b. algorithm starts here:
            inside = 0
            xx = np.array(0)
            yy = np.array(0)
            for point in range(1, self.n + 1):
                x = rd.random()
                y = rd.random()
                if x ** 2 + y ** 2 < 1:
                    inside += 1
                # update points (x)
                if self.n > 1000 and point % (self.n // 1000) == 0:
                    xx = np.c_[xx, x]
                    yy = np.c_[yy, y]
                # update π text box (10 times for each run)
                if point % (self.n // 10) == 0 or point == self.n:
                    plt.pause(0.1)
                    plot_ax.plot(xx, yy, 'xr')
                    xx = np.array(0)
                    yy = np.array(0)
                    estimated_pi = round(inside / self.n * 4, 6)
                    point_text_box.set_text(f'Points: {point}')
                    pi_text_box.set_text(f'Estimated π: {estimated_pi}')

            # c. algorithm ends here
            while self.wait(): plt.pause(0.0001)
            self.set_wait()
            point_text_box.remove()
            pi_text_box.remove()
            plot_ax.remove()
        inst_text_box.remove()
        my_slider.remove()

    ### [10] Game of Life ###
    def game_of_life(self):
        # a. generate input and vialization objects:
        self.menu.title.set_text(s.game_of_life)
        inst_text_box = self.menu.text_box(s.game_of_life, [0.5, 0.78])
        while self.wait(): plt.pause(0.0001)
        self.set_wait()
        (ROWS, COLS) = 50, 100
        iterations = 30
        if self.menu != '0':  # menu == '0' -> Back
            iter_text_box = self.menu.text_box(f'Iteration: 0', [.5, .1], size=32)
            board = rd.choice([0, 1], size=(ROWS, COLS), p=(.7, .3))
            grix_ax = self.menu.fig.add_axes((-1, .1, 3, .7))
            grix_ax.axis('off')
            grix_ax.imshow(board, cmap='summer')

            # b. algorithm starts here:
            for iteration in range(iterations):
                def get_neighbors(self):
                    nonlocal i, j, board
                    neighbors = 0

                    def in_grid():
                        nonlocal xx, yy, board
                        return (0 <= xx < len(board)) and (0 <= yy < len(board[xx]))

                    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1))
                    for dx, dy in offsets:
                        xx, yy = i + dx, j + dy
                        if in_grid() and board[xx][yy]:
                            neighbors += 1
                    return neighbors

                ans = [[0] * len(board[0]) for _ in range(len(board))]

                for i in range(len(board)):
                    for j in range(len(board[i])):
                        n = get_neighbors((i, j))
                        if board[i][j]:  # if live
                            if n < 2 or n > 3:
                                ans[i][j] = 0
                            else:
                                ans[i][j] = 1
                        elif n == 3:
                            ans[i][j] = 1
                        else:
                            ans[i][j] = 0

                for i in range(len(board)):
                    for j in range(len(board[i])):
                        board[i][j] = ans[i][j]

                grix_ax.imshow(board, cmap='summer')
                iter_text_box.set_text(iteration)
                plt.pause(.00000000001)
            # c. algorithm ends here
            while self.wait(): plt.pause(.00001)
            self.set_wait()
            grix_ax.remove()
            iter_text_box.remove()
        inst_text_box.remove()
