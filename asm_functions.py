from random import randint, random
from asm_assets import dice, deck

def roll_asm_dice(num_dice, num_sides):
    results = []

    for _ in range(num_dice):

        dice_value = randint(0, num_sides - 1)

        result = f"D{num_sides}: {dice['d' + str(num_sides)][dice_value]}"

        results.append(result)

        # print(f"D{num_sides}: {dice['d' + str(num_sides)][dice_value]}")
        
    return "\n".join(results)