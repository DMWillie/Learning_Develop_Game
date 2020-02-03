"""
    作者:北辰
    日期:31/05/2019
    功能:使用line_profiler包来逐行监视函数的性能
    在命令行使用: kernprof -v -l line_profiler_goldhunt.py来观察输出
"""

import math
import random
import matplotlib.pyplot as plt
import time

def plot_points(ref_radius, x_coords, y_coords):
    """Utility function to show the 'Gold Field!' """
    # Define axis limits
    a1 = ref_radius + 1
    a2 = a1*(-1.0)
    plt.plot(x_coords, y_coords, ".", color='#A67C00', ms=4)
    plt.axis([a2,a1,a2,a1])
    plt.show()

@profile
def generate_random_points(ref_radius,total_points):
    """Return x,y coords representing random points inside a circle"""
    x = []
    y = []
    show_plot = False

    for i in range(total_points):
        theta = random.uniform(0.0,2*math.pi)  # 点与原点之间的夹角
        r = ref_radius*math.sqrt(random.uniform(0.0,1.0)) # 点到原点的距离r
        x.append(r*math.cos(theta))
        y.append(r*math.sin(theta))

    if show_plot:
        plot_points(ref_radius,x,y)

    return x,y

class GoldHunt:
    """Class to play a scenario ‘Great Gold Hunt’"""
    def __init__(self,field_coins=5000,field_radius=10.0,search_radius=1.0):
        self.field_coins = field_coins
        self.field_radius = field_radius
        self.search_radius = search_radius

        # Game unit's inital coordinates e.g. (-9.0,0)
        self.x_ref = - (self.field_radius-self.search_radius)
        self.y_ref = 0.0

        # Distance by which the game unit advances
        # for the next gold search.
        self.move_distance = 2*self.search_radius

    #@profile
    def find_coins(self,x_list,y_list):
        """Return list of coins that lie within a given distance."""
        collected_coins = []
        for x,y in zip(x_list,y_list):
            # Find distance between the current point and the center
            # of the search circle.
            delta_x = self.x_ref - x
            delta_y = self.y_ref - y
            dist = math.sqrt(delta_x**2+delta_y**2)

            # Check if the point is inside the search circle
            if dist <= self.search_radius:
                collected_coins.append((x,y))


        return collected_coins

    def play(self):
        """Logic to play the scenario Great Gold Hunt"""
        total_collected_coins = []

        x_list,y_list = generate_random_points(self.field_radius,self.field_coins)

        count = 0
        # Loop to collect the gold coins in all the 'search circles'
        while self.x_ref <= self.field_radius - self.search_radius:
            count += 1
            # Find all the coins within a circle defined by 'search_radius'
            coins = self.find_coins(x_list,y_list)

            print("Circle# {num}, center:({x},{y}), coins: {gold}".format(
                num=count,x=self.x_ref,y=self.y_ref,gold=len(coins)
            ))

            # Update the list that keeps record of all the collected coins.
            total_collected_coins.extend(coins)

            # Move to the next position along positive X axis
            self.x_ref += self.move_distance

        print("Total collected coins: ",len(total_collected_coins))

if __name__ == '__main__':
    start = time.perf_counter()
    game = GoldHunt()

    # Optionally you can specify the problem size using input args
    # to GoldHunt.The line of code that does this is shown below (disabled)
    # IMPORTANT: The choice of input suggested below can consume a lot of
    # computational resources on your machine. See what your computer can
    # handle first by choosing a smaller size for field_coins and a LARGER
    # search_radius!

    #game = GoldHunt(field_coins=10000, search_radius=0.1)

    game.play()
    end = time.perf_counter()
    print("Total time interval:",end-start)