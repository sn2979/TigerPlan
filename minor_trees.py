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

def create_dan_tree(subrequirements, parent=None):
    # Create the root node for DAN minor
    dan = Node('DAN', parent, marked=True)

    # Create Studio node under DAN
    dan.add_child(Node('Studio', parent=dan, classes_needed=subrequirements.get('Studio', 0), marked=True))

    # Create Seminar node under DAN
    dan.add_child(Node('Seminar', parent=dan, classes_needed=subrequirements.get('Seminar', 0), marked=True))

    # Create Electives node under DAN
    dan.add_child(Node('Electives', parent=dan, classes_needed=subrequirements.get('Electives', 0), marked=True))

    return dan

def create_eas_tree(subrequirements, parent=None):

    # Create the root node for EAS minor
    eas = Node('EAS', parent, marked=True)

    # Create the Language node under EAS
    language = Node('Language', parent=eas, marked=True)

    # Create Advanced Language node under Language
    language.add_child(Node('Advanced Language', parent=language, classes_needed=subrequirements.get('Advanced Language', 0), marked=True))

    # Create Other Language node under Language
    language.add_child(Node('Other Language', parent=language, classes_needed=subrequirements.get('Other Language', 0), marked=True))

    # Add Language under EAS
    eas.add_child(language)

    # Create Content node under EAS
    content = Node('Content', parent=eas, marked=True)

    # Create 200-Level Content node under Content
    content.add_child(Node('200-Level Content', parent=content, classes_needed=subrequirements.get('200-Level Content', 0), marked=True))

    # Create Other Content node under Content
    content.add_child(Node('Other Content', parent=content, classes_needed=subrequirements.get('Other Content', 0), marked=True))

    # Add Content under EAS
    eas.add_child(content)

    return eas

def create_eng_tree(subrequirements, parent=None):
    '''subrequirements = {
        'Seminars': 2,
        'English Courses': 3
    }'''

    # Create the root node for ENG minor
    eng = Node('ENG', parent, marked=True)
    
    # Create Seminars node under ENG
    eng.add_child(Node('Seminars', parent=eng, classes_needed=subrequirements.get('Seminars', 0), marked=True))

    # Create English Courses node under ENG
    eng.add_child(Node('English Courses', parent=eng, classes_needed=subrequirements.get('English Courses', 0), marked=True))

    return eng

def create_ghp_tree(subrequirements, parent=None):
    # Create the root node for GHP minor
    ghp = Node('GHP', parent, marked=True)

    # Create Prerequisites node under GHP
    prerequisites = Node('Prerequisites', parent=ghp, marked=True)
    foundations = OrNode('Foundations', parent=prerequisites, marked=True)
    foundations.add_child(Node('ISC', parent=foundations, 
                               classes_needed=subrequirements.get('ISC', 0)))
    foundations.add_child(Node('Foundation', parent=foundations, 
                               classes_needed=subrequirements.get('Foundation', 0)))

    prerequisites.add_child(foundations)

    prerequisites.add_child(Node('Statistics', parent=prerequisites, 
                                 classes_needed=subrequirements.get('Statistics', 0), marked=True))

    ghp.add_child(prerequisites)

    # Create Core node under GHP
    ghp.add_child(Node('Core', parent=ghp, classes_needed=subrequirements.get('Core', 0), marked=True))

    # Create Electives node under GHP
    electives = OrNode('Electives', parent=ghp, marked=True)
    electives.add_child(Node('Advanced Electives 4', parent=electives, 
                            classes_needed=subrequirements.get('Advanced Electives 4', 0)))
    
    advanced_2_200_2 = Node('Advanced Electives 2 and 200-Level 2', parent=electives)
    advanced_2_200_2.add_child(Node('Advanced Electives 2', parent=advanced_2_200_2, 
                               classes_needed=subrequirements.get('Advanced Electives 2', 0)))
    advanced_2_200_2.add_child(Node('200-Level Electives 2', parent=advanced_2_200_2,
                                 classes_needed=subrequirements.get('200-Level Electives 2', 0)))
    
    electives.add_child(advanced_2_200_2)

    advanced_3_200_1 = Node('Advanced Electives 3 and 200-Level 1', parent=electives)
    advanced_3_200_1.add_child(Node('Advanced Electives 3', parent=advanced_3_200_1, 
                               classes_needed=subrequirements.get('Advanced Electives 3', 0)))
    advanced_3_200_1.add_child(Node('200-Level Electives 1', parent=advanced_3_200_1,
                                 classes_needed=subrequirements.get('200-Level Electives 1', 0)))
    
    electives.add_child(advanced_3_200_1)

    ghp.add_child(electives)

    return ghp

def create_his_tree(subrequirements, parent=None):
    '''subrequirements = {
        'HIS': 5
    }'''
    history = Node('HIS', parent, marked=True)
    history.add_child(Node('HIS', parent=history, classes_needed=subrequirements.get('HIS', 0), marked=True))

    return history

def create_hls_tree(subrequirements, parent=None):
    '''
    subrequirements = {
        'Gateway Seminar': 1,
        '400-Level Seminar': 1,
        'History, Society Religion': 1,
        'Language, Literature, Philosophy': 1,
        'Visual, Material Culture and Music': 1
    }'''

    # Create the root node for HLS minor
    hls = Node('HLS', parent, marked=True)

    # Create all requirements
    hls.add_child(Node('Gateway Seminar', parent=hls, 
                       classes_needed=subrequirements.get('Gateway Seminar', 0), marked=True))
    hls.add_child(Node('400-Level Seminar', parent=hls, 
                       classes_needed=subrequirements.get('400-Level Seminar', 0), marked=True))
    hls.add_child(Node('History, Society Religion', parent=hls, 
                       classes_needed=subrequirements.get('History, Society Religion', 0), marked=True))
    hls.add_child(Node('Language, Literature, Philosophy', parent=hls, 
                       classes_needed=subrequirements.get('Language, Literature, Philosophy', 0), marked=True))
    hls.add_child(Node('Visual, Material Culture and Music', parent=hls, 
                       classes_needed=subrequirements.get('Visual, Material Culture and Music', 0), marked=True))
    
    return hls

def create_hstm_tree(subrequirements, parent=None):
    # Create the root node for HSTM minor
    hstm = Node('HSTM', parent, marked=True)

    # Create Core node under HSTM
    hstm.add_child(Node('Core', parent=hstm, classes_needed=subrequirements.get('Core', 0), marked=True))
    hstm.add_child(Node('Selected Courses', parent=hstm, classes_needed=subrequirements.get('Selected Courses', 0), marked=True))
    hstm.add_child(Node('HOS/HIS Cognate', parent=hstm, classes_needed=subrequirements.get('HOS/HIS Cognate', 0), marked=True))
    hstm.add_child(Node('History', parent=hstm, classes_needed=subrequirements.get('History', 0), marked=True))

    return hstm

def create_hum_tree(subrequirements, parent=None):
    # Create the root node for HUM minor
    hum = Node('HUM', parent, marked=True)

    # Create 200-Level Humanities node under HUM
    hum.add_child(Node('200-Level Humanities', parent=hum, classes_needed=subrequirements.get('200-Level Humanities', 0), marked=True))

    # create interdisciplinary courses node under HUM
    interdisciplinary = Node('Interdisciplinary Courses', parent=hum, marked=True)

    # create interdisciplinary requirements or node under interdisciplinary
    interdisciplinary_requirements = OrNode('Interdisciplinary Requirements', parent=interdisciplinary, marked=True)

    # create Tradition and Transformation with Global or Comparative Humanities node under interdisciplinary requirements
    tradition_global = Node('Tradition and Transformation with Global or Comparative Humanities', parent=interdisciplinary_requirements)
    tradition_global.add_child(Node('Tradition and Transformation', parent=tradition_global,
                                    classes_needed=subrequirements.get('Tradition and Transformation', 0)))
    tradition_global.add_child(Node('Global or Comparative Humanities', parent=tradition_global, 
                                    classes_needed=subrequirements.get('Global or Comparative Humanities', 0)))

    interdisciplinary_requirements.add_child(tradition_global)

    # create Tradition and Transformation with Engaged or Public Humanities node under interdisciplinary requirements
    tradition_engaged = Node('Tradition and Transformation with Engaged or Public Humanities', parent=interdisciplinary_requirements)
    tradition_engaged.add_child(Node('Tradition and Transformation', parent=tradition_engaged, 
                                     classes_needed=subrequirements.get('Tradition and Transformation', 0)))
    tradition_engaged.add_child(Node('Engaged or Public Humanities', parent=tradition_engaged, 
                                     classes_needed=subrequirements.get('Engaged or Public Humanities', 0)))
    
    interdisciplinary_requirements.add_child(tradition_engaged)

    # create Tradition and Transformation with Humanities and Sciences in Dialogue node under interdisciplinary requirements
    tradition_sciences = Node('Tradition and Transformation with Humanities and Sciences in Dialogue', parent=interdisciplinary_requirements)
    tradition_sciences.add_child(Node('Tradition and Transformation', parent=tradition_sciences,
                                        classes_needed=subrequirements.get('Tradition and Transformation', 0)))
    tradition_sciences.add_child(Node('Humanities and Sciences in Dialogue', parent=tradition_sciences,
                                        classes_needed=subrequirements.get('Humanities and Sciences in Dialogue', 0)))
    
    interdisciplinary_requirements.add_child(tradition_sciences)

    # create Tradition and Transformation with Data and Culture node under interdisciplinary requirements
    tradition_data = Node('Tradition and Transformation with Data and Culture', parent=interdisciplinary_requirements)
    tradition_data.add_child(Node('Tradition and Transformation', parent=tradition_data,
                                    classes_needed=subrequirements.get('Tradition and Transformation', 0)))
    tradition_data.add_child(Node('Data and Culture', parent=tradition_data,
                                    classes_needed=subrequirements.get('Data and Culture', 0)))
    
    interdisciplinary_requirements.add_child(tradition_data)

    # create Global or Comparative Humanities with Engaged or Public Humanities node under interdisciplinary requirements
    global_engaged = Node('Global or Comparative Humanities with Engaged or Public Humanities', parent=interdisciplinary_requirements)
    global_engaged.add_child(Node('Global or Comparative Humanities', parent=global_engaged,
                                    classes_needed=subrequirements.get('Global or Comparative Humanities', 0)))
    global_engaged.add_child(Node('Engaged or Public Humanities', parent=global_engaged,
                                    classes_needed=subrequirements.get('Engaged or Public Humanities', 0)))
    
    interdisciplinary_requirements.add_child(global_engaged)

    # create Global or Comparative Humanities with Humanities and Sciences in Dialogue node under interdisciplinary requirements
    global_sciences = Node('Global or Comparative Humanities with Humanities and Sciences in Dialogue', parent=interdisciplinary_requirements)
    global_sciences.add_child(Node('Global or Comparative Humanities', parent=global_sciences,
                                    classes_needed=subrequirements.get('Global or Comparative Humanities', 0)))
    global_sciences.add_child(Node('Humanities and Sciences in Dialogue', parent=global_sciences,
                                    classes_needed=subrequirements.get('Humanities and Sciences in Dialogue', 0)))
    
    interdisciplinary_requirements.add_child(global_sciences)

    # create Global or Comparative Humanities with Data and Culture node under interdisciplinary requirements
    global_data = Node('Global or Comparative Humanities with Data and Culture', parent=interdisciplinary_requirements)
    global_data.add_child(Node('Global or Comparative Humanities', parent=global_data,
                                classes_needed=subrequirements.get('Global or Comparative Humanities', 0)))
    global_data.add_child(Node('Data and Culture', parent=global_data,
                                classes_needed=subrequirements.get('Data and Culture', 0)))
    
    interdisciplinary_requirements.add_child(global_data)

    # create Engaged or Public Humanities with Humanities and Sciences in Dialogue node under interdisciplinary requirements
    engaged_sciences = Node('Engaged or Public Humanities with Humanities and Sciences in Dialogue', parent=interdisciplinary_requirements)
    engaged_sciences.add_child(Node('Engaged or Public Humanities', parent=engaged_sciences,
                                    classes_needed=subrequirements.get('Engaged or Public Humanities', 0)))
    engaged_sciences.add_child(Node('Humanities and Sciences in Dialogue', parent=engaged_sciences,
                                    classes_needed=subrequirements.get('Humanities and Sciences in Dialogue', 0)))
    
    interdisciplinary_requirements.add_child(engaged_sciences)

    # create Engaged or Public Humanities with Data and Culture node under interdisciplinary requirements
    engaged_data = Node('Engaged or Public Humanities with Data and Culture', parent=interdisciplinary_requirements)
    engaged_data.add_child(Node('Engaged or Public Humanities', parent=engaged_data,
                                    classes_needed=subrequirements.get('Engaged or Public Humanities', 0)))
    engaged_data.add_child(Node('Data and Culture', parent=engaged_data,
                                    classes_needed=subrequirements.get('Data and Culture', 0)))
    
    interdisciplinary_requirements.add_child(engaged_data)

    # create Humanities and Sciences in Dialogue with Data and Culture node under interdisciplinary requirements
    sciences_data = Node('Humanities and Sciences in Dialogue with Data and Culture', parent=interdisciplinary_requirements)
    sciences_data.add_child(Node('Humanities and Sciences in Dialogue', parent=sciences_data,
                                    classes_needed=subrequirements.get('Humanities and Sciences in Dialogue', 0)))
    sciences_data.add_child(Node('Data and Culture', parent=sciences_data,
                                    classes_needed=subrequirements.get('Data and Culture', 0)))
    
    interdisciplinary_requirements.add_child(sciences_data)

    interdisciplinary.add_child(interdisciplinary_requirements)

    # Create Interdisciplinary Electives node under Interdisciplinary Courses
    interdisciplinary.add_child(Node('Interdisciplinary Electives', parent=interdisciplinary,
                                        classes_needed=subrequirements.get('Interdisciplinary Electives', 0), marked=True))
    
    hum.add_child(interdisciplinary)

    return hum

def create_jpn_tree(subrequirements, parent=None):
    # Create the root node for JPN minor
    jpn = Node('JPN', parent, marked=True)

    # Create the Language node under JPN
    language = Node('Language', parent=jpn, marked=True)

    # Create Advanced Language node under Language
    language.add_child(Node('Advanced Language', parent=language, classes_needed=subrequirements.get('Advanced Language', 0), marked=True))

    # Create Other Language node under Language
    language.add_child(Node('Other Language', parent=language, classes_needed=subrequirements.get('Other Language', 0), marked=True))

    # Add Language under JPN
    jpn.add_child(language)

    # Create EAS/Cognate node under JPN
    jpn.add_child(Node('EAS/Cognate', parent=jpn, classes_needed=subrequirements.get('EAS/Cognate', 0), marked=True))

    return jpn

def create_jrn_tree(subrequirements, parent=None):
    # Create the root node for JRN minor
    jrn = Node('JRN', parent, marked=True)

    # Create Gateway node under JRN
    jrn.add_child(Node('Gateway', parent=jrn, classes_needed=subrequirements.get('Gateway', 0), marked=True))

    # Create Advanced node under JRN
    jrn.add_child(Node('Advanced', parent=jrn, classes_needed=subrequirements.get('Advanced', 0), marked=True))

    # Create Electives node under JRN
    jrn.add_child(Node('Electives', parent=jrn, classes_needed=subrequirements.get('Electives', 0), marked=True))

    return jrn

def create_kor_tree(subrequirements, parent=None):
    # Create the root node for KOR minor
    kor = Node('KOR', parent, marked=True)

    # Create the Language node under KOR
    language = Node('Language', parent=kor, marked=True)

    # Create Advanced Language node under Language
    language.add_child(Node('Advanced Language', parent=language, classes_needed=subrequirements.get('Advanced Language', 0), marked=True))

    # Create Other Language node under Language
    language.add_child(Node('Other Language', parent=language, classes_needed=subrequirements.get('Other Language', 0), marked=True))

    # Add Language under KOR
    kor.add_child(language)

    # Create EAS/Cognate node under KOR
    kor.add_child(Node('EAS/Cognate', parent=kor, classes_needed=subrequirements.get('EAS/Cognate', 0), marked=True))

    return kor

def create_lao_tree(subrequirements, parent=None):
    # Create the root node for LAO minor
    lao = Node('LAO', parent, marked=True)

    # Create Required node under LAO
    lao.add_child(Node('Required', parent=lao, classes_needed=subrequirements.get('Required', 0), marked=True))

    # Create Breadth node under LAO
    lao.add_child(Node('Breadth', parent=lao, classes_needed=subrequirements.get('Breadth', 0), marked=True))

    # Create Advanced Seminar node under LAO
    lao.add_child(Node('Advanced Seminar', parent=lao, classes_needed=subrequirements.get('Advanced Seminar', 0), marked=True))

    return lao

def create_med_tree(subrequirements, parent=None):
    # Create the root node for MED minor
    med = Node('MED', parent, marked=True)

    # Create Intro or node under MED
    intro = OrNode('Intro', parent=med, marked=True)
    intro.add_child(Node('Single Course', parent=intro, classes_needed=subrequirements.get('Single Course', 0), marked=True))
    intro.add_child(Node('Humanities Sequence', parent=intro, classes_needed=subrequirements.get('Humanities Sequence', 0), marked=True))
    med.add_child(intro)

    # Create Medieval Topics node under MED
    med.add_child(Node('Medieval Topics', parent=med, classes_needed=subrequirements.get('Medieval Topics', 0), marked=True))

    return med

def create_mpp_tree(subrequirements, parent=None):
    # Create the root node for MPP minor
    mpp = Node('MPP', parent, marked=True)
    
    # Create Core node under MPP
    mpp.add_child(Node('Core', parent=mpp, classes_needed=subrequirements.get('Core', 0), marked=True))

    # Create Materials and Making node under MPP
    mpp.add_child(Node('Materials and Making', parent=mpp, classes_needed=subrequirements.get('Materials and Making', 0), marked=True))

    # Create Culture and Criticism node under MPP
    mpp.add_child(Node('Culture and Criticism', parent=mpp, classes_needed=subrequirements.get('Culture and Criticism', 0), marked=True))

    # Create Elective node under MPP
    mpp.add_child(Node('Elective', parent=mpp, classes_needed=subrequirements.get('Elective', 0), marked=True))

    # Create Departmental node under MPP
    mpp.add_child(Node('Departmental', parent=mpp, classes_needed=subrequirements.get('Departmental', 0), marked=True))

    return mpp

def create_mqe_tree(subrequirements, parent=None):
    # Create the root node for MQE minor
    mqe = Node('MQE', parent, marked=True)

    # create prerequisite node
    prerequisites = Node('Prerequisites', parent=mqe, marked=True)

    # create multivariable calculus node under prerequisites
    prerequisites.add_child(Node('Multivariable Calculus', parent=prerequisites,
                                    classes_needed=subrequirements.get('Multivariable Calculus', 0), marked=True))
    
    # create linear algebra node under prerequisites
    prerequisites.add_child(Node('Linear Algebra', parent=prerequisites,
                                    classes_needed=subrequirements.get('Linear Algebra', 0), marked=True))
    
    # create statistics node under prerequisites
    prerequisites.add_child(Node('Statistics', parent=prerequisites,
                                    classes_needed=subrequirements.get('Statistics', 0), marked=True))
    
    mqe.add_child(prerequisites)

    # create Core Courses under MQE
    mqe.add_child(Node('Core Courses', parent=mqe, classes_needed=subrequirements.get('Core Courses', 0), marked=True))

    # create Electives under MQE
    mqe.add_child(Node('Electives', parent=mqe, classes_needed=subrequirements.get('Electives', 0), marked=True))

    return mqe

def create_mse_tree(subrequirements, parent=None):
    # Create the root node for MSE minor
    mse = Node('MSE', parent, marked=True)

    # create General Physics under MSE
    general_physics = OrNode('General Physics', parent=mse, marked=True)
    general_physics.add_child(Node('103-104 Sequence', parent=general_physics,
                                      classes_needed=subrequirements.get('103-104 Sequence', 0), marked=True))
    general_physics.add_child(Node('105-106 Sequence', parent=general_physics,
                                        classes_needed=subrequirements.get('105-106 Sequence', 0), marked=True))
    
    mse.add_child(general_physics)

    # create General Chemistry under MSE
    general_chemistry = OrNode('General Chemistry', parent=mse, marked=True)
    general_chemistry.add_child(Node('201-202 Sequence', parent=general_chemistry,
                                        classes_needed=subrequirements.get('201-202 Sequence', 0), marked=True))
    general_chemistry.add_child(Node('Chemistry', parent=general_chemistry,
                                        classes_needed=subrequirements.get('Chemistry', 0), marked=True))
    
    mse.add_child(general_chemistry)

    # create Thermodynamics under MSE
    mse.add_child(Node('Thermodynamics', parent=mse,
                        classes_needed=subrequirements.get('Thermodynamics', 0), marked=True))
    
    # create Materials under MSE
    mse.add_child(Node('Materials', parent=mse,
                        classes_needed=subrequirements.get('Materials', 0), marked=True))
    
    # create Mathematics under MSE
    mse.add_child(Node('Mathematics', parent=mse,
                        classes_needed=subrequirements.get('Mathematics', 0), marked=True))
    
    # create Electives under MSE
    mse.add_child(Node('Electives', parent=mse,
                        classes_needed=subrequirements.get('Electives', 0), marked=True))
    
    # create Experimental Methods under MSE
    mse.add_child(Node('Experimental Methods', parent=mse,
                        classes_needed=subrequirements.get('Experimental Methods', 0), marked=True))
    
    return mse

def create_mus_tree(subrequirements, parent=None):
    # Create the root node for MPP minor
    mus = Node('MUS', parent, marked=True)
    
    # Create Core node under MPP
    mus.add_child(Node('Core', parent=mus, classes_needed=subrequirements.get('Core', 0), marked=True))

    # Create Materials and Making node under MPP
    mus.add_child(Node('Materials and Making', parent=mus, classes_needed=subrequirements.get('Materials and Making', 0), marked=True))

    # Create Culture and Criticism node under MPP
    mus.add_child(Node('Culture and Criticism', parent=mus, classes_needed=subrequirements.get('Culture and Criticism', 0), marked=True))

    # Create Music Electives node under MPP
    mus.add_child(Node('Music Electives', parent=mus, classes_needed=subrequirements.get('Music Electives', 0), marked=True))

    return mus

def create_neu_tree(subrequirements, parent=None):
    # Create the root node for NEU minor
    neu = Node('NEU', parent, marked=True)

    # Create core node under NEU
    core = Node('Core', parent=neu, marked=True)
    core.add_child(Node('Fundamentals', parent=core, classes_needed=subrequirements.get('Fundamentals', 0), marked=True))
    core.add_child(Node('Intro', parent=core, classes_needed=subrequirements.get('Intro', 0), marked=True))
    neu.add_child(core)

    # add electives node under NEU
    electives = Node('Electives', parent=neu, marked=True)

    # add Other elective node under electives
    electives.add_child(Node('Other Electives', parent=electives, classes_needed=subrequirements.get('Other Electives', 0), marked=True))
    
    # add tracks or node under electives
    tracks = OrNode('Tracks', parent=electives, marked=True)

    # add Molecular/Cellular/Disease with Circuits & Systems with  Neural Computation node under tracks
    mcd_cs_nc = Node('Molecular/Cellular/Disease with Circuits & Systems with Neural Computation', parent=tracks)
    mcd_cs_nc.add_child(Node('Molecular/Cellular/Disease', parent=mcd_cs_nc, 
                             classes_needed=subrequirements.get('Molecular/Cellular/Disease', 0)))
    mcd_cs_nc.add_child(Node('Circuits & Systems', parent=mcd_cs_nc,
                                classes_needed=subrequirements.get('Circuits & Systems', 0)))
    mcd_cs_nc.add_child(Node('Neural Computation', parent=mcd_cs_nc,
                                classes_needed=subrequirements.get('Neural Computation', 0)))
    
    tracks.add_child(mcd_cs_nc)

    # add Molecular/Cellular/Disease with Circuits & Systems with Cognitive & Social Neuroscience node under tracks
    mcd_cs_csn = Node('Molecular/Cellular/Disease with Circuits & Systems with Cognitive & Social Neuroscience', parent=tracks)
    mcd_cs_csn.add_child(Node('Molecular/Cellular/Disease', parent=mcd_cs_csn,
                                classes_needed=subrequirements.get('Molecular/Cellular/Disease', 0)))
    mcd_cs_csn.add_child(Node('Circuits & Systems', parent=mcd_cs_csn,
                                classes_needed=subrequirements.get('Circuits & Systems', 0)))
    mcd_cs_csn.add_child(Node('Cognitive & Social Neuroscience', parent=mcd_cs_csn,
                                classes_needed=subrequirements.get('Cognitive & Social Neuroscience', 0)))
    
    tracks.add_child(mcd_cs_csn)

    # add Molecular/Cellular/Disease with Neural Computation with Cognitive & Social Neuroscience node under tracks
    mcd_nc_csn = Node('Molecular/Cellular/Disease with Neural Computation with Cognitive & Social Neuroscience', parent=tracks)
    mcd_nc_csn.add_child(Node('Molecular/Cellular/Disease', parent=mcd_nc_csn,
                                classes_needed=subrequirements.get('Molecular/Cellular/Disease', 0)))
    mcd_nc_csn.add_child(Node('Neural Computation', parent=mcd_nc_csn,
                                classes_needed=subrequirements.get('Neural Computation', 0)))
    mcd_nc_csn.add_child(Node('Cognitive & Social Neuroscience', parent=mcd_nc_csn,
                                classes_needed=subrequirements.get('Cognitive & Social Neuroscience', 0)))
    
    tracks.add_child(mcd_nc_csn)

    # add Circuits & Systems with Neural Computation with Cognitive & Social Neuroscience node under tracks
    cs_nc_csn = Node('Circuits & Systems with Neural Computation with Cognitive & Social Neuroscience', parent=tracks)
    cs_nc_csn.add_child(Node('Circuits & Systems', parent=cs_nc_csn,
                                classes_needed=subrequirements.get('Circuits & Systems', 0)))
    cs_nc_csn.add_child(Node('Neural Computation', parent=cs_nc_csn,
                                classes_needed=subrequirements.get('Neural Computation', 0)))
    cs_nc_csn.add_child(Node('Cognitive & Social Neuroscience', parent=cs_nc_csn,
                                classes_needed=subrequirements.get('Cognitive & Social Neuroscience', 0)))
    
    tracks.add_child(cs_nc_csn)
    electives.add_child(tracks)
    neu.add_child(electives)

    return neu

def create_phi_tree(subrequirements, parent=None):
    # Create the root node for PHI minor
    phi = Node('PHI', parent, marked=True)

    # Create Prerequisite node under PHI
    phi.add_child(Node('Prerequisite', parent=phi, classes_needed=subrequirements.get('Prerequisite', 0), marked=True))

    # create Core node under PHI
    core = OrNode('Core', parent=phi, marked=True)

    # create Advanced 5 node under Core
    core.add_child(Node('Advanced 5', parent=core, classes_needed=subrequirements.get('Advanced 5', 0)))

    # create 200-Level 1 and Advanced 4 node under Core
    advanced_4_200_1 = Node('Advanced 4 and 200-Level 1', parent=core)
    advanced_4_200_1.add_child(Node('Advanced 4', parent=advanced_4_200_1,
                                    classes_needed=subrequirements.get('Advanced 4', 0)))
    advanced_4_200_1.add_child(Node('200-Level 1', parent=advanced_4_200_1,
                                    classes_needed=subrequirements.get('200-Level 1', 0)))
    
    core.add_child(advanced_4_200_1)

    # create 200-Level 2 and Advanced 3 node under Core
    advanced_3_200_2 = Node('Advanced 3 and 200-Level 2', parent=core)
    advanced_3_200_2.add_child(Node('Advanced 3', parent=advanced_3_200_2,
                                    classes_needed=subrequirements.get('Advanced 3', 0)))
    advanced_3_200_2.add_child(Node('200-Level 2', parent=advanced_3_200_2,
                                    classes_needed=subrequirements.get('200-Level 2', 0)))
    
    core.add_child(advanced_3_200_2)

    phi.add_child(core)

    return phi

def create_res_tree(subrequirements, parent=None):
    # Create the root node for RES minor
    res = Node('RES', parent, marked=True)

    # Create History and Social Sciences node under RES
    res.add_child(Node('History and Social Sciences', parent=res, 
                       classes_needed=subrequirements.get('History and Social Sciences', 0), marked=True))
    
    # Create Literature, Arts and Culture node under RES
    res.add_child(Node('Literature, Arts and Culture', parent=res,
                          classes_needed=subrequirements.get('Literature, Arts and Culture', 0), marked=True))
    
    # create language or node under RES
    language = OrNode('Language', parent=res, marked=True)

    # create BCS node under language
    language.add_child(Node('BCS', parent=language,
                            classes_needed=subrequirements.get('BCS', 0), marked=True))
    language.add_child(Node('CZE', parent=language,
                            classes_needed=subrequirements.get('CZE', 0), marked=True))
    language.add_child(Node('PLS', parent=language,
                            classes_needed=subrequirements.get('PLS', 0), marked=True))
    language.add_child(Node('RUS', parent=language,
                            classes_needed=subrequirements.get('RUS', 0), marked=True))
    language.add_child(Node('TUR', parent=language,
                            classes_needed=subrequirements.get('TUR', 0), marked=True))
    language.add_child(Node('UKR', parent=language,
                            classes_needed=subrequirements.get('UKR', 0), marked=True))
    
    res.add_child(language)

    return res

def create_sas_tree(subrequirements, parent=None):
    # Create the root node for SAS minor
    sas = Node('SAS', parent, marked=True)

    # Create Core node under SAS
    sas.add_child(Node('Core', parent=sas, classes_needed=subrequirements.get('Core', 0), marked=True))

    # Create Language node under SAS
    sas.add_child(Node('Language', parent=sas, classes_needed=subrequirements.get('Language', 0), marked=True))

    # Create Electives node under SAS
    sas.add_child(Node('Electives', parent=sas, classes_needed=subrequirements.get('Electives', 0), marked=True))

    return sas

def create_sla_tree(subrequirements, parent=None):
    # Create the root node for SLA minor
    sla = Node('SLA', parent, marked=True)

    sla.add_child(Node('First Requirement', parent=sla, 
                       classes_needed=subrequirements.get('First Requirement', 0), marked=True))
    sla.add_child(Node('Second Requirement', parent=sla,
                          classes_needed=subrequirements.get('Second Requirement', 0), marked=True))
    sla.add_child(Node('Departmentals', parent=sla,
                            classes_needed=subrequirements.get('Departmentals', 0), marked=True))

    return sla

def create_sml_tree(subrequirements, parent=None):
    # Create the root node for SML minor
    sml = Node('SML', parent, marked=True)
    sml.add_child(Node('Statistics', parent=sml, classes_needed=subrequirements.get('Statistics', 0), marked=True))
    sml.add_child(Node('Machine Learning', parent=sml, classes_needed=subrequirements.get('Machine Learning', 0), marked=True))
    sml.add_child(Node('Electives', parent=sml, classes_needed=subrequirements.get('Electives', 0), marked=True))

    return sml

def create_tmt_tree(subrequirements, parent=None):
    # Create the root node for TMT minor
    tmt = Node('TMT', parent, marked=True)
    tmt.add_child(Node('Introduction', parent=tmt, classes_needed=subrequirements.get('Introduction', 0), marked=True))
    tmt.add_child(Node('Additional Courses', parent=tmt, classes_needed=subrequirements.get('Additional Courses', 0), marked=True))
    tmt.add_child(Node('Electives', parent=tmt, classes_needed=subrequirements.get('Electives', 0), marked=True))
    tmt.add_child(Node('Dramaturgical', parent=tmt, classes_needed=subrequirements.get('Dramaturgical', 0), marked=True))

    return tmt

def create_tra_tree(subrequirements, parent=None):
    # Create the root node for TRA minor
    tra = Node('TRA', parent, marked=True)

    # Create Core node under TRA
    tra.add_child(Node('Core', parent=tra, classes_needed=subrequirements.get('Core', 0), marked=True))

    # create Additional Courses node under TRA
    additional_courses = Node('Additional Courses', parent=tra, marked=True)
    additional_courses.add_child(Node('Other Additional Course', parent=additional_courses,
                                      classes_needed=subrequirements.get('Other Additional Course', 0), marked=True))
    
    # Tracks or node under Additional Courses
    tracks = OrNode('Tracks', parent=additional_courses, marked=True)

    # created a Upper-Level Course with Cross-listed by TRA node under Tracks
    upper_cross = Node('Upper-Level Course with Cross-listed by TRA', parent=tracks)
    upper_cross.add_child(Node('Upper-Level Course', parent=upper_cross,
                                 classes_needed=subrequirements.get('Upper-Level Course', 0)))
    upper_cross.add_child(Node('Cross-listed by TRA', parent=upper_cross,
                                    classes_needed=subrequirements.get('Cross-listed by TRA', 0)))
    
    tracks.add_child(upper_cross)

    # create Upper-Level Course with Understanding of Translation node under Tracks
    upper_understanding = Node('Upper-Level Course with Understanding of Translation', parent=tracks)
    upper_understanding.add_child(Node('Upper-Level Course', parent=upper_understanding,
                                        classes_needed=subrequirements.get('Upper-Level Course', 0)))
    upper_understanding.add_child(Node('Understanding of Translation', parent=upper_understanding,
                                        classes_needed=subrequirements.get('Understanding of Translation', 0)))
    
    tracks.add_child(upper_understanding)

    # add Cross-listed by TRA with Understanding of Translation node under Tracks
    cross_understanding = Node('Cross-listed by TRA with Understanding of Translation', parent=tracks)
    cross_understanding.add_child(Node('Cross-listed by TRA', parent=cross_understanding,
                                        classes_needed=subrequirements.get('Cross-listed by TRA', 0)))
    cross_understanding.add_child(Node('Understanding of Translation', parent=cross_understanding,
                                        classes_needed=subrequirements.get('Understanding of Translation', 0)))
    
    tracks.add_child(cross_understanding)

    additional_courses.add_child(tracks)
    tra.add_child(additional_courses)

    return tra

def create_vis_tree(subrequirements, parent=None):
    vis = Node('VIS', parent, marked=True)
    vis.add_child(Node('Studio', parent=vis, classes_needed=subrequirements.get('Studio', 0)))
    vis.add_child(Node('Artist and Studio', parent=vis, classes_needed=subrequirements.get('Artist and Studio', 0)))
    vis.add_child(Node('Exhibition Issues and Methods', parent=vis,
                        classes_needed=subrequirements.get('Exhibition Issues and Methods', 0)))
    vis.add_child(Node('Art and Archaeology', parent=vis, 
                        classes_needed=subrequirements.get('Art and Archaeology', 0)))
    vis.add_child(Node('Elective', parent=vis, classes_needed=subrequirements.get('Elective', 0)))

    return vis

def create_vpl_tree(subrequirements, parent=None):
    # Create the root node for VPL minor
    vpl = Node('VPL', parent, marked=True)
    vpl.add_child(Node('Intro', parent=vpl, classes_needed=subrequirements.get('Intro', 0), marked=True))
    vpl.add_child(Node('Political Theory', parent=vpl, classes_needed=subrequirements.get('Political Theory', 0), marked=True))
    vpl.add_child(Node('Seminar', parent=vpl, classes_needed=subrequirements.get('Seminar', 0), marked=True))
    vpl.add_child(Node('Thematic Courses', parent=vpl, classes_needed=subrequirements.get('Thematic Courses', 0), marked=True))

    return vpl

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
    elif key == 'DAN':
        return create_dan_tree(subrequirements)
    elif key == 'EAS':
        return create_eas_tree(subrequirements)
    elif key == 'ENG':
        return create_eng_tree(subrequirements)
    elif key == 'GHP':
        return create_ghp_tree(subrequirements)
    elif key == 'HIS':
        return create_his_tree(subrequirements)
    elif key == 'HLS':
        return create_hls_tree(subrequirements)
    elif key == 'HSTM':
        return create_hstm_tree(subrequirements)
    elif key == 'HUM':
        return create_hum_tree(subrequirements)
    elif key == 'JPN':
        return create_jpn_tree(subrequirements)
    elif key == 'JRN':
        return create_jrn_tree(subrequirements)
    elif key == 'KOR':
        return create_kor_tree(subrequirements)
    elif key == 'LAO':
        return create_lao_tree(subrequirements)
    elif key == 'MED':
        return create_med_tree(subrequirements)
    elif key == 'MPP':
        return create_mpp_tree(subrequirements)
    elif key == 'MQE':
        return create_mqe_tree(subrequirements)
    elif key == 'MSE':
        return create_mse_tree(subrequirements)
    elif key == 'MUS':
        return create_mus_tree(subrequirements)
    elif key == 'NEU':
        return create_neu_tree(subrequirements)
    elif key == 'PHI':
        return create_phi_tree(subrequirements)
    elif key == 'RES':
        return create_res_tree(subrequirements)
    elif key == 'SAS':
        return create_sas_tree(subrequirements)
    elif key == 'SLA':
        return create_sla_tree(subrequirements)
    elif key == 'SML':
        return create_sml_tree(subrequirements)
    elif key == 'TMT':
        return create_tmt_tree(subrequirements)
    elif key == 'TRA':
        return create_tra_tree(subrequirements)
    elif key == 'VIS':
        return create_vis_tree(subrequirements)
    elif key == 'VPL':
        return create_vpl_tree(subrequirements)
    else:
        return None
    
    
    

