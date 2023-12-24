
"""
  Description: Ship, Captain, and Crew: the two-player dice game. If a player does not roll a 6, 5 and 4 with their three rolls, then they score zero points. If, they manage to roll a 6, 5, and a 4, then the remaining two dice (the cargo) are added together to determine the player's score. The player with the highest score is the winner.
"""

import random
import check_input


"""
  Roll_dice randomizes each of the 5 dice with values 1-6. 
  Then sorts in descending order.
"""
def roll_dice(dice):
  for i in range(len(dice)):
    dice[i] = random.randint(1, 6)
    dice.sort(reverse=True)
  return dice


"""Display_dice displays the title and set of dice values."""
def display_dice(name, dice):
  print(name, end='')
  for number in dice:
    print(number, end=' ')
  print("")


"""
  Compares each of the player’s points
  Displays each of the player’s points and the winner (or tie).
"""
def find_winner(player_points):
  print(f"\nScore:\nPlayer #1 = {player_points[0]}")
  print(f"Player #2 = {player_points[1]}")
  if (player_points[0] > player_points[1]):
    print("Player #1 won!")
  elif (player_points[0] < player_points[1]):
    print("Player #2 won!")
  else:
    print("Tie!")


def main():
  print("- Ship, Captain, and Crew! -")
  score = []
  #Define users turn, limit in 2 turns
  for turn in range(1, 3):
    diceToKeep = []
    diceToRoll = []
    dice_size = 5
    dice = [0] * dice_size
    cargo = 0
    i = 0
    again = True

    print(f"\nPlayer #{turn}'s Turn:")
    #Define user round, limit in 3 rounds. User can continue or stop their round.
    while i < 3 and again == True:
      diceToRoll = roll_dice(dice)
      display_dice("Roll = ", diceToRoll)
      #Apply the rule to find dice to keep and dice to roll
      if (dice_size == 5 and 6 in diceToRoll):
        diceToKeep.append(6)
        dice_size -= 1
        diceToRoll.remove(6)
        print("Ho ho ho! Ye secured a ship!")
      if (dice_size == 4 and 5 in diceToRoll):
        diceToKeep.append(5)
        dice_size -= 1
        diceToRoll.remove(5)
        print("Shiver me timbers! A Capt’n!")
      if (dice_size == 3 and 4 in diceToRoll):
        diceToKeep.append(4)
        dice_size -= 1
        diceToRoll.remove(4)
        print("Ye bribed a crew with Grog!")
      if (dice_size == 2):
        cargo = diceToRoll[0] + diceToRoll[1]
      display_dice("Keep = ", diceToKeep)

      # Display player's cargo
      if (cargo > 0):
        print(f"Cargo = {diceToRoll[0]} {diceToRoll[1]}")
        print(f"Your cargo points are: {cargo}")

      if (i < 2):
        again = check_input.get_yes_no("\nRoll again? ")
      if (again == False or i == 2):
        score.append(cargo)
      i += 1
    # Display player's final point
    print(f"Player #{turn} points = {cargo}")

  find_winner(score)


main()
