import random

def main():
    is_done = False
  
    while is_done == False:
        dice_type = input("How many sides do you want? ")
        if dice_type == "exit":
            is_done = True
        else:
            is_done = False
      
        dice_type = int(dice_type)
      
        if dice_type <= 0:
            is_done = False
            print(f"A dice can't have {dice_type} sides")
        else:
            print(f"Your roll is: {roll_dice(dice_type)}")
        
def roll_dice(dice_type):
    return random.randint(1, dice_type)
  
main()
