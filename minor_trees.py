class Node:
    def __init__(self, name, parent=None, classes_needed=0, marked=False):
        self.name = name
        self.children = []
        self.node_type = 'AND'
        self.classes_needed = classes_needed
        self.classes_taken = 0
        self.parent = parent
        self.class_list = set()
        self.node_classes = set()
        self.marked = marked
    
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
    
    def get_node_classes(self):
        return self.node_classes

    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        self.children.remove(child_node)
    
    def get_marked(self):
        return self.marked

    def compute_classes_taken_needed(self):
        if self.children:
            winner = []
            self.classes_taken = sum(child.classes_taken for child in self.children)
            self.classes_needed = sum(child.classes_needed for child in self.children)
            winner = [child for child in self.children if child.classes_taken > 0]
        return self.classes_taken, self.classes_needed, winner


class OrNode(Node):
    def __init__(self, name, parent=None, classes_needed=0, marked=False):
        super().__init__(name)
        self.node_type = 'OR'
        self.classes_needed = classes_needed
        self.classes_taken = 0
        self.parent = parent
        self.marked = marked
        self.winner = None
    
    def get_winner(self):
        return self.winner

    def compute_classes_taken_needed(self):
        if self.children:
            max_fraction = 0
            for child in self.children:
                fraction =  child.classes_taken / child.classes_needed
                if fraction >= max_fraction:
                    max_fraction = fraction
                    self.classes_taken = int(max_fraction * child.classes_needed)
                    self.classes_needed = child.classes_needed
                    self.winner = child
        return self.classes_taken, self.classes_needed, self.winner

def create_tree(key, subrequirements):
    if key == 'CLA':
        return create_cla_tree(subrequirements)
    elif key == 'ENV':
        return create_env_tree(subrequirements)
    elif key == 'COS':
        return create_cos_tree(subrequirements)
    elif key == 'FIN':
        return create_fin_tree(subrequirements)
    elif key == 'LIN':
        return create_lin_tree(subrequirements)
    elif key == 'GSS':
        return create_gss_tree(subrequirements)
    elif key == 'AFS':
        return create_afs_tree(subrequirements)
    elif key == 'ASA':
        return create_asa_tree(subrequirements)
    elif key == 'CHI':
        return create_chi_tree(subrequirements)
    elif key == 'CS':
        return create_cs_tree(subrequirements)
    elif key == 'CWR':
        return create_cwr_tree(subrequirements)
    else:
        return None
    
def create_cla_tree(subrequirements, parent=None):
    # Create the root node for CLA minor
    cla = Node('CLA', parent, marked=True)

    # Create the Prerequisites node under CLA
    prerequisites = Node('Prerequisites', parent=cla, classes_needed=subrequirements.get('Prerequisites', 0), marked=True)
    cla.add_child(prerequisites)

    # Create the Tracks (OR node) under CLA
    tracks = OrNode('Tracks', parent=cla, marked=True)

    # Create Classical Track (AND node) under Tracks
    classical = Node('Classics with Focal Point Track', parent=tracks, marked=True)

    # Create Basic Requirements (AND node) under Classical Track
    basic_reqs = Node('Basic Requirements', parent=classical, classes_needed=subrequirements.get('Basic Requirements', 0), marked=True)
    classical.add_child(basic_reqs)

    # Create Subtracks (OR node) under Classical Track
    subtracks = OrNode('Subtracks', parent=classical, marked=True)

    # Create Greek (OR node) under Subtracks
    greek = OrNode('Greek Track', parent=subtracks, marked=True)
    greek_4 = Node('Greek 4 and Relevant 4', parent=greek)
    greek_4.add_child(Node('Greek 4', parent=greek_4, classes_needed=subrequirements.get('Greek 4', 0)))
    greek_4.add_child(Node('Relevant Courses', parent=greek_4, classes_needed=subrequirements.get('Relevant Courses', 0)))
    greek.add_child(greek_4)
    greek.add_child(Node('Greek 5', parent=greek, classes_needed=subrequirements.get('Greek 5', 0)))
    subtracks.add_child(greek)

    # Create Latin (OR node) under Subtracks
    latin = OrNode('Latin Track', parent=subtracks, marked=True)
    latin_4 = Node('Latin 4 and Relevant 4', parent=latin)
    latin_4.add_child(Node('Latin 4', parent=latin_4, classes_needed=subrequirements.get('Latin 4', 0)))
    latin_4.add_child(Node('Relevant Courses', parent=latin_4, classes_needed=subrequirements.get('Relevant Courses', 0)))
    latin.add_child(latin_4)
    latin.add_child(Node('Latin 5', parent=latin, classes_needed=subrequirements.get('Latin 5', 0)))
    subtracks.add_child(latin)

    # Create Medicine (OR node) under Subtracks
    medicine = OrNode('Medicine Track', parent=subtracks,  marked=True)
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
    ancient = Node('Ancient History Track', parent=tracks, marked=True)
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
    env = Node('ENV', parent, marked=True)

    # Create the Foundation node under ENV
    foundation = OrNode('Foundation', parent=env, marked=True)
    env.add_child(foundation)

    # Create the Electives node under ENV
    electives = OrNode('Electives', parent=env, marked=True)
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

def create_cos_tree(subrequirements, parent=None):\
    # Create the root node for COS minor
    cos = Node('COS', parent, marked=True)

    # Create the Elective node under COS
    cos.add_child(Node('Electives', parent=cos, classes_needed=subrequirements.get('Electives', 0), marked=True))

    # Create the Core node under COS
    core = Node('Core', parent=cos, marked=True)

    # Create the Intro node under Core
    intro = OrNode('Intro', parent=core, marked=True)
    intro.add_child(Node('Intro Course', parent=intro, classes_needed=subrequirements.get('Intro Course', 0)))
    intro.add_child(Node('ISC', parent=intro, classes_needed=subrequirements.get('ISC', 0)))
    core.add_child(intro)

    # Create the Core Course node under Core
    core.add_child(Node('Core Course', parent=core, classes_needed=subrequirements.get('Core Course', 0),  marked=True))
    cos.add_child(core)

    return cos

def create_fin_tree(subrequirements, parent=None):
    # Create the root node for FIN minor
    fin = Node('FIN', parent, marked=True)

    # Create Prerequisites node under FIN
    prerequisites = Node('Prerequisites', parent=fin, marked=True)
    prerequisites.add_child(Node('Probability/Stats', 
                                 parent=prerequisites, 
                                 classes_needed=subrequirements.get('Probability/Stats', 0), 
                                 marked=True))
    prerequisites.add_child(Node('Micro',
                                 parent=prerequisites,
                                 classes_needed=subrequirements.get('Micro', 0),
                                 marked=True))
    math = OrNode('Math', parent=prerequisites, marked=True)
    math.add_child(Node('MAT 175',
                        parent=math,
                        classes_needed=subrequirements.get('MAT 175', 0)))
    math.add_child(Node('Advanced Math',
                        parent=math,
                        classes_needed=subrequirements.get('Advanced Math', 0)))
    math.add_child(Node('BSE Math',
                        parent=math,
                        classes_needed=subrequirements.get('BSE Math', 0)))
    math.add_child(Node('EGR',
                        parent=math,
                        classes_needed=subrequirements.get('EGR', 0)))
    
    prerequisites.add_child(math)
    fin.add_child(prerequisites)

    # Add Core under FIN
    fin.add_child(Node('Core', parent=fin, classes_needed=subrequirements.get('Core', 0), marked=True))

    # Add Electives under FIN
    electives = Node('Electives', parent=fin, marked=True)
    electives.add_child(Node('Finanical Applications 1',
                             parent=electives,
                             classes_needed=subrequirements.get('Finanical Applications 1', 0),
                             marked=True))
    
    electives_choices = OrNode('Elective Choices', parent=electives, marked=True)
    electives_choices.add_child(Node('Finanical Applications 2',
                                     parent=electives_choices,
                                     classes_needed=subrequirements.get('Finanical Applications 2', 0)))
    fin_1_gen_1 = Node('Finanical Applications 1 and General Electives 1',
                       parent=electives_choices)
    fin_1_gen_1.add_child(Node('Finanical Applications 1',
                              parent=fin_1_gen_1,
                              classes_needed=subrequirements.get('Finanical Applications 1', 0)))
    fin_1_gen_1.add_child(Node('General Electives 1',
                              parent=fin_1_gen_1,
                              classes_needed=subrequirements.get('General Electives 1', 0)))
    electives_choices.add_child(fin_1_gen_1)
    electives_choices.add_child(Node('General Electives 2',
                                     parent=electives_choices,
                                     classes_needed=subrequirements.get('General Electives 2', 0)))
    electives.add_child(electives_choices)
    fin.add_child(electives)

    return fin

def create_lin_tree(subrequirements, parent=None):
    # Create the root node for LIN minor
    lin = Node('LIN', parent, marked=True)

    # Create Prerequisites node under LIN
    lin.add_child(Node('Prerequisites', 
                                 parent=lin, 
                                 classes_needed=subrequirements.get('Prerequisites', 0),
                                 marked=True))
    
    # Create Coursework Node under LIN
    coursework = Node('Coursework', parent=lin, marked=True)
    coursework.add_child(Node('Core Course',
                                 parent=coursework, 
                                 classes_needed=subrequirements.get('Core Course', 0),
                                 marked=True))
    coursework.add_child(Node('Methods',
                                 parent=coursework, 
                                 classes_needed=subrequirements.get('Methods', 0),
                                 marked=True))
    coursework.add_child(Node('Electives',
                                 parent=coursework, 
                                 classes_needed=subrequirements.get('Electives', 0),
                                 marked=True))
    lin.add_child(coursework)

    return lin

def create_gss_tree(subrequirements, parent=None):
    # Create the root node for GSS minor
    gss = Node('GSS', parent, marked=True)

    # Create the Intro node under GSS
    gss.add_child(Node('Intro', parent=gss, classes_needed=subrequirements.get('Intro', 0), marked=True))

    # Create the Thematic node under GSS
    gss.add_child(Node('Thematic', parent=gss, classes_needed=subrequirements.get('Thematic', 0), marked=True))

    # Create the Elective node under GSS
    gss.add_child( Node('Elective', parent=gss, classes_needed=subrequirements.get('Elective', 0), marked=True))

    return gss

def create_afs_tree(subrequirements, parent=None):

    # Create the root node for AFS minor
    afs = Node('AFS', parent, marked=True)

    # Create Core node under AFS
    afs.add_child(Node('Core', parent=afs, classes_needed=subrequirements.get('Core', 0), marked=True))

    # Create Electives node under AFS
    electives = Node('Electives', parent=afs, marked=True)

    # Create Humanities node under Electives
    electives.add_child(Node('Humanities', parent=electives, classes_needed=subrequirements.get('Humanities', 0), marked=True))

    # Create African Language node under Electives
    electives.add_child(Node('African Language', parent=electives, classes_needed=subrequirements.get('African Language', 0), marked=True))

    # Create Social Sciences node under Electives
    electives.add_child(Node('Social Sciences', parent=electives, classes_needed=subrequirements.get('Social Sciences', 0), marked=True))

    # Create Other Electives node under Electives
    electives.add_child(Node('Other Electives', parent=electives, classes_needed=subrequirements.get('Other Electives', 0), marked=True))

    afs.add_child(electives)

    return afs

def create_asa_tree(subrequirements, parent=None):
    ''' # Subrequirements
    subrequirements = {
        'Core': 1,
        'Electives': 3,
        'Advanced Seminar': 1
    }'''

    # Create the root node for ASA minor
    asa = Node('ASA', parent, marked=True)

    # Create Core node under ASA
    asa.add_child(Node('Core', parent=asa, classes_needed=subrequirements.get('Core', 0), marked=True))

    # Create Electives node under ASA
    asa.add_child(Node('Electives', parent=asa, classes_needed=subrequirements.get('Electives', 0), marked=True))

    # Create Advanced Seminar node under ASA
    asa.add_child(Node('Advanced Seminar', parent=asa, classes_needed=subrequirements.get('Advanced Seminar', 0), marked=True))

    return asa

def create_chi_tree(subrequirements, parent=None):
    ''' subrequirements = {
        'Advanced Language': 2,
        'Other Language': 4,
        'EAS/Cognate': 1
    }'''

    # Create the root node for CHI minor
    chi = Node('CHI', parent, marked=True)

    # create the language node under CHI
    language = Node('Language', parent=chi, marked=True)

    # Create Advanced Language node under CHI
    language.add_child(Node('Advanced Language', parent=language, classes_needed=subrequirements.get('Advanced Language', 0), marked=True))

    # Create Other Language node under CHI
    language.add_child(Node('Other Language', parent=language, classes_needed=subrequirements.get('Other Language', 0), marked=True))

    # Add Language under CHI
    chi.add_child(language)

    # Create EAS/Cognate node under CHI
    chi.add_child(Node('EAS/Cognate', parent=chi, classes_needed=subrequirements.get('EAS/Cognate', 0), marked=True))

    return chi

def create_cs_tree(subrequirements, parent=None):
    # Create the root node for CS minor
    cs = OrNode('CS', parent, marked=True)

    # Create Core 2 and Capstone 3 node under CS
    core_2_capstone_3 = Node('Core 2 and Capstone 3', parent=cs, marked=True)
    core_2_capstone_3.add_child(Node('Core 2', parent=core_2_capstone_3, classes_needed=subrequirements.get('Core 2', 0), marked=True))
    core_2_capstone_3.add_child(Node('Capstone 3', parent=core_2_capstone_3, classes_needed=subrequirements.get('Capstone 3', 0), marked=True))

    cs.add_child(core_2_capstone_3)

    # Create Core 3 and Capstone 2 node under CS
    core_3_capstone_2 = Node('Core 3 and Capstone 2', parent=cs, marked=True)
    core_3_capstone_2.add_child(Node('Core 3', parent=core_3_capstone_2, classes_needed=subrequirements.get('Core 3', 0), marked=True))
    core_3_capstone_2.add_child(Node('Capstone 2', parent=core_3_capstone_2, classes_needed=subrequirements.get('Capstone 2', 0), marked=True))

    cs.add_child(core_3_capstone_2)

    # Create Core 4 and Capstone 1 node under CS
    core_4_capstone_1 = Node('Core 4 and Capstone 1', parent=cs, marked=True)
    core_4_capstone_1.add_child(Node('Core 4', parent=core_4_capstone_1, classes_needed=subrequirements.get('Core 4', 0), marked=True))
    core_4_capstone_1.add_child(Node('Capstone 1', parent=core_4_capstone_1, classes_needed=subrequirements.get('Capstone 1', 0), marked=True))

    cs.add_child(core_4_capstone_1)

    return cs

def create_cwr_tree(subrequirements, parent=None):
    # Create the root node for CWR minor
    cwr = Node('CWR', parent, marked=True)

    # Create CWR Hosted node under CWR
    cwr.add_child(Node('CWR Hosted', parent=cwr, classes_needed=subrequirements.get('CWR Hosted', 0), marked=True))

    # Create CWR Electives node under CWR
    cwr.add_child(Node('CWR Electives', parent=cwr, classes_needed=subrequirements.get('CWR Electives', 0), marked=True))

    return cwr


                         


    


    