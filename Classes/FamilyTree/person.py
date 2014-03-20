# Need to put a graphical back end on this at some point. but for
class Person(object):
    """
    Represents a node in a family tree.

    Members:
    name -- The name of the individual
    Children -- List of Person objects that represent the descendents.
    birthyear -- Self explainatory.
    deathyear -- Self explainatory.
    """
    def __init__(self, name, children, birthyear, deathyear):
        """
        Main constructor method.
        """
        self.name = name
        if children is not None:
            for child in children:
                if not(isinstance(child, Person) or child is None):
                    raise TypeError("Not a Person or None")
        self.children = children
        self.birthyear = birthyear
        self.deathyear = deathyear
        print(self.name)
        print("Children:" + str(self.children))
        print("birthyear:" + str(self.birthyear))
        print("deathyear:" + str(self.deathyear))
        print("\n")

    def traverseTree(self):
        """
        Traverses the person's generational tree and returns a list of
        references to all descendents.
        """
        tree = []
        tree.append(self)
        if self.children is not None:
            for child in self.children:
                tree.extend(child.traverseTree())
        return tree


def printTree(Person):
    """
    Traverses through all descendents of this individual by returning
    all children until the most recent generation.
    """
    if not hasattr(printTree, "depth"):
        printTree.depth = 0  # How many generations into the tree we are
    else:
        printTree.depth += 1
    print(Person.name + " " + str(printTree.depth))
    #   Format the tree
    if Person.children is not None:
        for child in Person.children:
            print('\t' * printTree.depth + '|___', end="")
            printTree(child)
    printTree.depth -= 1


if __name__ == '__main__':  # Our test cases
    bob = Person("Bob Lawrence", None, 2000, None)
    cindy = Person("Cindy Lawrence", None, 2001, None)
    katie = Person("Katie Lawrence", None, 2022, None)
    martin = Person("Martin Lawrence", [katie], 2002, None)
    loreli = Person("Loreli Lawrence", [bob, martin, cindy], 1975, None)
    tree = loreli.traverseTree()
    for entry in tree:
        print(entry.name)
    print()
    printTree(loreli)
