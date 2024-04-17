import itertools
from itertools import product, combinations
import minor_trees as minors
import math
import json
    
def generate_combinations(class_list, subrequirements):
    #print("Generating combinations...")
    # Generate all possible combinations of classes
    all_combinations = {}
    for category, classes in class_list.items():
        
        # Determine the number of classes required for this category
        num_required_classes = min(len(classes), subrequirements[category])

        # Generate combinations of required length for this category
        category_combinations = [()]
        if num_required_classes > 0:
            category_combinations.extend((combinations(classes, 
                                                  num_required_classes)))

        #print(f"Category combinations: {category_combinations}")
        all_combinations[category] = category_combinations

    '''print("All combinations:")
    for category, combo in all_combinations.items():
        print(f"{category}: {combo}")'''
    
    all_combinations_product = list(product(*list(all_combinations.values())))

    # Transform combinations into list of dictionaries
    combined_combinations = []
    for combo in all_combinations_product:
        category_map = {}
        for idx, (category, combos) in enumerate(all_combinations.items()):
            category_map[category] = combo[idx]
        combined_combinations.append(category_map)
    
    combined_combinations = combined_combinations[1:]
    all_combinations_product = all_combinations_product[1:]

    return all_combinations_product, combined_combinations

def best_path(node):
    '''print(f"Node: {node.get_name()}")
    print(f"Marked: {node.get_marked()}")
    for child in node.get_children():
        print(f"Child: {child.get_name()}")'''
    if node.get_children() == []:
        return node
    
    if node.get_node_type() == 'OR':
        #print(f"Winner: {node.get_winner().get_name()}")
        node.children = [node.get_winner()]
        '''print(f"Winner: {node.get_winner().get_name()}")
        for child in node.get_children():
            print(f"Child: {child.get_name()}")'''

    marked_children = []
    for child in node.get_children():
        if child.get_marked():
            marked_children.append(child)
            best_path(child)
    node.children = marked_children
    return node

def extract_node_information(node, parent_name=None):
    # Initialize dictionary to store node information
    node_info = {}

    # Extract node information
    node_name = node.get_name()
    class_list = node.get_class_list()
    
    # Store node name and associated class list
    node_info['name'] = node_name
    node_info['class_list'] = class_list
    
    # Store parent's name if available
    if parent_name is not None:
        node_info['parent'] = parent_name
    
    # Recursively process children nodes
    if node.get_children():
        node_info['children'] = []
        for child in node.get_children():
            child_info = extract_node_information(child, node_name)
            node_info['children'].append(child_info)
    
    return node_info

def traverse_tree(node, combination_dict, 
                  subrequirements, used):
    if node.get_parent():
        #if node.get_parent().get_node_type() == 'AND':
        node.class_list = node.get_parent().class_list.copy()
    # Base case: child node with no children
    if node.get_children() == []:
        # Get classes taken for this requirement

        # First section checks to make sure if the parent is an AND node, 
        # the classes are not repeated
        combination = combination_dict.get(node.get_name(), [])
        courses = list(combination).copy()
        taken = len(combination)
        for course in combination:
            if course in used:
                taken -= 1
                courses.remove(course)
            else:
                if node.get_parent().get_node_type() == 'AND':
                    used.add(course)
        node.classes_taken = taken
        node.clases_needed = subrequirements.get(node.get_name(), 0)
        node.class_list = courses
        '''print(f"Classes taken for {node.get_name()}: {node.classes_taken}")
        print(f"Classes needed for {node.get_name()}: {node.classes_needed}")
        print()'''
        return used, node.classes_taken, node.classes_needed, node.classes_taken / node.classes_needed, node.class_list#, winning_classes

    # print node's children
    '''for child in node.get_children():
        print(f"Node: {child.get_name()}")'''

    # Recursive case: node with children
    for child_node in node.get_children():
        '''print(f"Used at {child_node.get_name()}: {node.class_list}")
        print()'''
        curr_used, _, _, _, class_list = traverse_tree(child_node, combination_dict, 
                             subrequirements, set(node.class_list))
        if node.get_node_type() == 'AND':
            node.class_list.extend(child_node.class_list)
    
    # Compute classes taken for this node
    _, _, winner = node.compute_classes_taken_needed()

    if node.get_node_type() == 'OR':
        if winner:
            #print(f"Winner: {winner.get_name()}")
            node.class_list.extend(winner.class_list)

    '''print(f"Classes taken for {node.get_name()}: {node.classes_taken}")
    print(f"Classes needed for {node.get_name()}: {node.classes_needed}")
    print()'''

    return used, node.classes_taken, node.classes_needed, node.classes_taken / node.classes_needed, node.class_list

def find_best_combination(key, all_combinations, subrequirements):
    best_fraction = 0
    difference = math.inf
    best_combination = []
    taken_needed = (0, 0)
    best_tree = None

    for combination_dict in all_combinations:
        #print(f"Combination: {combination_dict}")
        # Traverse the tree with the current combination
        root_node = minors.create_tree(key, subrequirements)
        used = set()
        _, taken, needed, fraction_completion, _ = traverse_tree(root_node, 
                                                  combination_dict,
                                                  subrequirements,
                                                  used)
        '''print(f"Classes taken: {taken}")
        print(f"Classes needed: {needed}")
        print(f"Fraction of completion: {fraction_completion}")
        print(f"Class list: {class_list}")'''
        
        #print(f"Fraction of completion: {fraction_completion}")

        # Update best combination based on fraction of completion
        # fraction_completion >= best_fraction
        if taken_needed[1] == 0:
            taken_needed = (taken, needed)
        if needed - taken < difference:
            '''if fraction_completion == best_fraction and (needed - taken) >= difference:
                continue'''
            #best_fraction = fraction_completion
            difference =  needed - taken
            best_combination = combination_dict
            taken_needed = (taken, needed)
            best_tree = root_node
        
        # remove duplicates from winning classes after flattening
        '''winning_classes = [course for sublist in winning_classes for course in sublist]
        winning_classes = list(set(winning_classes))'''
    #print(f"Best tree and children: {best_tree.get_children()}")
    #best_tree = best_path(best_tree)
    best_tree = best_path(root_node)
    print(f"root node and children: {best_tree.get_children()}")

    return best_combination, best_fraction, taken_needed, best_tree


if __name__ == '__main__':
    # testing ENV
    # Class list
    class_list = {
        'Foundation Above 300 2': ['ENV 304', 'ENV 377'],
        'Foundation Above 300 1': ['ENV 304', 'ENV 377'],
        'Foundation Below 300 1': ['ENV 200A'],
        'Elective Above 300 2': ['ENV 304', 'CEE 304'],
        'Elective Above 300 1': ['ENV 304', 'CEE 304'],
        'Elective Below 300 1': ['ENV 200A']

        # class_list: {'Foundational Courses/Above 300-level': ['ENV 304'], 'Elective Courses/Above 300-level': ['ENV 304']}
    }

    # Subrequirements
    subrequirements = {
        'Foundation Above 300 2': 2,
        'Foundation Above 300 1': 1,
        'Foundation Below 300 1': 1,
        'Elective Above 300 2': 2,
        'Elective Above 300 1': 1,
        'Elective Below 300 1': 1
    }
    
    # Generate all combinations of classes
    all_combinations, dict_combinations = generate_combinations(class_list, subrequirements)

    '''dict_combinations = [
        {
            'Foundation Above 300 2': ['ENV 304', 'ENV 377'],
            'Foundation Above 300 1': ['ENV 304'],
            'Foundation Below 300 1': ['ENV 200A'],
            'Elective Above 300 2': ['ENV 304', 'CEE 304'],
            'Elective Above 300 1': ['ENV 304'],
            'Elective Below 300 1': ['ENV 200A']
        },

        {
            'Foundation Above 300 2': [],
            'Foundation Above 300 1': ['ENV 377'],
            'Foundation Below 300 1': ['ENV 200A'],
            'Elective Above 300 2': ['ENV 304', 'CEE 304'],
            'Elective Above 300 1': ['CEE 304'],
            'Elective Below 300 1': ['ENV 200A']
        }
    ]
    #Print all combinations
    for i, combination in enumerate(all_combinations, start=1):
        print(f"Combination {i}: {combination}")

    # Create the ENV tree
    env = minors.create_cla_tree(subrequirements)'''

    best_combination, best_fraction, classes_taken_needed, tree = find_best_combination('ENV', dict_combinations, subrequirements)
    print(f"Best combination: {best_combination}")
    print(f"Best fraction: {best_fraction}")
    print(f"Classes taken and needed: {classes_taken_needed}")
    tree = extract_node_information(tree)

    print(json.dumps(tree, indent=2))


    
    '''# testing COS
    # Class list
    class_list = {
    'Intro Course': ['COS 126', 'ECE 115'],
    'ISC': ['ISC 231', 'ISC 232'],
    'Core Course': ['COS 226', 'COS 217'],
    'Electives': ['COS 226', 'COS 217', 'COS 324']
    }

    # Subrequirements
    subrequirements = {
        "Intro Course": 1,
        "ISC": 4,
        "Core Course": 1,
        "Electives": 3
    }

    # Print all combinations
    for i, combination in enumerate(all_combinations, start=1):
        print(f"Combination {i}: {combination}")

        # Generate all combinations of classes
    all_combinations, dict_combinations = generate_combinations(class_list, subrequirements)

    # Find the best combination
    best_combination, best_fraction, classes_taken_needed = find_best_combination('COS', dict_combinations, subrequirements)
    print(f"Best combination: {best_combination}")
    print(f"Best fraction: {best_fraction}")
    print(f"Classes taken and needed: {classes_taken_needed}")

    # testing CLA
    
    class_list = {
        "Prerequisites": ["CLA 219", "CLA 212", "CLG 108"],
        "Basic Requirements": ["CLA 212"],
        "Greek 4": [],
        "Relevant Courses": ['CLA 219', 'CLA 212', 'CLA 247', 'LAT 336', 'LAT 333', 'LAT 315'],
        "Greek 5": [],
        "Latin 4": ["LAT 336", "LAT 333", "LAT 315"],
        "Latin 5": ["LAT 336", "LAT 333", "LAT 315"],
        "Medicine 5": [],
        "Medicine 4": [],
        "Historical Survey": ["CLA 219"],
        "Track Requirements": ["CLA 219", 'CLA 247']
    }

    subrequirements = {
        "Prerequisites": 1,
        "Basic Requirements": 1,
        "Greek 4": 2,
        "Relevant Courses": 1,
        "Greek 5": 3,
        "Latin 4": 2,
        "Latin 5": 3,
        "Medicine 5": 3,
        "Medicine 4": 2,
        "Historical Survey": 2,
        "Track Requirements": 2
    }

    # Combinations
    # Print all combinations
    all_combinations, dict_combinations = generate_combinations(class_list, subrequirements)

    # Define all_combinations as a list of dictionaries
    dict_combinations = [
        {
            "Prerequisites": ["CLA 219"],
            "Basic Requirements": ["CLA 212"],
            "Greek 4": [],
            "Relevant Courses": ['LAT 315'],
            "Greek 5": [],
            "Latin 4": ["LAT 336", "LAT 333", "LAT 315"],
            "Latin 5": ["LAT 336", "LAT 333", "LAT 315"],
            "Medicine 5": [],
            "Medicine 4": [],
            "Historical Survey": ["CLA 219"],
            "Track Requirements": []
        },
        {
            "Prerequisites": ["CLA 219"],
            "Basic Requirements": ["CLA 212"],
            "Greek 4": [],
            "Relevant Courses": ['CLA 247'],
            "Greek 5": [],
            "Latin 4": ["LAT 336", "LAT 333", "LAT 315"],
            "Latin 5": ["LAT 336", "LAT 333", "LAT 315"],
            "Medicine 5": [],
            "Medicine 4": [],
            "Historical Survey": ["CLA 219"],
            "Track Requirements": []
        },
        {
            "Prerequisites": ["CLA 219"],
            "Basic Requirements": ["CLA 212"],
            "Greek 4": [],
            "Relevant Courses": ['CLA 219'],
            "Greek 5": [],
            "Latin 4": ["LAT 336", "LAT 333", "LAT 315"],
            "Latin 5": [],
            "Medicine 5": [],
            "Medicine 4": [],
            "Historical Survey": [],
            "Track Requirements": []
        }
    ]
    # Print all combinations
    for i, combination in enumerate(all_combinations, start=1):
        print(f"Combination {i}: {combination}")

    for i, combo in enumerate(dict_combinations, start=1):
        print(f"Combination {i}:")
        for category, selected_class in combo.items():
            print(f"  {category}: {selected_class}")
    # Find the best combination
    best_combination, best_fraction, classes_taken_needed = find_best_combination('CLA', dict_combinations, subrequirements)
    print(f"Best combination: {best_combination}")
    print(f"Best fraction: {best_fraction}")
    print(f"Classes taken and needed: {classes_taken_needed}")

    # testing FIN
    # Class list
    class_list = {
        'MAT 175': [],
        'Advanced Math': [],
        'BSE Math': ['MAT 201', 'MAT 202'],
        'EGR': [],
        'Micro': ['ECO 300'],
        'Probability/Stats': ['ORF 245'],
        'Core': [],
        'Finanical Applications 1': [],
        'Finanical Applications 2': [],
        'General Electives 1': [],
        'General Electives 2': []
    }

    # Subrequirements
    subrequirements = {
        'MAT 175': 1,
        'Advanced Math': 1,
        'BSE Math': 2,
        'EGR': 1,
        'Micro': 1,
        'Probability/Stats': 1,
        'Core': 2,
        'Finanical Applications 1': 1,
        'Finanical Applications 2': 2,
        'General Electives 1': 1,
        'General Electives 2': 2
    }

    # Generate all combinations of classes
    all_combinations, dict_combinations = generate_combinations(class_list, subrequirements)
    
    # Find the best combination
    best_combination, best_fraction, classes_taken_needed = find_best_combination('FIN', dict_combinations, subrequirements)
    print(f"Best combination: {best_combination}")
    print(f"Best fraction: {best_fraction}")
    print(f"Classes taken and needed: {classes_taken_needed}")

    # testing LIN
    # Class list

    class_list = {
        'Prerequisites': ['LIN 201'],
        'Core Courses 1': [],
        'Core Courses 2': [],
        'Methods 1': [],
        'Methods 2': [],
        'Electives 1': ['LIN 201', 'LIN 214', 'LIN 205'],
        'Electives 2': ['LIN 201', 'LIN 214', 'LIN 205']
    }

    # Subrequirements
    subrequirements = {
        'Prerequisites': 1,
        'Core Courses 1': 1,
        'Core Courses 2': 2,
        'Methods 1': 1,
        'Methods 2': 2,
        'Electives 1': 1,
        'Electives 2': 2
    }

    # Generate all combinations of classes
    all_combinations, dict_combinations = generate_combinations(class_list, subrequirements)

    # Find the best combination
    best_combination, best_fraction, classes_taken_needed = find_best_combination('LIN', dict_combinations, subrequirements)
    print(f"Best combination: {best_combination}")
    print(f"Best fraction: {best_fraction}")
    print(f"Classes taken and needed: {classes_taken_needed}")'''
