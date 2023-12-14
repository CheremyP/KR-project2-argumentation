import numpy as np
import json
import sys
import os

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
    try:
        attacks = framework["Attack Relations"]
    except Exception as e:
        print(f"Encountered exception: {e}. Ensure the attack relations in the .json file are called \"Attack Relations\"")
        sys.exit()
        
    attacks = [[int(x), int(y)] for x,y in attacks] 


    opponent_wins, proponent_wins = False, False
    proponent_used_arguments = set()
    opponent_used_arguments = set()

    # 0. Initialize with a proponent argument, select from flattened list of arguments
    all_possible_arguments = [number for sublist in attacks for number in sublist]
    proponent_argument = np.random.choice(all_possible_arguments)
    # proponent_argument = 0
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

        opponent_argument = get_user_input(opponent_arguments_copy, opponent_used_arguments) #quits if opponent reuses argument
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
        valid_framework = False
        valid_argument = False
        framework_path = sys.argv[1] 
        argument = sys.argv[2]
        
        while valid_framework == False:
            print(f"Loading framework {framework_path}")
            if not os.path.exists(framework_path):
                framework_path = input(f"{framework_path} does not exist. Please enter a valid \"framework\".json: ") 
            else:
                with open(framework_path, encoding="utf-8") as j_file:
                    framework = json.load(j_file)
                valid_framework = True     
                
        # while not isinstance(argument, int):
        #     print(f"The claimed argument should be an integer. {argument} is not an integer")
        #     argument = input("Please input a valid integer:")
        

    else:
        print("\nLoading default framework example_framework.json\n")
        with open("example_framework.json", encoding="utf-8") as j_file:
            framework = json.load(j_file)
            
    
    arguments = framework["Arguments"]
    print("Arguments")
    for number, arg in arguments.items():
        print(f"{number}: {arg}")
    print("\n")   
    
    all_possible_arguments = [int(x) for x in arguments.keys()]        
    print(all_possible_arguments)
    if len(sys.argv) == 3:

        while True:
            argument = input("Enter an integer argument from the set {}:".format(all_possible_arguments))

            try:
                argument = int(argument)

                if argument in all_possible_arguments:
                    break
                else:
                    print("Argument is not in the set of possible arguments. Try again.")
            except ValueError:
                print("Input is not an integer. Please enter a valid integer.")

        
        
        
        
        
        # while argument not in all_possible_arguments and not isinstance(argument, int):
        #     argument = input("Argument needs to be an integer in the set of possible arguments. Please choose a valid argument:")
        #     try:
        #         argument = int(argument)
        #     except ValueError:
        #         print("Argument needs to be an integer!")
                 
                
            # argument = input("Argument needs to be an integer in the set of possible arguments. Please choose a valid argument:")
    

    main(framework)
    

        

        
        

        



