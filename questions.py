class Node:
    def __init__(self, question, answer, choices=None):
        self.question = question
        self.answer = answer
        self.choices = choices
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, question, answer, choices=None):
        new_node = Node(question, answer, choices)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def to_list(self):
        arr = [] # meaning array
        cur = self.head # meaning current
        while cur:
            arr.append((cur.question, cur.answer, cur.choices))
            cur = cur.next
        return arr

# EASY QUESTIONS (True/False)
easy_dict = {
    "The Sun is a star.": True,
    "Humans can breathe underwater without equipment.": False,
    "Dogs are mammals.": True,
    "Ice melts into water.": True,
    "The moon produces its own light.": False,
    "Fish live on land.": False,
    "Plants need sunlight to grow.": True,
    "Earth is the third planet from the Sun.": True,
    "Clouds are made of water vapor.": True,
    "Birds have feathers.": True,
    "A year has 365 days.": True,
    "Fire is cold.": False,
    "Water boils at 100°C.": True,
    "The sky is naturally green.": False,
    "Spiders have eight legs.": True,
    "Bats are birds.": False,
    "Humans have two eyes.": True,
    "Cows can fly.": False,
    "The Pacific Ocean is the largest ocean.": True,
    "Rocks can breathe.": False,
    "Apples grow on trees.": True,
    "Lightning is electricity.": True,
    "Snakes have legs.": False,
    "A triangle has three sides.": True,
    "Gold is a metal.": True,
    "The Earth is flat.": False,
    "Milk is a liquid.": True,
    "Paper is made from trees.": True,
    "The brain controls the body.": True,
    "Sand is made of tiny rocks.": True
}

# MEDIUM QUESTIONS (Multiple Choice)
medium_list = LinkedList()
medium_data = [
    ("What is the capital of Japan?", "B) Tokyo",
     ["A) Seoul", "B) Tokyo", "C) Beijing", "D) Bangkok"]),
    ("Which gas do plants absorb?", "B) Carbon Dioxide",
     ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"]),
        ("Who wrote 'Romeo and Juliet'?", "B) William Shakespeare",
     ["A) Dickens", "B) William Shakespeare", "C) Poe", "D) Tolkien"]),
    ("Which planet is known as the Red Planet?", "C) Mars",
     ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"]),
    ("What is the largest mammal?", "B) Blue Whale",
     ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Rhino"]),
    ("Which organ pumps blood?", "C) Heart",
     ["A) Brain", "B) Lungs", "C) Heart", "D) Liver"]),
    ("What do bees produce?", "B) Honey",
     ["A) Milk", "B) Honey", "C) Oil", "D) Water"]),
    ("How many continents are there?", "C) 7",
     ["A) 5", "B) 6", "C) 7", "D) 8"]),
    ("What is H2O?", "D) Water",
     ["A) Oxygen", "B) Hydrogen", "C) Salt", "D) Water"]),
    ("Which one is a primary color?", "C) Red",
     ["A) Pink", "B) Purple", "C) Red", "D) Brown"]),
    ("Who painted the Mona Lisa?", "C) Leonardo da Vinci",
     ["A) Van Gogh", "B) Picasso", "C) Leonardo da Vinci", "D) Rembrandt"]),
    ("Which planet has rings?", "D) Saturn",
     ["A) Earth", "B) Mercury", "C) Jupiter", "D) Saturn"]),
    ("Which animal lays eggs?", "C) Duck",
     ["A) Dog", "B) Cat", "C) Duck", "D) Whale"]),
    ("What is the boiling point of water?", "C) 100°C",
     ["A) 50°C", "B) 80°C", "C) 100°C", "D) 120°C"]),
    ("What is the largest desert?", "A) Sahara",
     ["A) Sahara", "B) Gobi", "C) Arctic", "D) Kalahari"]),
    ("A triangle has how many sides?", "B) 3",
     ["A) 2", "B) 3", "C) 4", "D) 5"]),
    ("What shape is a stop sign?", "B) Octagon",
     ["A) Hexagon", "B) Octagon", "C) Square", "D) Circle"]),
    ("Which metal is liquid at room temperature?", "C) Mercury",
     ["A) Gold", "B) Iron", "C) Mercury", "D) Copper"]),
    ("Which country invented pizza?", "B) Italy",
     ["A) France", "B) Italy", "C) USA", "D) Mexico"]),
    ("Which sense is associated with the nose?", "B) Smell",
     ["A) Touch", "B) Smell", "C) Taste", "D) Sight"]),
    ("What gas do humans inhale?", "C) Oxygen",
     ["A) Carbon dioxide", "B) Nitrogen", "C) Oxygen", "D) Helium"]),
    ("What is Earth’s only natural satellite?", "A) Moon",
     ["A) Moon", "B) Titan", "C) Deimos", "D) Europa"]),
    ("How many legs does a spider have?", "B) 8",
     ["A) 6", "B) 8", "C) 10", "D) 12"]),
    ("Which is the fastest land animal?", "C) Cheetah",
     ["A) Lion", "B) Tiger", "C) Cheetah", "D) Leopard"]),
    ("What currency is used in Japan?", "B) Yen",
     ["A) Dollar", "B) Yen", "C) Peso", "D) Won"]),
    ("What planet is closest to the Sun?", "C) Mercury",
     ["A) Earth", "B) Mars", "C) Mercury", "D) Venus"]),
    ("How many bones are in the human body?", "C) 206",
     ["A) 150", "B) 170", "C) 206", "D) 250"]),
    ("Which continent is Egypt in?", "B) Africa",
     ["A) Asia", "B) Africa", "C) Europe", "D) South America"]),
    ("What gas makes balloons float?", "B) Helium",
     ["A) Oxygen", "B) Helium", "C) Hydrogen", "D) Carbon dioxide"]),
    ("Which animal is known as the King of the Jungle?", "B) Lion",
     ["A) Tiger", "B) Lion", "C) Wolf", "D) Bear"])
]
for q, a, c in medium_data:
    medium_list.add(q, a, c)

# HARD QUESTIONS
hard_list = LinkedList()
hard_data = [
    ("What gas do plants release during photosynthesis?", "Oxygen"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("What do we call molten rock beneath the Earth's surface?", "Magma"),
        ("What planet is known as the Morning Star?", "Venus"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What part of the cell contains DNA?", "Nucleus"),
    ("What is the freezing point of water in Fahrenheit?", "32"),
    ("What force keeps us on the ground?", "Gravity"),
    ("What is the hardest natural substance?", "Diamond"),
    ("What is the largest planet?", "Jupiter"),
    ("What is the smallest unit of life?", "Cell"),
    ("What organ filters blood?", "Kidney"),
    ("What is the nearest star to Earth?", "Sun"),
    ("What do plants need for photosynthesis?", "Sunlight"),
    ("What organ helps us breathe?", "Lungs"),
    ("What is the process of water turning to gas called?", "Evaporation"),
    ("What is the longest river?", "Nile river"),
    ("What mineral makes bones strong?", "Calcium"),
    ("What natural satellite orbits Earth?", "Moon"),
    ("What do bees collect from flowers?", "Nectar"),
    ("What gas do humans exhale?", "Carbon dioxide"),
    ("What is the largest internal organ?", "Liver"),
    ("What is the study of living things?", "Biology"),
    ("What galaxy do we live in?", "Milky Way"),
    ("What is the biggest ocean?", "Pacific Ocean"),
    ("What device measures temperature?", "Thermometer"),
    ("What is the chemical symbol for water?", "H2O"),
    ("What organ pumps blood?", "Heart"),
    ("What is the study of fossils called?", "Paleontology"),
    ("What is Earth’s layer beneath the crust?", "Mantle")
]
for q, a in hard_data:
    hard_list.add(q, a)