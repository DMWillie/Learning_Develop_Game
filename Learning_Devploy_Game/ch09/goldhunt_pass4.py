"""
    作者:北辰
    日期:03/06/2019
    功能:兽人之袭游戏中的寻找黄金场景
    版本:4.0.0
    1.0.0改进之处:优化find_coins方法中的距离计算,加快程序运行速度
    2.0.0改进之处:避免函数重新评估(跳过点操作)来加快循环的运行速度
    3.0.0改进之处:将generate_random_points方法中调用的内置函数替换为本地函数加快运行速度
    4.0.0改进之处:使用numpy来优化generate_random_points函数
"""

import random
import math
import cProfile
import pstats
import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    msg = "You won't be able to visualize the random point distribution."
    print("ImportError: matplotlib.pyplot ", msg)


def plot_points(ref_radius, x_coords, y_coords):
    """Utility function to show the 'Gold Field!

    :param float ref_radius: Reference radius to determine axis limits
    :param list x_coords: X coordinates of the points to be plotted
    :param list y_coords: Y coordinates of the points to be plotted
    """
    # Define axis limits
    a1 = ref_radius + 1
    a2 = a1*(-1.0)
    plt.plot(x_coords, y_coords, ".", color='#A67C00', ms=4)
    plt.axis([a2, a1, a2, a1])
    plt.show()


# Enable the @profile decorator only when you are running line_profiler
# or memory_profiler. Otherwise it will throw an error.
#@profile
def generate_random_points(ref_radius, total_points):
    """Return x, y coordinate lists representing random points inside a circle.

    Generates random points inside a circle with center at (0,0). For any point
    it randomly picks a radius between 0 and ref_radius.

    :param ref_radius: The random point lies between 0 and this radius.
    :param total_points: total number of random points to be created
    :return: x and y coordinates as lists

    .. note:: This function shows an inefficient way of generating random
            points. In the next few chapters, the book will show a better
            way of writing this code.
    .. todo:: Refactor! Move the function to a module like gameutilities.py
    """
    x = []
    y = []
    show_plot = False
    # Combination of avoiding the dots (function reevaluations)
    # and using local variable
    l_unifrom = np.random.uniform
    l_sqrt = np.sqrt
    l_pi = np.pi
    l_cos = np.cos
    l_sin = np.sin

    theta = l_unifrom(0.0,2.0*l_pi,total_points)
    radius = ref_radius*l_sqrt(l_unifrom(0.0,1.0,total_points))
    x = radius*l_cos(theta)
    y = radius*l_sin(theta)

    # x and y thus obtained are Numpy arrays. Return these as lists
    return x.tolist(),y.tolist()

class GoldHunt:
    """Class to play a game scenario 'Great Gold Hunt' in 'Attack of The Orcs'.

    This class is created to illustrate a scenario discussed in the book:
    'Learning Python Application Development (Packt Publishing).

    This class illustrates various bottlenecks that impact
    the performance of the application. The bottlenecks will be visible if
    appropriately change the input arguments to __init__. For example,
    setting field_coins to a large number and/or making the search radius very
    small. A word of caution: if you do such changes, it will likely
    consume a lot of memory and you may notice performance lag on your computer.
    So do it at your own risk!

    :ivar int field_coins: Gold coins scattered over a circular field
    :ivar float field_radius: Radius of the circular field with gold coins
    :ivar float search radius: Radius of a circle. The gold search will be
            constrained within this circle.
    :ivar float x_ref: X-coordinate of the game unit searching for gold.
    :ivar float y_ref: Y-coordinate of the game unit searching for gold.
    :ivar float move_distance: Distance by which the game unit advances for the
           next search.
    """
    def __init__(self, field_coins=5000, field_radius=10.0, search_radius=1.0):
        self.field_coins = field_coins
        self.field_radius = field_radius
        self.search_radius = search_radius

        # Sir Foo's initial coordinates e.g. (-9.0, 0)
        self.x_ref = - (self.field_radius - self.search_radius)
        self.y_ref = 0.0
        # Distance by which Sir Foo (or any unit) advances for the
        # next search
        self.move_distance = 2*self.search_radius

    def reset_params(self):
        """Resets some dependent params to their default computed value."""
        self.x_ref = - (self.field_radius - self.search_radius)
        self.move_distance = 2*self.search_radius

    # Enable the @profile decorator only when you are running line_profiler
    # or memory_profiler. Otherwise it will throw an error.
    #@profile
    def find_coins(self, x_list, y_list):
        """Return list of coins that lie within a given distance.

        :param x_list: List of x coordinates of all the coins (points)
        :param y_list: List of y coordinates of all the coins (points)
        :return: A list containing (x,y) coordinates of all the eligible coins
        """
        collected_coins = []
        # Compute the square
        search_radius_square = self.search_radius*self.search_radius

        # Assign collected_coins.append to a local function
        append_coins_function = collected_coins.append
        # Create local variables to represent the instance vars
        local_xref = self.x_ref
        local_yref = self.y_ref

        # Find distance between current point and the center
        # of the search circle
        for x, y in zip(x_list, y_list):
            delta_x = local_xref - x
            delta_y = local_yref - y
            dist_square = delta_x*delta_x + delta_y*delta_y

            # Just compare the squares of the distances!
            if dist_square <= search_radius_square:
                # See the definition of append_coins_function
                # before the for loop. It is used in place of
                # collected_coins.append for speedup
                append_coins_function((x, y))

        return collected_coins

    def play(self):
        total_collected_coins = []
        x_list, y_list = generate_random_points(self.field_radius,
                                                self.field_coins)
        count = 0
        while self.x_ref <= 9.0:
            count += 1
            # Find all the coins that lie within the circle of radius 1 unit
            coins = self.find_coins(x_list, y_list)
            print("Circle# {num}, center:({x}, {y}), coins: {gold}".format(
                num=count, x=self.x_ref, y=self.y_ref, gold=len(coins)))

            # Update the main list that keeps record of all collected coins.
            total_collected_coins.extend(coins)

            # Move to the next position along positive X axis
            self.x_ref += self.move_distance

        print("Total_collected_coins =", len(total_collected_coins))


# Functions for profiling the code.
def view_stats(fil, text_restriction):
    """View the pstats for the given file

    :param fil: The file name for printing the stats.
    :param text_restriction: UNUSED variable to define filter on the output

    .. todo:: Cleanup the unused text_restriction variable or implement it!
    """
    stats = pstats.Stats(fil)
    # Remove the long directory paths
    stats.strip_dirs()
    # Sort the stats by the total time (internal time)
    sorted_stats = stats.sort_stats('tottime')
    # Only show stats that have "goldhunt" in their 'name column'
    sorted_stats.print_stats("goldhunt")


def play_game():
    """Control function to execute the GoldHunt game"""
    # IMPORTANT: The choice of input suggested below can consume a lot of
    # computational resources on your machine. See what your computer can
    # handle first by choosing a smaller size for field_coins and a LARGER
    # search_radius!
    game = GoldHunt(field_coins=2000000, search_radius=0.1)
    game.play()

if __name__ == '__main__':
    filname = 'profile_output_new'
    cProfile.run('play_game()', filname)
    # View the pstats
    view_stats(filname, "goldhunt")
