import random

def main():
    print('To use the roller, just input the number of sides that you want. No decimals. To roll more than one dice at the same time, just a space between the numbers. If you want to exit, just type "exit"')
    
    is_done = False
  
    while is_done == False:
        dice_type = input("How many sides do you want? ")
        if dice_type == "exit":
            is_done = True
        else:
            is_done = False
      
            dice_type = dice_type.split()
            dice_type = list(map(int, dice_type))
            
            for dice in dice_type:
                if dice_type <= 0:
                    print(f"A dice can't have {dice_type} sides")
                else:
                    print(f"Your roll is: {roll_dice(dice_type)}")
        
def roll_dice(dice_type):
    return random.randint(1, dice_type)
  
main()
