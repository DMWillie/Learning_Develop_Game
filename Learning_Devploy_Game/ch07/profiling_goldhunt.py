"""
    作者:北辰
    日期:30/05/2019
    功能:使用pstats.Stats模块对cProfile产生的输出进行分析
"""

import cProfile
import pstats
from goldhut_inefficient import GoldHunt

def view_stats(fil, text_restriction):
    """View the pstats for the given file"""

    stats = pstats.Stats(fil)
    # Remove the long directory paths
    stats.strip_dirs()
    # Sort the stats by the total time(internal time)
    sorted_stats = stats.sort_stats('tottime')
    # Only show stats that have "goldhunt" in their ‘name column’
    sorted_stats.print_stats("goldhunt")

def play_game():
    """Control function to execute the GoldHunt game"""
    game = GoldHunt()
    game.play()

if __name__ == '__main__':
    filename = 'profile_output_new'
    cProfile.run('play_game()',filename)
    # View the pstats
    view_stats(filename,"goldhunt")