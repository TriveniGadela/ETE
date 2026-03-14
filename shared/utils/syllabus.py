"""
Syllabus and curriculum topics for each academic level
"""

SYLLABUS = {
    'elementary': {
        'Mathematics': [
            'Basic Addition and Subtraction',
            'Multiplication Tables',
            'Division Basics',
            'Fractions Introduction',
            'Shapes and Geometry',
            'Measurement (Length, Weight, Time)',
            'Money and Currency',
            'Simple Word Problems'
        ],
        'Science': [
            'Plants and Animals',
            'Human Body Basics',
            'Weather and Seasons',
            'Solar System',
            'Water Cycle',
            'States of Matter (Solid, Liquid, Gas)',
            'Simple Machines',
            'Healthy Habits'
        ],
        'English': [
            'Alphabet and Phonics',
            'Reading Comprehension',
            'Basic Grammar',
            'Sentence Formation',
            'Story Writing',
            'Vocabulary Building',
            'Punctuation Marks'
        ]
    },
    'middle_school': {
        'Mathematics': [
            'Integers and Rational Numbers',
            'Algebraic Expressions',
            'Linear Equations',
            'Geometry (Angles, Triangles, Circles)',
            'Perimeter and Area',
            'Data Handling and Statistics',
            'Probability Basics',
            'Exponents and Powers'
        ],
        'Science': [
            'Cell Structure and Functions',
            'Photosynthesis',
            'Force and Motion',
            'Electricity and Circuits',
            'Chemical Reactions',
            'Acids, Bases and Salts',
            'Light and Reflection',
            'Sound and Waves'
        ],
        'Social Studies': [
            'Ancient Civilizations',
            'Geography Basics',
            'Government and Civics',
            'World History',
            'Maps and Globes'
        ]
    },
    'high_school': {
        'Mathematics': [
            'Quadratic Equations',
            'Trigonometry',
            'Coordinate Geometry',
            'Calculus Basics',
            'Probability and Statistics',
            'Matrices and Determinants',
            'Sequences and Series',
            'Complex Numbers'
        ],
        'Physics': [
            'Newton\'s Laws of Motion',
            'Work, Energy and Power',
            'Gravitation',
            'Thermodynamics',
            'Waves and Optics',
            'Electromagnetism',
            'Modern Physics',
            'Atomic Structure'
        ],
        'Chemistry': [
            'Atomic Structure',
            'Chemical Bonding',
            'Periodic Table',
            'Chemical Reactions and Equations',
            'Acids, Bases and Salts',
            'Organic Chemistry Basics',
            'Electrochemistry',
            'Thermochemistry'
        ],
        'Biology': [
            'Cell Biology',
            'Genetics and Evolution',
            'Human Physiology',
            'Plant Physiology',
            'Ecology and Environment',
            'Biotechnology',
            'Reproduction',
            'Biodiversity'
        ]
    },
    'undergraduate': {
        'Computer Science': [
            'Data Structures and Algorithms',
            'Object-Oriented Programming',
            'Database Management Systems',
            'Operating Systems',
            'Computer Networks',
            'Software Engineering',
            'Web Development',
            'Artificial Intelligence Basics'
        ],
        'Mathematics': [
            'Linear Algebra',
            'Differential Equations',
            'Real Analysis',
            'Abstract Algebra',
            'Discrete Mathematics',
            'Numerical Methods',
            'Probability Theory',
            'Mathematical Statistics'
        ],
        'Engineering': [
            'Engineering Mechanics',
            'Thermodynamics',
            'Fluid Mechanics',
            'Circuit Theory',
            'Control Systems',
            'Digital Electronics',
            'Signals and Systems',
            'Engineering Drawing'
        ]
    },
    'graduate': {
        'Research Methods': [
            'Research Methodology',
            'Statistical Analysis',
            'Literature Review Techniques',
            'Thesis Writing',
            'Data Collection Methods',
            'Qualitative Research',
            'Quantitative Research',
            'Research Ethics'
        ],
        'Advanced Topics': [
            'Machine Learning',
            'Deep Learning',
            'Natural Language Processing',
            'Computer Vision',
            'Advanced Algorithms',
            'Distributed Systems',
            'Cloud Computing',
            'Blockchain Technology'
        ],
        'Specialized Studies': [
            'Advanced Mathematics',
            'Quantum Computing',
            'Bioinformatics',
            'Computational Biology',
            'Advanced Physics',
            'Nanotechnology'
        ]
    }
}

def get_syllabus_for_level(academic_level):
    """Get syllabus topics for a specific academic level"""
    return SYLLABUS.get(academic_level, {})

def get_all_topics_for_level(academic_level):
    """Get all topics as a flat list for a specific academic level"""
    syllabus = get_syllabus_for_level(academic_level)
    all_topics = []
    for subject, topics in syllabus.items():
        all_topics.extend(topics)
    return all_topics

def get_random_suggestions(academic_level, count=5):
    """Get random topic suggestions for a specific academic level"""
    import random
    all_topics = get_all_topics_for_level(academic_level)
    if len(all_topics) <= count:
        return all_topics
    return random.sample(all_topics, count)
