action = ''
if action == 'help':
  print("You can type 'help', 'left', 'right', 'up', 'down', 'grab', or 'fight'")
  pass
elif action == 'left':
  # move left
  pass
elif action == 'right':
  # move right
   pass
elif action == 'up':
  # move up
  pass
elif action == 'down':
  # move down
  pass
elif action == 'grab':
  # grab items
  pass
elif action == 'fight':
  # fight the monster
  pass
elif action == 'exit':
    done = True
Floor_1 = ['Bottle of Juice','Dog', 'RPG', 'M16']
Floor_2 = ['']
Floor_3 = ['']
Inventory = ['Rocks', 'Dog', 'Sword', 'Juice']
Section = 0
I = 0
Goodies = 0
Floor = 0
print("Welcome to my Dungeon Game, Enjoy....")
def InventoryChecker():
  global I
  print("You are currently holding:")
  while I < len(Inventory):
    if Inventory[I] == '':
      Inventory[I] = 'Nothing'
      print(Inventory[I])
    else:
      print(Inventory[I])
    I = I+1
InventoryChecker()
def Floor_Set():
  global Floor
  if Floor == 0 and Section == 0:
    print("You see a room on the left and right")
    action = input("What action will you take?")
    if action == 'left':
      Goodies = 0
    action = input("You see a "+ Floor_1[Goodies]+" on the ground, what is your action?")
Floor_Set()
  