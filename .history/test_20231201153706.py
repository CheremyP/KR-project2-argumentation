import numpy as np
import json

with open("example-argumentation-framework.json", encoding="utf-8") as j_file:
    framework = json.load(j_file)
    
    
arguments = framework["Arguments"]
attacks = framework["Attack Relations"]
attacks = [[int(x), int(y)] for x,y in attacks]


opponent_wins, proponent_wins = False, False
proponent_used_arguments = set()
opponent_used_arguments = set()

test = False


# 0. Initialize with a proponent argument, select from flattened list of arguments
all_possible_arguments = [number for sublist in attacks for number in sublist]
proponent_argument = np.random.choice(all_possible_arguments)
proponent_argument = 4
proponent_used_arguments.add(proponent_argument)

print(f"Proponent plays {proponent_argument}")

    
while not proponent_wins and not opponent_wins:
    if not test:
        opponent_wins = True
        print("poep")
    print("kakka")
    
print('dia')