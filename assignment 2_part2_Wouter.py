def find_conflict_free_set(arguments, attacks):
    conflict_free_set = set()
    for arg1 in arguments:
        has_attack = False
        for arg2 in arguments:
            if (arg1, arg2) in attacks:
                has_attack = True
                break
        if not has_attack:
            conflict_free_set.add(arg1)
        else:
           conflict_free_set.add((arg1, arg2))
    return conflict_free_set

arguments = {'a', 'b', 'c', 'd', 'e'}
attacks = {('b', 'a'), ('b', 'c'), ('d', 'c'), ('c', 'd'), ('e', 'd'), ('e', 'e')}




result = find_conflict_free_set(arguments, attacks)
print("Conflict-free set:", result)


def is_defended(argument, relation, A):
    for element in A:
        defended = False
        for index in A:
            if (element, index) in relation and :
                # Check if there exists an argument in A that attacks 'argument'
                defended = any((arg, element) in relation for arg in A)
                if not defended:
                    print("Not defended")
                    return
        # If 'defended' is True at this point, it means 'argument' is defended by the set
    print("Defended")
    
    
    


# Example Framework
A = {'a', 'b', 'c', 'd', 'e'}
R = {('a', 'b'), ('c', 'b'), ('c', 'd'), ('d', 'c'), ('d', 'e'), ('e', 'e')}

def find_conflict_free_set(arguments, attacks):
    conflict_free_set = set()
    for arg1 in arguments:
        for arg2 in arguments:
            # if not (arg1, arg2) and not (arg2, arg1) in attacks:
            if not (arg1, arg2) in attacks:
                if not (arg2, arg1) in attacks:
                    conflict_free_set.add(tuple({arg1, arg2}))
    return conflict_free_set


def is_defended(argument, attacks):
    #Find attacks:
    # Checks if second item in tuple is argument (attacked), returns first item (attacker)
    attacked_by = set(x[0] for x in attacks if x[-1] == argument)
    # Set of all arguments that are attacked
    attacked_arguments = set(x[-1] for x in R)
    # Check if the attackers are a subset of the attacked arguments
    attacker_is_attacked = attacked_by.issubset(attacked_arguments)
    
    return attacker_is_attacked


def find_admissible_semantics(relations):
    # Get all arguments from relations (union of first and last element in each tuple of relations)
    arguments = {x[0] for x in relations}.union({x[-1] for x in relations})
    conflict_free_set = find_conflict_free_set(arguments, relations)
    # Get all arguments from conflict free set
    conflict_free_arguments = {x[0] for x in conflict_free_set}.union({x[-1] for x in conflict_free_set})
    # Set of arguments in the conflict free set that are undefended
    undefended_set = {x for x in conflict_free_arguments if not is_defended(x, relations)}
    # Checks if any argument in undefended set is in any of the tuples of the conflict-free set
    admissible_set = {x for x in conflict_free_set if not any(undefended_argument in x for undefended_argument in undefended_set)}

    return admissible_set

a = find_admissible_semantics(R)

set('c') in [set(x) for x in a]



a = {'b', 'e'}

b = ('a', 'b')


any(x in b for x in a)




['e' in x for x in relations]


arguments = {'a', 'b', 'c', 'd', 'e'}
attacks = {('a', 'b'), ('c', 'b'), ('c', 'd'), ('d', 'c'), ('d', 'e'), ('e', 'e')}

it = iter(arguments)
a = next(it)


aa = arguments.copy()



# Example Framework
A = {'a', 'b', 'c', 'd', 'e'}
R = {('a', 'b'), ('c', 'b'), ('c', 'd'), ('d', 'c'), ('d', 'e'), ('e', 'e')}

def find_conflict_free_set(arguments, attacks):
    conflict_free_list = []
    for arg1 in arguments:
        for arg2 in arguments:
            if (arg1, arg2) not in attacks:
                if not {arg1,arg2} in conflict_free_list:
                    conflict_free_list.append({arg1,arg2})
    return conflict_free_list

find_conflict_free_set(A, R)


# Check if 'c' is defended by any set
is_defended('b', R, A)




def is_defended(argument, relation, arguments):
    for element in arguments:
        defended = any((arg, element) in relation for arg in arguments)
        if not defended:
            return False
    return True

def find_admissible_semantics(arguments, attacks):
    conflict_free_set = find_conflict_free_set(arguments, attacks)
    admissible_set = set()
    for argument in conflict_free_set:
        if is_defended(argument, attacks, arguments):
            admissible_set.add(argument)
    return admissible_set

def main():
    # Given arguments and attacks
    arguments = {'a', 'b', 'c', 'd', 'e'}
    attacks = {('a', 'b'), ('c', 'b'), ('c', 'd'), ('d', 'c'), ('d', 'e'), ('e', 'e')}

    # Find admissible semantics
    admissible_set = find_admissible_semantics(arguments, attacks)

    # Ask the user for an argument to check
    try:
        argument_to_check = input("Enter the argument to check for credulous acceptance: ")
    except ValueError:
        print("Invalid input. Please enter a valid argument.")
        return

    # Check if the argument is in the admissible semantics set
    if argument_to_check in admissible_set:
        print(f"The argument {argument_to_check} is credulously accepted under admissible semantics.")
    else:
        print(f"The argument {argument_to_check} is not credulously accepted under admissible semantics.")

if __name__ == "__main__":
    main()
