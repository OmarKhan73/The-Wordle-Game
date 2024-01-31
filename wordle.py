import random

word_list = ["chair", "Stare", "Start", "Carts", "Comma", "Spare", "Bored"]
answer = random.choice(word_list)
print("This is wordle")


def get_clue(ans, guess):
  clue = ""
  for idx, letter in enumerate(guess):
    if letter == ans[idx]:
      clue += "G"
    elif letter in ans:
      clue += "Y"
    else:
      clue += "-"
  return clue


for x in range(1, 7):
  guess = input("Word? ")
  print(get_clue(answer, guess), x)
  if answer == guess:
    break
