import json
import sys, os


with open("example_AF.json", encoding="utf-8") as j_file:
    framework = json.load(j_file)

framework




def find_conflict_free_set(arguments, attacks):
    conflict_free_set = set()
    new_args = set()
    for arg1 in arguments:
        if (arg1,arg1) not in attacks:
            new_args.add(arg1)
    for arg1 in new_args:
        for arg2 in new_args:
            # check (x,y) and (y,x) in attacks
            if not (arg1, arg2) in attacks:
                if not (arg2, arg1) in attacks:
                    #first converting to set ensures:
                    # (x,x) -> (x)
                    # (x,y), (y,x) is added only once
                    conflict_free_set.add(tuple({arg1, arg2}))
    
    
    return conflict_free_set

# find_conflict_free_set(A, R)

def is_defended(argument, attacks):
    #Find attacks:
    # Checks if second item in tuple is argument (attacked), returns first item (attacker)
    attacked_by = set(x[0] for x in attacks if x[-1] == argument)
    # Set of all arguments that are attacked
    attacked_arguments = set(x[-1] for x in R)
    # Check if the attackers are a subset of the attacked arguments
    attacker_is_attacked = attacked_by.issubset(attacked_arguments)

    return attacker_is_attacked


def find_admissible_semantics(attacks):
    # Get all arguments from relations (union of first and last element in each tuple of relations)
    arguments = {x[0] for x in attacks}.union({x[-1] for x in attacks})
    conflict_free_set = find_conflict_free_set(arguments, attacks)
    # Get all arguments from conflict free set
    conflict_free_arguments = {x[0] for x in conflict_free_set}.union({x[-1] for x in conflict_free_set})
    # Set of arguments in the conflict free set that are undefended
    undefended_set = {x for x in conflict_free_arguments if not is_defended(x, attacks)}
    # Checks if any argument in undefended set is in any of the tuples of the conflict-free set
    admissible_set = {x for x in conflict_free_set if not any(undefended_argument in x for undefended_argument in undefended_set)}

    return admissible_set


def main(attacks):
    # Given arguments and attacks

    # Find admissible semantics
    admissible_set = find_admissible_semantics(attacks)

    print(admissible_set)

    # Ask the user for an argument to check
    try:
        argument_to_check = input("Enter the argument to check for credulous acceptance: ")
    except ValueError:
        print("Invalid input. Please enter a valid argument.")
        return

    is_in_admissible_set = set(argument_to_check) in [set(x) for x in admissible_set]

    if is_in_admissible_set:
        print(f"The argument {argument_to_check} is credulously accepted under admissible semantics.")
    else:
        print(f"The argument {argument_to_check} is not credulously accepted under admissible semantics.")



if __name__ == "__main__":
    # Extract command-line arguments
    if len(sys.argv) == 2:
        valid_framework = False
        framework_path = sys.argv[1] 
        
        while valid_framework == False:
            print(f"Loading framework {framework_path}")
            if not os.path.exists(framework_path):
                framework_path = input(f"{framework_path} does not exist. Please enter a valid \"framework\".json: ")
            else:
                with open(framework_path, encoding="utf-8") as j_file:
                    framework = json.load(j_file)
                valid_framework = True

    else:
        print("\nLoading default framework example_AF.json")
        with open("example_AF.json", encoding="utf-8") as j_file:
            framework = json.load(j_file)
    print("\n")
    A = framework['A']
    R = set((x,y) for x,y in framework['R'])

    main(R)
