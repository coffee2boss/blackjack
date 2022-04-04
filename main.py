import random
from art import logo 
print(logo)



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



dealer_first_card = random.sample(cards,1)
dealer_second_card = random.sample(cards,1)
dealer_sum = int(sum(dealer_first_card + dealer_second_card))
print(f"dealer has {dealer_first_card}")

user_first_card = random.sample(cards,1)
user_second_card = random.sample(cards,1)
user_sum = int(sum(user_first_card + user_second_card))
print(f"You have {user_first_card} and {user_second_card}")
print(f"Your total is {user_sum}")


def game_over():
  print(f"dealer has {dealer_second_card}")
  print(f"dealers total is {dealer_sum}")
  if user_sum > 21:
    print("You lose")
  elif dealer_sum == user_sum:
    print("Draw ")
  elif user_sum > dealer_sum and user_sum < 21:
    print("You win")
  else:
    print("Dealer wins")

inplay = True

if user_sum == 21:
    print("Blackjack you win")
else:
  inplay = True

while inplay:
  next_card = input("Hit or Stay? ")
  if next_card == "hit":
   new_card = random.sample(cards,1)
   new_user_total = sum(user_sum + new_card)
   print(new_user_total)
   if new_user_total > 21:
    inplay = False
    print("Too greedy, you lost")
  else:
   inplay = False
   game_over()


