"""
    作者:北辰
    日期:02/05/2019
    版本:0.0.2
    新增功能:重构0.0.1版本,将其模块化
    功能:兽人之袭文本游戏,具体功能描述如下:
    当用户希望一直玩这个游戏时：
    1.打印游戏的任务
    2.创建一个木屋的列表
    3.在5个木屋中随机分配敌人,同伴或空闲类型
    4.提示用户选择一个木屋的编号
    5.如果选中敌人占据的木屋,打印"你输了"
    6.否则,打印你赢了
"""

import random
import textwrap

width = 72

def print_dotted_line():
    """打印分割线"""
    dotted_line = '-' * width
    print(dotted_line)

def show_theme_message():
    """打印游戏的主题信息"""
    print_dotted_line()
    # 序列\033[1m表示使用粗体文本,\033[0m表示返回到正常的打印样式
    print("\033[1m" + "Attack of the Orcs v0.0.1:" + "\033[0m")
    # 在控制台中打印游戏的进一步信息
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")
    # textwrap.fill会让每行以72个字符长度的方式对消息进行显示
    print(textwrap.fill(msg, width=width))

def show_game_mission():
    """打印游戏任务"""
    print("\033[1m" + "Mission:" + "\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m" + "TIP:" + "\033[0m")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()


def occupy_huts(occupants):
    """
    occupants: 木屋占据者的类型
    随机选择木屋占据者
    """
    huts = []
    # Randomly append 'enemy' or 'friend' or None to the huts list
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts

def process_user_choice():
    """
    处理用户的选择的木屋编号
    """
    msg = '\033[1m' + 'Choose a hut number to enter (1-5): ' + '\033[0m'
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx

def reveal_occupants(idx,huts):
    """
    idx: 玩家选择的进入的木屋编号
    huts: 木屋占有者列表
    Print the occupants of the hut
    """
    msg = ""
    print('Revealing the occupants...')
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i + 1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

def enter_hut(idx,huts):
    """
    idx: 玩家选择进入的木屋编号
    huts: 木屋
    """
    print("\033[1m" + "Enter hut %d... " % idx + "\033[0m", end=' ')

    # Determine and announce the winner
    if huts[idx - 1] == 'enemy':
        print("\033[1m" + "YOU LOSE :( Better luck next time!" +
              "\033[0m")
    else:
        print("\033[1m" + "Congratulations! YOU WIN!!!" +
              "\033[0m")
    print_dotted_line()

def run_application():
    """主进程:处理游戏逻辑"""
    keep_playing = 'y'
    # 列表occupants表示木屋占有者的类型
    occupants = ['enemy', 'friend', 'unoccpuied']

    show_theme_message()
    show_game_mission()

    while keep_playing == 'y':
        huts = occupy_huts(occupants)
        idx = process_user_choice()
        reveal_occupants(idx,huts)
        enter_hut(idx,huts)
        keep_playing = input("Play again? Yes(y)/No(n): ")

if __name__ == '__main__':
    run_application()

