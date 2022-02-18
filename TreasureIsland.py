# Write Code 💻
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome To Treasure Island.")
print("Your Mission Is To Find The Treasure.")

direction = input('You\'re At The Bottom Of The Sea, Which Way Do You Wanna Go? Type "Up" Or "Down" ').lower()

if(direction == "up"):
    take_Or_Explore = input('You Arrive At A Dock Near A Deserted Town, Would You Like To The "Take" The Boat Or "Explore" The Town? ').lower()
    if(take_Or_Explore == "take"):
        hole = input('You\'ve Just Reached A Dungeon Far Far Away, As You Go Through It You Get Lost. You Have Three Holes In Front Of You, "First", "Second", "Third" ').lower()
        if(hole == "second"):
            print("You Entered The Hole Full Of Treasure, You Win.")
        else:
            print("You Get Lost In The Cave And Die Of Starvation. Game Over.")
    else:
        print("The Volcano In The Town Erupted And Burned You. Game Over.")
else:
    print("You Got Eaten By A Shark. Game Over.")
