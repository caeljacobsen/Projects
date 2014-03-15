class Person(object):
    """
    Represents a node in a family tree.

    Members:
    name -- The name of the individual
    Children -- Collection of Person objects that represent the descendents.
    birthyear -- Self explainatory.
    deathyear -- Self explainatory.
    """
    def __init__(self, name, children, birthyear, deathyear):
        """
        Main constructor method.
        """
        self.name = name
        if len(children) > 0:
            for child in children:
                if not(isinstance(child, Person) or child is None):
                    raise TypeError("Not a Person or None")
        self.children = children
        self.birthyear = birthyear
        self.deathyear = deathyear

    def traverse(self):
        """
        Traverses through all descendents of this individual by returning
        all children until the most recent generation.
        """
        if len(self.children) == 0:
            return None
        for child in self.children:
            print("----" + child.traverse())
