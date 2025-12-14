# -*- coding: utf-8 -*-

import os
import random
import time

#const for schedule for sleep console:
SCHEDULE = 1

#ANSII colors:
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

#sleep console:
def sleep():
    time.sleep(SCHEDULE)
def print_exception_message(txt):
    print(txt)
    sleep()
#return random color:
def set_color():
    colors = [RED,GREEN,BLUE,YELLOW,GREEN,CYAN]
    index = random.randint(0,5)
    return colors[index]
#check for exception
def have_bug_for_bet(bet,m):
    try:
        int(bet)
    except ValueError:
        return True
    except TypeError:
        return True
    if int(bet) < m:
        return True
    return False

#generate random numbers: for a b c
def generate(rotate):
    for i in range(3):
         rotate.append(random.randint(1, 20))
    print(set_color()+str(rotate[0])+RESET+' '+
          set_color()+str(rotate[1])+RESET+' '+
          set_color()+str(rotate[2])+RESET)
#compare a b c:
def compare(rotate,bet,balance):
    if rotate[0] == rotate[1] 
    and rotate[1] == rotate[2]:
        print(BLUE+"JACKPOT"+RESET)
        print(BLUE+"win: "+RESET, bet * 10)
        balance[0] += bet * 10
        sleep()

    elif rotate[0] == rotate[1] 
    or rotate[1] == rotate[2] 
    or rotate[0] == rotate[2]:
        print(BLUE+"WIN"+RESET)
        print(BLUE+"win: "+RESET, bet * 2)
        balance[0] += bet * 2
        sleep()
        
    else:
        print(BLUE+"Try Again."+RESET)
        balance[0] -= bet
        sleep()
#play casino simulate:
def play_casino():
    balance = []
    balance.append(100)
    rotate = []
    while True:
        os.system("cls")
        #simulate console clearing:
        print('\n' * 100)
        
        print(YELLOW+"Balance:"+RESET,balance)
        n = input(YELLOW+"Enter bet: "+RESET)
        if have_bug_for_bet(n,1):
            print_exception_message(RED+"Invalid bet"+RESET)
            continue
        bet = int(n)
        if bet > balance[0]:
            print(RED+"Not enough balance."+RESET)
            break
        #generating random combination:
        generate(rotate)
        compare(rotate,bet,balance)
        #clear a b c
        rotate.clear()
#run:
play_casino()