from itertools import product, combinations

def generate_combinations(class_list, subrequirements):
    #print("Generating combinations...")
    # Generate all possible combinations of classes
    all_combinations = []
    for category, classes in class_list.items():
        #print(f"Category: {category}, Classes: {classes}")
        # Get the minimum and maximum number of classes required for this category
        min_classes = subrequirements[category][0]
        max_classes = subrequirements[category][1]
        #print(f"Min classes: {min_classes}, Max classes: {max_classes}")

        # Generate combinations of classes for this category
        category_combinations = [()]
        for r in range(min_classes, max_classes + 1):
            category_combinations.extend(combinations(classes, r))

        #print(f"Category combinations: {category_combinations}")
        all_combinations.append(category_combinations)

    print("All combinations:", all_combinations)
    all_combinations = list(product(*all_combinations))
    
    # Filter out duplicate versions and combinations where a class occurs more than once
    filtered_combinations = []
    for combo in all_combinations:
        flattened_combo = [item for sublist in combo for item in sublist]  # Flatten the combination
        if len(flattened_combo) == len(set(flattened_combo)):  # Check if no class occurs more than once
            if combo not in filtered_combinations:  # Check if not duplicate version
                filtered_combinations.append(combo)

    return filtered_combinations

def _fulfill_base_reqs(combination, dependencies, base_reqs, dependent_reqs, subrequirements):
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
    reqs_fulfilled = []
    # Iterate over reversed class_list and count fulfilled requirements
    for combination in combinations:
        reqs_fulfilled.append(_fulfill_base_reqs(combination, 
                          dependencies, 
                          base_reqs,
                          dependent_reqs,
                          subrequirements))
    '''print("Requirements fulfilled:")
    for index, fulfilled in enumerate(reqs_fulfilled, start=1):
        print(f"Combination {index}:")
        for requirement, info in fulfilled.items():
            print(f"\t{requirement}:")
            print(f"\t\tClasses: {info['classes']}")
            print(f"\t\tCount: {info['count']}")'''
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
    return closest

if __name__ == '__main__':
    # testing ENV
    # Class list
    class_list = {
        'Foundational Courses/Above 300-level': ['ENV 304', 'ENV 377'],
        'Foundational Courses/Below 300-level': ['ENV 200A'],
        'Elective Courses/Above 300-level': ['ENV 304', 'CEE 304'],
        'Elective Courses/Below 300-level': ['ENV 200A']
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
        'Elective Courses': [3,3]
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
    
    '''# Given combinations you want to check
    combinations_to_check = [
        [('ENV 304',), (), (), ()],
        [('ENV 304',), ('ENV 200A',), (), ()],
        [('ENV 304',), (), (), ('ENV 200A',)],
        [('ENV 377',), (), ('ENV 304', 'CEE 304'), ()],
        [('ENV 377',), ('ENV 200A',), ('ENV 304', 'CEE 304'), ()],
        [('ENV 377',), (), ('ENV 304', 'CEE 304'), ('ENV 200A',)],
        [('ENV 304', 'ENV 377'), (), (), ()],
        [('ENV 304', 'ENV 377'), ('ENV 200A',), (), ()],
        [('ENV 304', 'ENV 377'), (), (), ('ENV 200A',)]
    ]
    given_combinations = [
        [(), (), (), ()],
        [(), (), (), ('ENV 200A',)],
        [(), (), ('ENV 304', 'CEE 304'), ()],
        [(), (), ('ENV 304', 'CEE 304'), ('ENV 200A',)],
        [(), ('ENV 200A',), (), ()],
        [(), ('ENV 200A',), ('ENV 304', 'CEE 304'), ()],
        [('ENV 304',), (), (), ()],
        [('ENV 304',), (), (), ('ENV 200A',)],
        [('ENV 304',), ('ENV 200A',), (), ()],
        [('ENV 377',), (), (), ()],
        [('ENV 377',), (), (), ('ENV 200A',)],
        [('ENV 377',), (), ('ENV 304', 'CEE 304'), ()],
        [('ENV 377',), (), ('ENV 304', 'CEE 304'), ('ENV 200A',)],
        [('ENV 377',), ('ENV 200A',), (), ()],
        [('ENV 377',), ('ENV 200A',), ('ENV 304', 'CEE 304'), ()],
        [('ENV 304', 'ENV 377'), (), (), ()],
        [('ENV 304', 'ENV 377'), (), (), ('ENV 200A',)],
        [('ENV 304', 'ENV 377'), ('ENV 200A',), (), ()]
    ]
    # Check if given combinations are contained in the list of combinations
    for i, combo_to_check in enumerate(combinations_to_check, start=1):
        if combo_to_check in given_combinations:
            print(f"Combination {i} is contained in the list.")
        else:
            print(f"Combination {i} is not contained in the list.")'''
    
    # testing COS
    # Class list
    class_list = {
    'Core/Introduction/Introductory Course': ['COS 126', 'ECE 115'],
    'Core/Introduction/Integrated Science Curriculum': ['ISC 231', 'ISC 232'],
    'Core/Core Course': ['COS 226', 'COS 217'],
    'Electives': ['COS 226', 'COS 217', 'COS 324', 'COS 333', 'COS 340']
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
    'Core/Introduction': [1,1],
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
        print(f"\t\tCount: {info['count']}")
