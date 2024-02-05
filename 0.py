Quiz questions
Question #0
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

b = Base()
print(b.id)

0


1


None

Question #1
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

for i in range(3):
    b = Base()
print(b.id)

3


4


None


2

Question #2
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        self.id = 89

u = User()
print(u.id)

90


1


89

Question #3
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

u = User()
print(u.id)

0


1


None


2

Question #4
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)

1


2


0


3

Question #5
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

for i in range(4):
    u = User()
print(u.id)

3


5


4


None

Question #6
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id += 99

u = User()
print(u.id)

100


1


99

Question #7
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()

u = User()
print(u.id)

0


1


None


2

Question #8
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        self.id = 89
        super().__init__()

u = User()
print(u.id)

90


1


89

Question #9
What do these lines print?

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id = 89

u = User()
print(u.id)

90


1


89

# Answers to quiz questions

# Question #0: The answer is 1
# Question #1: The answer is 3
# Question #2: The answer is 89
# Question #3: The answer is 1
# Question #4: The answer is 2
# Question #5: The answer is 4
# Question #6: The answer is 100
# Question #7: The answer is 1
# Question #8: The answer is 1
# Question #9: The answer is 89
