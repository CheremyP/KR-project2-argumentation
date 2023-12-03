import numpy as np
import json

with open("example-argumentation-framework.json", encoding="utf-8") as j_file:
    framework = json.load(j_file)
    
    
arguments = framework["Arguments"]
attacks = framework["Attack Relations"]
attacks = [[int(x), int(y)] for x,y in attacks]
# attacked_by = [[y,x] for x,y in attacks]


def main():
    
    opponent_wins, proponent_wins = False, False
    proponent_used_arguments = set()
    opponent_used_arguments = set()
    
    # 0. Initialize with a proponent argument, select from flattened list of arguments
    all_possible_arguments = [number for sublist in attacks for number in sublist]
    proponent_argument = np.random.choice(all_possible_arguments)
    proponent_argument = 4
    proponent_used_arguments.add(proponent_argument)
    
    print(f"Proponent plays {proponent_argument}")
    
    while proponent_wins==False:
        # 1. Set of arguments the opponent is allowed to use, based on the history of proponent arguments
        opponent_arguments = {x for x,y in attacks if y in proponent_used_arguments}
        # 1.1. Make copy, since opponent should be allowed to choose argument that is already used by proponent
        opponent_arguments_copy = opponent_arguments.copy()
        # 1.2. Player loses automatically if opponent_arguments is empty
        # 1.3. Player also loses if the only arguments left have already been played by proponent
        opponent_arguments = {x for x in opponent_arguments if x not in proponent_arguments}

        if not opponent_arguments:
            print("exit pleaase")
            proponent_wins = True

        opponent_argument = input(f"Select one of the following arguments:\n{opponent_arguments_copy}")
        opponent_used_arguments.add(opponent_argument)

        # 1.1. Proponent loses if they use an argument that was previously used by opponent
        opponent_arguments = {x for x in opponent_arguments if x not in proponent_arguments}
        # proponent_arguments = {x for x in opponent_arguments if x not in proponent_arguments}

        if opponent_argument in proponent_used_arguments:
            proponent_wins = True

        # 2. Proponent can use arguments that attack the opponent argument
        proponent_arguments = {x for x,y in attacks if y == opponent_argument}
        # 3. Proponent cannot use the same argument twice
        proponent_arguments = {x for x in proponent_arguments if x not in proponent_used_arguments}
        # 3.1 Proponent loses if they use an argument that was previously used by opponent
        # 3.2 Proponent loses if they have no more moves left
        ## Implicitly checks both cases
        ## Bc. if this set is empty, either 3.1 or 3.2 is True -> proponent loses
        proponent_arguments = {x for x in proponent_arguments if x not in opponent_used_arguments}
        if not proponent_arguments:
            opponent_wins = True

        proponent_argument = np.random.choice(list(proponent_arguments))
        proponent_used_arguments.add(proponent_argument)
    
    return opponent_wins, proponent_wins    

    
if __name__ == "__main__":

    opponent_wins, proponent_wins = main()
    
    if opponent_wins:
        print("Opponent wins!")
    if proponent_wins:
        print("Proponent wins!")


