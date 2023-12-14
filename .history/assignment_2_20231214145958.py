import numpy as np
import json
import sys


def get_user_input(possible_arguments, oponent_used_arguments):
    print("Possible arguments: ", possible_arguments)
    argument = input("Choose an argument: ")
    while True:
        if argument.isdigit() and int(argument) in possible_arguments:
            if int(argument) in oponent_used_arguments:
                print("Proponent wins!")
                exit()
            return int(argument)
        argument = input("Invalid argument. Choose again: ")
    
    
def main(framework):
    arguments = framework["Arguments"]
    attacks = framework["Attack Relations"]
    attacks = [[int(x), int(y)] for x,y in attacks] 

    opponent_wins, proponent_wins = False, False
    proponent_used_arguments = set()
    opponent_used_arguments = set()

    # 0. Initialize with a proponent argument, select from flattened list of arguments
    all_possible_arguments = [number for sublist in attacks for number in sublist]
    proponent_argument = np.random.choice(all_possible_arguments)
    proponent_argument = 0
    proponent_used_arguments.add(proponent_argument)

    print(f"Proponent plays {proponent_argument}, with argument '{arguments[str(proponent_argument)]}'")
    count = 0
    while not proponent_wins and not opponent_wins:
        # 1. Opponent is allowed to use any argument that attacks arguments used by proponent
        opponent_arguments = {x for x,y in attacks if y in proponent_used_arguments}
        # 1.1. Make copy, since opponent should be allowed to choose argument that is already used by proponent
        opponent_arguments_copy = opponent_arguments.copy()
        # 1.2. The set opponent_arguments is empty if:
        # 1.2.1 Opponent has no more valid moves(set will already be empty)
        # 1.2.2 The only valid arguments have been previously played by the proponent (set is empty after next line)
        opponent_arguments = {x for x in opponent_arguments if x not in proponent_used_arguments}

        if not opponent_arguments:
            proponent_wins = True
            break

        opponent_argument = get_user_input(opponent_arguments_copy, opponent_used_arguments)
        
        opponent_used_arguments.add(opponent_argument)

        # 1.3. Opponent loses if they use an argument that was previously used by proponent (again, this time by choice)
        if opponent_argument in proponent_used_arguments:
            proponent_wins = True
            break

        # 2. Proponent can use arguments that attack the opponent_argument in previous round
        proponent_arguments = {x for x,y in attacks if y == opponent_argument}
        # 3.1 Proponent cannot use the same argument twice
        proponent_arguments = {x for x in proponent_arguments if x not in proponent_used_arguments}
        # 3.2. The set proponent_arguments is empty if:
        # 3.2.1. Proponent has no more valid moves
        # 3.2.2. The only valid arguments have been previously played by the proponent
        proponent_arguments = {x for x in proponent_arguments if x not in opponent_used_arguments}
        if not proponent_arguments:
            opponent_wins = True
            break

        # If set is not empty, plays random move from set of possible arguments
        proponent_argument = np.random.choice(list(proponent_arguments))
        print(f"Proponent plays {proponent_argument} with argument '{arguments[str(proponent_argument)]}'")
        proponent_used_arguments.add(proponent_argument)
        count += 1
        
        
    if opponent_wins:
        print(f"Opponent plays {opponent_argument} with argument '{arguments[str(opponent_argument)]}'")
        print("Opponent wins!")
    if proponent_wins and count == 0:
        print("Proponent wins!")
    elif proponent_wins and count > 0:
        print(f"Proponent plays {proponent_argument} with argument '{arguments[str(proponent_argument)]}'")
        print("Proponent wins!")
        
        
if __name__ == "__main__":
    # Extract command-line arguments
    if len(sys.argv) == 3:
        print("Using custom parameters")
        ontology_file = sys.argv[1]
        class_name = sys.argv[2]
    elif len(sys.argv) != 1:
        print("Length of arguments should be 2 or 0. ")
    
    with open("example-argumentation-framework.json", encoding="utf-8") as j_file:
        framework = json.load(j_file)
    

        

        
        

        



