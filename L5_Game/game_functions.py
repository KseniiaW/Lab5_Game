# -*- coding: utf-8 -*-
from random import randint
import time

def get_player_names():
    """Get player names"""
    player1 = input('Enter name of player 1: ')
    player2 = input('Enter name of player 2: ')
    return player1, player2

def play_round(player_name):
    """Play one round"""
    print(f'{player_name} rolls the dice...', end=' ')
    time.sleep(1.5)
    number = randint(1, 6)
    dice_symbols = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    print(f'Result: {number} ({dice_symbols[number-1]})')
    return number

def determine_round_winner(n1, n2, name1, name2):
    """Determine round winner"""
    if n1 > n2:
        print(f'Round won by {name1}\n')
        return 1, 0
    elif n1 < n2:
        print(f'Round won by {name2}\n')
        return 0, 1
    else:
        print('Draw in this round!\n')
        return 0, 0

def determine_final_winner(sum1, sum2, wins1, wins2, name1, name2):
    """Determine game winner"""
    print('\n=== GAME RESULTS ===')
    print(f'Total points: {name1} - {sum1}, {name2} - {sum2}')
    print(f'Wins: {name1} - {wins1}, {name2} - {wins2}')

    if sum1 > sum2:
        return f'WINNER: {name1} by total points!'
    elif sum1 < sum2:
        return f'WINNER: {name2} by total points!'
    else:
        if wins1 > wins2:
            return f'WINNER: {name1} by number of wins!'
        elif wins1 < wins2:
            return f'WINNER: {name2} by number of wins!'
        else:
            return 'DRAW!'