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

    def compute_classes_needed(self):
        if self.children:
            self.classes_needed = sum(child.compute_classes_needed() for child in self.children)
        return self.classes_needed

    def compute_classes_taken(self):
        if self.children:
            self.classes_taken = sum(child.compute_classes_taken() for child in self.children)
        return self.classes_taken

    def update_classes_needed(self):
        for child in self.children:
            child.update_classes_needed()
        self.compute_classes_needed()


class OrNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.node_type = 'OR'

    def compute_classes_needed(self):
        if self.children:
            max_classes_needed = max(child.compute_classes_needed() for child in self.children)
            return max_classes_needed
        return 0  # OrNode itself doesn't have a specific classes_needed

    def compute_classes_taken(self):
        if self.children:
            max_fraction = max(child.compute_classes_taken() / child.classes_needed for child in self.children)
            self.classes_taken = int(max_fraction * self.classes_needed)
        return self.classes_taken


def create_tree(subrequirements, parent=None):
    # Create the root node for CLA minor
    cla = Node('CLA', parent)

    # Create the Prerequisites node under CLA
    prerequisites = Node('Prerequisites', parent=cla, classes_needed=subrequirements.get('Prerequisites', 0))
    cla.add_child(prerequisites)

    # Create the Tracks (OR node) under CLA
    tracks = Node('Tracks', parent=cla)

    # Create Classical Track (AND node) under Tracks
    classical = Node('Classical Track', parent=tracks)

    # Create Basic Requirements (AND node) under Classical Track
    basic_reqs = Node('Basic Requirements', parent=classical, classes_needed=subrequirements.get('Basic Requirements', 0))
    classical.add_child(basic_reqs)

    # Create Subtracks (OR node) under Classical Track
    subtracks = Node('Subtracks', parent=classical)

    # Create Greek (OR node) under Subtracks
    greek = Node('Greek', parent=subtracks)
    greek_4 = Node('Greek 4 and Relevant 4', parent=greek)
    greek_4.add_child(Node('Greek 4', parent=greek_4, classes_needed=subrequirements.get('Greek 4', 0)))
    greek_4.add_child(Node('Relevant Courses', parent=greek_4, classes_needed=subrequirements.get('Relevant Courses', 0)))
    greek.add_child(greek_4)
    greek.add_child(Node('Greek 5', parent=greek, classes_needed=subrequirements.get('Greek 5', 0)))
    subtracks.add_child(greek)

    # Create Latin (OR node) under Subtracks
    latin = Node('Latin', parent=subtracks)
    latin_4 = Node('Latin 4 and Relevant 4', parent=latin)
    latin_4.add_child(Node('Latin 4', parent=latin_4, classes_needed=subrequirements.get('Latin 4', 0)))
    latin_4.add_child(Node('Relevant Courses', parent=latin_4, classes_needed=subrequirements.get('Relevant Courses', 0)))
    latin.add_child(latin_4)
    latin.add_child(Node('Latin 5', parent=latin, classes_needed=subrequirements.get('Latin 5', 0)))
    subtracks.add_child(latin)

    # Create Medicine (OR node) under Subtracks
    medicine = Node('Medicine', parent=subtracks)
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

    # Update classes_needed recursively
    cla.update_classes_needed()

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

    print("All combinations:")
    for category, combo in all_combinations.items():
        print(f"{category}: {combo}")
    
    all_combinations_product = list(product(*list(all_combinations.values())))

    # Transform combinations into list of dictionaries
    combined_combinations = []
    for combo in all_combinations_product:
        category_map = {}
        for idx, (category, combos) in enumerate(all_combinations.items()):
            category_map[category] = combo[idx]
        combined_combinations.append(category_map)

    return all_combinations_product, combined_combinations

def traverse_tree(node, combination_dict, used):
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
        return used

    # Recursive case: node with children
    # CLA 219, CLA 212
    for child_node in node.get_children():
        used = traverse_tree(child_node, combination_dict, used)
    
    # Compute classes taken for this node
    node.compute_classes_taken()

def find_best_combination(root_node, all_combinations):
    best_fraction = 0
    best_combination = None

    for combination_dict in all_combinations:
        # Traverse the tree with the current combination
        _, _, fraction_completion = traverse_tree(root_node, combination_dict)

        # Update best combination based on fraction of completion
        if fraction_completion > best_fraction:
            best_fraction = fraction_completion
            best_combination = combination_dict

    return best_combination, best_fraction


'''def _fulfill_base_reqs(combination, dependencies, base_reqs, dependent_reqs, subrequirements):
    fulfilled_requirements = {requirement: {'classes': [], 'count': 0} for requirement in dependencies}
    
    def fulfill_dependency(dependency, units, classes):
        if fulfilled_requirements[dependency]['count'] + units <= subrequirements[dependency][1]:
            fulfilled_requirements[dependency]['count'] += units
            fulfilled_requirements[dependency]['classes'].extend(classes)
        else:
            return
        dependent_dependency = dependencies.get(dependency, '')
        if dependent_dependency in dependent_reqs:
            fulfill_dependency(dependent_dependency, units, classes)
        return
    
    for i, base_req in enumerate(combination):
        if base_req:
            classes = base_req
            fulfilled_requirements[base_reqs[i]]['count'] += len(base_req)
            fulfilled_requirements[base_reqs[i]]['classes'].extend(classes)
            
            dependency = dependencies.get(base_reqs[i], '')
            if dependency in dependent_reqs:
                if subrequirements[base_reqs[i]][1] - subrequirements[base_reqs[i]][0] == 0:
                    units = 1
                else:
                    units = len(base_req)
                fulfill_dependency(dependency, units, classes)
                
    return fulfilled_requirements

# Function to check the max number of requirements fulfillable
def max_reqs_fulfilled(combinations, dependencies, base_reqs, dependent_reqs, subrequirements):
    # list of all combinations and the requirements they can fill
    reqs_fulfilled = []
    
    # check each combination to see which requirements it fulfills
    for combination in combinations:
        reqs_fulfilled.append(_fulfill_base_reqs(combination, 
                          dependencies, 
                          base_reqs,
                          dependent_reqs,
                          subrequirements))
    print("Requirements fulfilled:")
    for index, fulfilled in enumerate(reqs_fulfilled, start=1):
        print(f"Combination {index}:")
        for requirement, info in fulfilled.items():
            print(f"\t{requirement}:")
            print(f"\t\tClasses: {info['classes']}")
            print(f"\t\tCount: {info['count']}")
    main_reqs = [req for req in dependencies if dependencies[req] == '']
    closest = [0, {}, {}]
    champ_dist = float('inf')
    count = 0
    for fulfilled in reqs_fulfilled:
        mains_dist = 0
        mains_filled = 0
        class_fit_req = {req: [] for req in main_reqs}

        for req in main_reqs:
            # distance between main requirements being fulfilled
            mains_dist += subrequirements[req][1] - fulfilled[req]['count']
            # print(f"Distance from main requirements at {count}:", mains_dist)

            if fulfilled[req]['count'] == subrequirements[req][1]:
                mains_filled += 1
                class_fit_req[req] = fulfilled[req]['classes']
        
        if mains_dist < champ_dist:
            champ_dist = mains_dist
            closest = [mains_filled, class_fit_req, fulfilled]
        count += 1
    return closest'''

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

    # Dependencies
    dependencies = {
        'Foundational Courses/Above 300-level': 'Foundational Courses',
        'Foundational Courses/Below 300-level': 'Foundational Courses',
        'Elective Courses/Above 300-level': 'Elective Courses',
        'Elective Courses/Below 300-level': 'Elective Courses',
        'Foundational Courses': '',
        'Elective Courses': ''
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
        "Prerequisities": ["CLA 219", "CLA 212", "CLG 108"],
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
        "Prerequisities": 1,
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
     # Print all combinations
    for i, combination in enumerate(all_combinations, start=1):
        print(f"Combination {i}: {combination}")

    for i, combo in enumerate(dict_combinations, start=1):
        print(f"Combination {i}:")
        for category, selected_class in combo.items():
            print(f"  {category}: {selected_class}")
