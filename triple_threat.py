"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Channing - November 2024
"""

import random

def main() -> None:
    # set original variables
    cost_to_play: int = 3
    base_prize = 10
    base_payout: int = 0
    mega_number: int = 6
    mega_multiplier: int = 10

    min_plays: int = 1000
    max_plays: int = 5000
    # Get random number of plays
    num_plays: int = random.randint(min_plays, max_plays) 

    # Set up total variables.
    total_collected: int = 0
    total_payout: int = 0
    total_profit: int = 0
    for i in range(num_plays):
        # roll three dice
        dice_1: int = random.randint(1, 6)
        dice_2: int = random.randint(1, 6)
        dice_3: int = random.randint(1, 6)

        # check if they are equal  
        payout: int = 0
        if dice_1 == dice_2 and dice_2 == dice_3:
            # if they are, calculate the prize 
            if dice_1 == mega_number:
                payout += base_prize * mega_multiplier
            else:
                payout += base_prize * dice_1

        profit: int = cost_to_play - payout

        # Add to total variables
        total_collected += cost_to_play
        total_payout += payout
        total_profit += profit

    # output results
    print("Games played, Total collected, Total paid out, Profit")
    print(f"{num_plays},{total_collected},{total_payout},{total_profit}")
if __name__ == "__main__":

    main()