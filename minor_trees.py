class Node:
    def __init__(self, name, parent=None, classes_needed=0):
        self.name = name
        self.children = []
        self.node_type = 'AND'
        self.classes_needed = classes_needed
        self.classes_taken = 0
        self.parent = parent
        self.class_list = []
    
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
    
    def get_class_list(self):
        return self.class_list

    def add_child(self, child_node):
        self.children.append(child_node)

    def compute_classes_taken_needed(self):
        if self.children:
            winner = []
            self.classes_taken = sum(child.classes_taken for child in self.children)
            self.classes_needed = sum(child.classes_needed for child in self.children)
            winner = [child for child in self.children if child.classes_taken > 0]
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
                    winner = child
        return self.classes_taken, self.classes_needed, winner


def create_cla_tree(subrequirements, parent=None):
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

def create_env_tree(subrequirements, parent=None):
    # Create the root node for ENV minor
    env = Node('ENV', parent)

    # Create the Foundation node under ENV
    foundation = OrNode('Foundation', parent=env)
    env.add_child(foundation)

    # Create the Electives node under ENV
    electives = OrNode('Electives', parent=env)
    env.add_child(electives)
    
    # Create the foundation paths
    foundation.add_child(Node('Foundation Above 300 2', 
                             parent=foundation,
                             classes_needed=subrequirements.get('Foundation Above 300 2', 0)))
    
    f_1_above_1_below = Node('Foundation Above 300 1 and Below 300 1', 
                             parent=foundation, 
                             classes_needed=subrequirements.get('Foundation Above 300 1 and Below 300 1', 0))
    f_1_above_1_below.add_child(Node('Foundation Above 300 1', 
                                     parent=f_1_above_1_below, 
                                     classes_needed=subrequirements.get('Foundation Above 300 1', 0)))
    f_1_above_1_below.add_child(Node('Foundation Below 300 1',
                                     parent=f_1_above_1_below,
                                     classes_needed=subrequirements.get('Foundation Below 300 1', 0)))
    foundation.add_child(f_1_above_1_below)

    # Create the elective paths
    electives.add_child(Node('Elective Above 300 2',
                            parent=electives,
                            classes_needed=subrequirements.get('Elective Above 300 2', 0)))
    e_1_above_1_below = Node('Elective Above 300 1 and Below 300 1',
                             parent=electives,
                             classes_needed=subrequirements.get('Elective Above 300 1 and Below 300 1', 0))
    e_1_above_1_below.add_child(Node('Elective Above 300 1',
                                     parent=e_1_above_1_below,
                                     classes_needed=subrequirements.get('Elective Above 300 1', 0)))
    e_1_above_1_below.add_child(Node('Elective Below 300 1',
                                     parent=e_1_above_1_below,
                                     classes_needed=subrequirements.get('Elective Below 300 1', 0)))
    electives.add_child(e_1_above_1_below)

    return env