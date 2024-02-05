#!/usr/bin/python3
"""
MyList class inherits from list
"""


class MyList(list):
    """MyList initializes as empty list object"""
    def __init__(self):
        """initializes the MyList object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted MyList"""
        print(sorted(self))
