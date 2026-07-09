# A match statement is used to perform different actions based on different conditions.
# The match expression is evaluated once. Then the value of the expression is compared
# to the value of each case. When one matches, that code block is executed.

Character = "Dante"
match Character:
    case "Nero":
        print("Nero is a main protagonist of DMC")
    case "Vergil":
        print("Vergil is the main protag of DMC")
    case "Dante":
        print("Dante is the main protag of DMC")
        # use the _ whne you wnat the code block to execute if there is not match
Character = "Goku"
match Character:
    case "Gohan":
        print("Gohan is the strongest")
    case "Vegeta":
        print("Vegeta is very strong")
    case _:
        print("Unknown character")
# for combineing vlaues use | or the or operators
Spell = 5
match Spell:
    case 1 | 2 | 3 | 4 | 5:
        print("The 5 keybind is tied a fireball")
    case 6 | 7:
        print("6 or 7 are an iceball or wind spell")
# you can use if statments as extra conditions 
MP = 5
Spell = 3
match Spell:
    case 1 | 2 | 3 | 4 if MP == 3:
        print("At 5 MP points you can cast spell 3 a fireball")
    case 1 | 2 | 3 | 4 if MP == 5:
        print("Spell 3 can only be cast with 5 Mana points")
        