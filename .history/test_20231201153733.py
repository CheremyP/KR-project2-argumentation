import numpy as np
import json

with open("example-argumentation-framework.json", encoding="utf-8") as j_file:
    framework = json.load(j_file)
    

opponent_wins, proponent_wins = False, False

test = False
proponent_argument = 4
print(f"Proponent plays {proponent_argument}")


while not proponent_wins and not opponent_wins:
    if not test:
        opponent_wins = True
        print("poep")
    print("kakka")
    
print('dia')