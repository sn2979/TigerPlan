import re
import courses as course_dicts
import recommender2
import math
import threading
import database_files.student_database as student_database

def categorize_courses(course_list, minor_requirements):
    categorized_courses = {}
    for category, courses_needed in minor_requirements.items():
        categorized_courses[category] = []
        for course in course_list:
            for pattern in courses_needed:
                if re.match(pattern, course):
                    categorized_courses[category].append(course)
                    break 

    return categorized_courses

def process_minor(username, minor, class_list, champions, lock):
    if minor == student_database.get_student_major(username):
        return
    courses = categorize_courses(class_list, course_dicts.get_courses(minor))
    subrequirements = course_dicts.get_minor_requirements(minor)

    _, combinations = recommender2.generate_combinations(courses, subrequirements)
    if len(combinations) == 0:
        best_combination = []
        tree_description = ''
        distance = 100
    else:
        best_combination, _, classes_taken_needed, _, tree_description = recommender2.find_best_combination(minor, combinations, subrequirements)
        distance = classes_taken_needed[1] - classes_taken_needed[0]
        print("Minor:", minor, "Distance:", distance)

    with lock:
        if distance < champions['champion1']['distance']:
            champions['champion3'] = champions['champion2']
            champions['champion2'] = champions['champion1']
            champions['champion1'] = {'distance': distance, 
                                      'minor': minor, 
                                      'best_combination': best_combination, 
                                      'tree_description': tree_description}
        elif distance < champions['champion2']['distance']:
            champions['champion3'] = champions['champion2']
            champions['champion2'] = {'distance': distance, 
                                      'minor': minor, 
                                      'best_combination': best_combination,
                                      'tree_description': tree_description}
        elif distance < champions['champion3']['distance']:
            champions['champion3'] = {'distance': distance, 
                                      'minor': minor, 
                                      'best_combination': best_combination,
                                      'tree_description': tree_description}

def recommend(class_list, username):
    minors = ['CLA', 'ENV', 'LIN', 'COS', 'FIN', 'GSS', 'AFS', 'ASA', 
              'CHI', 'CS', 'CWR', 'DAN', 'EAS', 'ENG', 'GHP', 'HIS', 
              'HLS', 'HSTM', 'HUM', 'JPN', 'JRN', 'KOR', 'LAO', 'MED',
              'MPP', 'MQE', 'MSE', 'MUS', 'NEU', 'PHI', 'RES', 'SAS',
              'SLA', 'SML', 'TMT', 'TRA', 'VIS', 'VPL']

    champions = {
        'champion1': {'distance': math.inf, 'minor': '', 'best_combination': [], 'tree_description': ''},
        'champion2': {'distance': math.inf, 'minor': '', 'best_combination': [],  'tree_description': ''},
        'champion3': {'distance': math.inf, 'minor': '', 'best_combination': [],  'tree_description': ''}
    }

    lock = threading.Lock()

    threads = []
    for minor in minors:
        t = threading.Thread(target=process_minor, args=(username, minor, class_list, champions, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    top_champions = [
        champions['champion1'],
        champions['champion2'],
        champions['champion3']
    ]

    
    filtered_champions = []

    
    for champion in top_champions:
        if champion['distance'] != 100:
            filtered_champions.append(champion)

    top_champions = filtered_champions

    return top_champions


if __name__ == "__main__":
    # testing categorize_courses()

    my_courses = student_database.get_student_coursenums("sn2979")

    # Specify the requirements for the CLA minor with regular expressions
    cla_minor_requirements = course_dicts.cla_minor_courses()

    # Call the function to categorize courses based on CLA minor requirements
    categorized_courses = categorize_courses(my_courses, cla_minor_requirements)

    # Print the categorized courses for each category
    for category, courses in categorized_courses.items():
        print(f"{category}: {courses}")
    
    # testing recommend()
    top_champions = recommend(my_courses, username="sn2979")

    # Print the top 3 recommended minors in a formatted way including distance and best combination
    print("Top 3 recommended minors:")
    for i, champion in enumerate(top_champions, start=1):
        print(f"{i}. {champion['minor']}: {champion['distance']} classes away")
        print(f"   Best combination: {champion['best_combination']}")
        print(f"   Tree Description: {champion['tree_description']}")