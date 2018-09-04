#!/usr/bin/env python3
#====coding:utf-8======
import random
def game():
    input('欢迎来到石头剪刀布的游戏')
    list1 = ['石头', '剪刀', '布']
    win = [['石头', '剪刀'], ['石头', '布'], ['剪刀', '布']]
    computer = random.chice(list1)
    u = input('你可以出了')
    if computer == u:
        print('平手了')
    elif [u, computer] in win:
        print('您赢了')
    else:
        print('sorry 您输了')
game()
