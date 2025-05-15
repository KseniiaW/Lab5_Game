# -*- coding: utf-8 -*-
from game_functions import get_player_names, play_round, determine_round_winner, determine_final_winner
import time
import sys

def main():
    try:
        # ввод имен игроков
        player1, player2 = get_player_names()
        
        sum1 = sum2 = 0
        wins1 = wins2 = 0
        
        print(f'\n{player1} vs {player2} - playing 5 rounds!\n')
        
        # цикл на 5 раундов
        for i in range(1, 6):
            print(f'=== Round {i} ===')
            
            #ход 1 игрока
            n1 = play_round(player1)
            sum1 += n1
            
            #ход 2 игрока
            n2 = play_round(player2)
            sum2 += n2
            
            # подсчет победителя
            round_wins1, round_wins2 = determine_round_winner(n1, n2, player1, player2)
            wins1 += round_wins1
            wins2 += round_wins2
            
            time.sleep(1)
        
        result = determine_final_winner(sum1, sum2, wins1, wins2, player1, player2)
        print(f'\n{result}\n\nGame over!')
        
        input("\nPress Enter to exit...")
    
    except Exception as e:
        print(f"Error occurred: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()