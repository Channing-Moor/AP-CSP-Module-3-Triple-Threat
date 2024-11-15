"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Channing - November 2024
"""

import random

def main() -> None:
    # set variables for cost to play and base prize
    cost_to_play: int = 1
    base_prize = 10
    base_payout: int = 0
    mega_number: int = 6
    mega_multiplier: int = 10


    # roll three dice
    dice_1: int = random.randint(1, 6)
    dice_2: int = random.randint(1, 6)
    dice_3: int = random.randint(1, 6)

    # check if they are equal
    # if they are, calculate the prize   
    payout: int = 0
    if dice_1 == dice_2 and dice_2 == dice_3:
        if dice_1 == mega_number:
            payout: int = base_prize * mega_multiplier
        else:
            payout: int = base_prize * dice_1

    # output results
    print("Casino collects: $" + str(cost_to_play))
    print(f"Player rolls: {dice_1}-{dice_2}-{dice_3}")
    print("Casino pays out: $" + str(payout))
    print("Profit: $" + str(cost_to_play - payout))

if __name__ == "__main__":
    main()