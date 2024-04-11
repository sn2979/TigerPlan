import itertools
from itertools import product, combinations
class Node:
    def __init__(self, name, parent=None, classes_needed=0):
        self.name = name
        self.children = []
        self.node_type = 'AND'
        self.classes_needed = classes_needed
        self.classes_taken = 0
        self.parent = parent
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def get_name(self):
        return self.name
    
    def get_node_type(self):
        return self.node_type
    
    def get_classes_needed(self):
        return self.classes_needed
    
    def get_classes_taken(self):
        return self.classes_taken

    def add_child(self, child_node):
        self.children.append(child_node)

    def compute_classes_taken_needed(self):
        if self.children:
            winner = []
            self.classes_taken = sum(child.classes_taken for child in self.children)
            self.classes_needed = sum(child.classes_needed for child in self.children)
            winner = [child.name for child in self.children if child.classes_taken > 0]
        return self.classes_taken, self.classes_needed, winner


class OrNode(Node):
    def __init__(self, name, parent=None, classes_needed=0):
        super().__init__(name)
        self.node_type = 'OR'
        self.classes_needed = classes_needed
        self.classes_taken = 0
        self.parent = parent

    def compute_classes_taken_needed(self):
        if self.children:
            max_fraction = 0
            for child in self.children:
                fraction = child.classes_taken / child.classes_needed
                winner = []
                if fraction >= max_fraction:
                    max_fraction = fraction
                    self.classes_taken = int(max_fraction * child.classes_needed)
                    self.classes_needed = child.classes_needed
                    winner.append(child.name)
                    
        return self.classes_taken, self.classes_needed, winner


def create_tree(subrequirements, parent=None):
    # Create the root node for CLA minor
    cla = Node('CLA', parent)

    # Create the Prerequisites node under CLA
    prerequisites = Node('Prerequisites', parent=cla, classes_needed=subrequirements.get('Prerequisites', 0))
    cla.add_child(prerequisites)

    # Create the Tracks (OR node) under CLA
    tracks = OrNode('Tracks', parent=cla)

    # Create Classical Track (AND node) under Tracks
    classical = Node('Classical Track', parent=tracks)

    # Create Basic Requirements (AND node) under Classical Track
    basic_reqs = Node('Basic Requirements', parent=classical, classes_needed=subrequirements.get('Basic Requirements', 0))
    classical.add_child(basic_reqs)

    # Create Subtracks (OR node) under Classical Track
    subtracks = OrNode('Subtracks', parent=classical)

    # Create Greek (OR node) under Subtracks
    greek = OrNode('Greek', parent=subtracks)
    greek_4 = Node('Greek 4 and Relevant 4', parent=greek)
    greek_4.add_child(Node('Greek 4', parent=greek_4, classes_needed=subrequirements.get('Greek 4', 0)))
    greek_4.add_child(Node('Relevant Courses', parent=greek_4, classes_needed=subrequirements.get('Relevant Courses', 0)))
    greek.add_child(greek_4)
    greek.add_child(Node('Greek 5', parent=greek, classes_needed=subrequirements.get('Greek 5', 0)))
    subtracks.add_child(greek)

    # Create Latin (OR node) under Subtracks
    latin = OrNode('Latin', parent=subtracks)
    latin_4 = Node('Latin 4 and Relevant 4', parent=latin)
    latin_4.add_child(Node('Latin 4', parent=latin_4, classes_needed=subrequirements.get('Latin 4', 0)))
    latin_4.add_child(Node('Relevant Courses', parent=latin_4, classes_needed=subrequirements.get('Relevant Courses', 0)))
    latin.add_child(latin_4)
    latin.add_child(Node('Latin 5', parent=latin, classes_needed=subrequirements.get('Latin 5', 0)))
    subtracks.add_child(latin)

    # Create Medicine (OR node) under Subtracks
    medicine = OrNode('Medicine', parent=subtracks)
    medicine_4 = Node('Medicine 4 and Relevant 4', parent=medicine)
    medicine_4.add_child(Node('Medicine 4', parent=medicine_4, classes_needed=subrequirements.get('Medicine 4', 0)))
    medicine_4.add_child(Node('Relevant Courses', parent=medicine_4, classes_needed=subrequirements.get('Relevant Courses', 0)))
    medicine.add_child(medicine_4)
    medicine.add_child(Node('Medicine 5', parent=medicine, classes_needed=subrequirements.get('Medicine 5', 0)))
    subtracks.add_child(medicine)

    # Add Subtracks under Classical Track
    classical.add_child(subtracks)

    # Add Classical Track under Tracks
    tracks.add_child(classical)

    # Create Ancient History Track (AND node) under Tracks
    ancient = Node('Ancient History Track', parent=tracks)
    ancient.add_child(Node('Historical Survey', parent=ancient, classes_needed=subrequirements.get('Historical Survey', 0)))
    ancient.add_child(Node('Track Requirements', parent=ancient, classes_needed=subrequirements.get('Track Requirements', 0)))
    ancient.add_child(Node('Relevant Courses', parent=ancient, classes_needed=subrequirements.get('Relevant Courses', 0)))

    # Add Ancient History Track under Tracks
    tracks.add_child(ancient)

    # Add Tracks under CLA
    cla.add_child(tracks)

    return cla
    
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

    return all_combinations_product, combined_combinations

def traverse_tree(node, combination_dict, 
                  subrequirements, used, winning_classes={}):
    # Base case: child node with no children
    if node.get_children() == []:
        # Get classes taken for this requirement

        # First section checks to make sure if the parent is an AND node, 
        # the classes are not repeated
        combination = combination_dict.get(node.get_name(), [])
        taken = len(combination)
        for course in combination:
            if course in used:
                taken -= 1
            else:
                if node.get_parent().get_node_type() == 'AND':
                    used.add(course)
        node.classes_taken = taken
        node.clases_needed = subrequirements.get(node.get_name(), 0)
        '''print(f"Classes taken for {node.get_name()}: {node.classes_taken}")
        print(f"Classes needed for {node.get_name()}: {node.classes_needed}")
        print()'''
        return used, node.classes_taken, node.classes_needed, node.classes_taken / node.classes_needed, winning_classes

    # Recursive case: node with children
    curr_used = used.copy()
    for child_node in node.get_children():
        curr_used, _, _, _ , _= traverse_tree(child_node, combination_dict, 
                             subrequirements, set(curr_used))
        '''print(f"Used at {node.get_name()}: {curr_used}")
        print()'''
    
    # Compute classes taken for this node
    _, _, winner = node.compute_classes_taken_needed()
    if winner:
        for requirement in winner:
            print(f"Winner: {requirement}")
            for course in combination_dict.get(requirement, []):
                winners = set(list(itertools.chain.from_iterable(winning_classes.values())))
                print(f"Winners: {winners}")
                print()
                if course not in winners:
                    if requirement not in winning_classes:
                        winning_classes[requirement] = [course]
                    else:
                        winning_classes[requirement].append(course)
        
        print(f"Winning classes: {winning_classes}")
        print()

    '''print(f"Classes taken for {node.get_name()}: {node.classes_taken}")
    print(f"Classes needed for {node.get_name()}: {node.classes_needed}")
    print()'''

    return used, node.classes_taken, node.classes_needed, node.classes_taken / node.classes_needed, winning_classes

def find_best_combination(root_node, all_combinations, 
                                                subrequirements):
    best_fraction = 0
    best_combination = None
    taken_needed = None

    for combination_dict in all_combinations:
        #print(f"Combination: {combination_dict}")
        # Traverse the tree with the current combination
        used = set()
        _, taken, needed, fraction_completion, winning_classes = traverse_tree(root_node, 
                                                  combination_dict,
                                                  subrequirements,
                                                  used)
        
        #print(f"Fraction of completion: {fraction_completion}")

        # Update best combination based on fraction of completion
        if fraction_completion > best_fraction:
            best_fraction = fraction_completion
            best_combination = combination_dict
            taken_needed = (taken, needed)
        
        # remove duplicates from winning classes after flattening
        '''winning_classes = [course for sublist in winning_classes for course in sublist]
        winning_classes = list(set(winning_classes))'''

    return best_combination, best_fraction, taken_needed, winning_classes


if __name__ == '__main__':
    '''# testing ENV
    # Class list
    class_list = {
        # class_list: ['COS 126', 'ECE 115', 'MAT 301', 'ANT 314', 'ENV 304', 'COS 217', 'COS 324']
        'Foundational Courses/Above 300-level': ['ENV 304', 'ENV 377'],
        'Foundational Courses/Below 300-level': ['ENV 200A'],
        'Elective Courses/Above 300-level': ['ENV 304', 'CEE 304'],
        'Elective Courses/Below 300-level': ['ENV 200A']

        # class_list: {'Foundational Courses/Above 300-level': ['ENV 304'], 'Elective Courses/Above 300-level': ['ENV 304']}
    }

    # Subrequirements
    subrequirements = {
        'Foundational Courses/Above 300-level': [1, 2],
        'Foundational Courses/Below 300-level': [1, 1],
        'Elective Courses/Above 300-level': [2, 3],
        'Elective Courses/Below 300-level': [1, 1],
        'Foundational Courses': [2, 2],
        'Elective Courses': [3, 3]
    }
    
    base_reqs = ['Foundational Courses/Above 300-level', 
                         'Foundational Courses/Below 300-level', 
                         'Elective Courses/Above 300-level', 
                         'Elective Courses/Below 300-level']
    
    dependent_reqs = ['Foundational Courses', 'Elective Courses']
    # Generate all combinations of classes
    all_combinations = generate_combinations(class_list, subrequirements)

    # Print all combinations
    for i, combination in enumerate(all_combinations, start=1):
        print(f"Combination {i}: {combination}")

    # Check the maximum number of requirements fulfillable
    max_fulfilled = max_reqs_fulfilled(all_combinations, dependencies, base_reqs, dependent_reqs, subrequirements)
    print(f"Maximum number of requirements fulfillable: {max_fulfilled[0]}")
    print(f"Classes that fulfill the main requirements: {max_fulfilled[1]}")
    print("Requirements fulfilled:")
    print(max_fulfilled[2])
    for requirement, info in max_fulfilled[2].items():
        print(f"\t{requirement}:")
        print(f"\t\tClasses: {info['classes']}")
        print(f"\t\tCount: {info['count']}")
    
    # testing COS
    # Class list
    class_list = {
    'Core/Introduction/Introductory Course': ['COS 126', 'ECE 115'],
    'Core/Introduction/Integrated Science Curriculum': ['ISC 231', 'ISC 232'],
    'Core/Core Course': ['COS 226', 'COS 217'],
    'Electives': ['COS 226', 'COS 217', 'COS 324']
    }

    # Dependencies
    dependencies = {
    'Core/Introduction/Introductory Course': 'Core/Introduction',
    'Core/Introduction/Integrated Science Curriculum': 'Core/Introduction',
    'Core/Introduction': 'Core',
    'Core/Core Course': 'Core',
    'Core': '',
    'Electives': ''
    }

    # Subrequirements
    subrequirements = {
    'Core/Introduction/Introductory Course': [1, 1], # [min number of courses needed to fulfill requirement, max number of courses that can be used to fulfill requirement]
    'Core/Introduction/Integrated Science Curriculum': [4, 4],
    'Core/Introduction': [1, 1],
    'Core/Core Course': [1, 1],
    'Core': [2,2],
    'Electives': [3, 3]
    }
    
    base_reqs = ['Core/Introduction/Introductory Course', 
                    'Core/Introduction/Integrated Science Curriculum', 
                    'Core/Core Course', 
                    'Electives']
    dependent_reqs = ['Core/Introduction', 'Core']

    # Generate all combinations of classes
    all_combinations = generate_combinations(class_list, subrequirements)

    # Print all combinations
    for i, combination in enumerate(all_combinations, start=1):
        print(f"Combination {i}: {combination}")

    # Check the maximum number of requirements fulfillable
    max_fulfilled = max_reqs_fulfilled(all_combinations, dependencies, base_reqs, dependent_reqs, subrequirements)
    print(f"Maximum number of requirements fulfillable: {max_fulfilled[0]}")
    print(f"Classes that fulfill the requirements: {max_fulfilled[1]}")
    print("Requirements fulfilled:")
    for requirement, info in max_fulfilled[2].items():
        print(f"\t{requirement}:")
        print(f"\t\tClasses: {info['classes']}")
        print(f"\t\tCount: {info['count']}")'''

    
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
        "Greek 4": 4,
        "Relevant Courses": 1,
        "Greek 5": 5,
        "Latin 4": 4,
        "Latin 5": 5,
        "Medicine 5": 5,
        "Medicine 4": 4,
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
    '''for i, combination in enumerate(all_combinations, start=1):
        print(f"Combination {i}: {combination}")

    for i, combo in enumerate(dict_combinations, start=1):
        print(f"Combination {i}:")
        for category, selected_class in combo.items():
            print(f"  {category}: {selected_class}")'''
    
    # Create the tree
    cla = create_tree(subrequirements)

    # Find the best combination
    best_combination, best_fraction, classes_taken_needed, winning_classes = find_best_combination(cla, dict_combinations, subrequirements)
    print(f"Best combination: {best_combination}")
    print(f"Best fraction: {best_fraction}")
    print(f"Classes taken and needed: {classes_taken_needed}")
    print(f"Winning classes: {winning_classes}")
