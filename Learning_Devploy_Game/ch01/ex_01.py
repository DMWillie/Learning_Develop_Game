"""
    作者:北辰
    日期:02/05/2019
    版本:0.0.1
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

if __name__ == '__main__':
    keep_playing = 'y'
    # 列表occupants表示木屋占有者的类型
    occupants = ['enemy','friend','unoccpuied']
    width = 72
    dotted_line = '-'*width
    print(dotted_line)
    # 序列\033[1m表示使用粗体文本,\033[0m表示返回到正常的打印样式
    print("\033[1m"+"Attack of the Orcs v0.0.1:"+"\033[0m")
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
    print(textwrap.fill(msg,width=width))
    print("\033[1m"+"Mission:"+"\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m"+"TIP:"+"\033[0m")
    print("Be careful as there are enemies lurking around!")
    print(dotted_line)

    # 最外层主循环,让玩家可以选择是否继续游戏
    while keep_playing == 'y':
        huts = []
        # Randomly append 'enemy' or 'friend' or None to the huts list
        while len(huts)<5:
            computer_choice = random.choice(occupants)
            huts.append(computer_choice)

        # Prompt user to select a hut
        msg = '\033[1m'+'Choose a hut number to enter (1-5): '+'\033[0m'
        user_choice  = input("\n"+msg)
        idx = int(user_choice)

        # Print the occupant info
        print('Revealing the occupants...')
        msg = ""
        for i in range(len(huts)):
            occupant_info = "<%d:%s>"%(i+1,huts[i])
            if i+1 == idx:
                occupant_info = "\033[1m"+occupant_info+"\033[0m"
            msg += occupant_info + " "
        print("\t"+msg)
        print(dotted_line)
        print("\033[1m"+"Enter hut %d... "% idx +"\033[0m",end=' ')

        # Determine and announce the winner
        if huts[idx-1] == 'enemy':
            print("\033[1m"+"YOU LOSE :( Better luck next time!"+
                  "\033[0m")
        else:
            print("\033[1m"+"Congratulations! YOU WIN!!!"+
                  "\033[0m")
        print(dotted_line)
        keep_playing = input("Play again? Yes(y)/No(n):")
