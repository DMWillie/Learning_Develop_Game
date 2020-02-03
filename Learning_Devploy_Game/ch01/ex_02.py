"""
    作者:北辰
    日期:06/05/2019
    版本:0.0.5
    功能:兽人之袭文本游戏
    0.0.5版本新增功能:具有攻击功能
    具体功能描述如下:
    当用户希望一直玩这个游戏时：
    1.打印游戏的任务
    2.创建一个木屋的列表
    3.在5个木屋中随机分配敌人,同伴或空闲类型
    4.提示用户选择一个木屋的编号
    5.如果木屋中有敌人,那么进行以下处理:
      5.1 当用户想要继续进攻时,对敌人使用attack()方法
      5.2 在每一次攻击之后,更新和显示Foo先生和敌人的健康状况
      5.3 如果敌人的health<=0,打印"你赢了"
      5.4 相反,如果Foo先生的health<=0,打印"你输了"
    6.否则(木屋被同伴占有或者空闲),打印"你赢了"
"""

import random

def print_bold(msg,end='\n'):
    """Print a string in 'bold' font"""
    print("\033[1m"+msg+"\033[0m",end=end)  # 以粗体方式打印

def print_dotted_line(width=72):
    """Print a dotted (rather 'dashed') line"""
    print('-'*width)

def show_game_mission():
    """Print the game mission in the terminal window"""
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()

def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30

def occupy_huts():
    """Randomly populate the `huts` list with occupants"""
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts

def process_user_choice():
    """Accepts the hut number from the user"""
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx

def reveal_occupants(idx,huts):
    """Print the occupants of the hut"""
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "

    print("\t" + msg)
    print_dotted_line()

def show_health(health_meter,bold=False):
    """Show the remaining hit points of the player and enemy"""
    msg = "Health: Sir Foo: %d,Enemy: %d" \
            % (health_meter['player'],health_meter['enemy'])

    if bold:
        print_bold(msg)
    else:
        print(msg)

def attack(health_meter):
    """The main logic to determine injured unit and amount of injury"""
    # 假设敌人有60%的概率受到伤害,而玩家有40%的概率受到伤害
    hit_list = 4*['player'] + 6*['enemy']
    injured_unit = random.choice(hit_list)
    # 取得随机选择的受伤方当前的生命力
    hit_points = health_meter[injured_unit]
    injury = random.randint(10,15)
    # 更新受伤方的健康表信息
    health_meter[injured_unit] = max(hit_points-injury,0)
    print("ATTACK! ",end='')
    show_health(health_meter)

def play_game(health_meter):
    """"""
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx,huts)
    # 遇到敌人
    if huts[idx-1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold("ENEMY SIGHTED! ",end='')
        show_health(health_meter,bold=True)
        continue_attack = True

        while continue_attack:
            continue_attack = input("......continue attack?(y/n): ")
            if continue_attack == 'n':
                print_bold("RUNNING AWAY with following health status...")
                show_health(health_meter,bold=True)
                print_bold("GAME OVER!")
                break

            attack(health_meter)  # 该函数的功能是参与战斗并更新健康表信息
            # 检查是否分出胜负
            if health_meter['enemy']  <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break

            if health_meter['player'] <= 0:
                print_bold("YOU LOSE :( Better luck next time")
                break

def run_application():
    """
    主函数
    Top level control function for running the application.
    """
    keep_playing = 'y'
    health_meter = {}      # 创建一个空的字典来存储生命值
    reset_health_meter(health_meter)  # 为Foo先生和潜在的敌人写入初始的生命值
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")

if __name__ == '__main__':
    run_application()