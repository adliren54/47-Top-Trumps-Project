import os, time, random

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 10, "Guile": 10, "Baldness": 10}
trumps["Monica from Friends"] = {"Intelligence": 100, "Speed": 65, "Guile": 99, "Baldness": 0}
trumps["Professor X"] = {"Intelligence": 160, "Speed": 0, "Guile": 5, "Baldness": 10}


while True:
  print("🌟Top Trumps🌟")
  print()
  print("Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")
  print()
  for key in trumps:
    print(key)
  print()
  user = input("Pick your character\n> ")
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)
  print()

  print("Choose your stats: Intelligence, Speed, Guile, & Baldness Level")

  answer = input("> ")

  print()
  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")
  print()
  
  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")


  time.sleep(5)
  os.system("clear")

  proceed = input("Again? y/n > ").lower()
  if proceed == "y":
    continue
  elif proceed == "n":
    break