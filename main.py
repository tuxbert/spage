'''
Welcome to SPAGE (SPAGE Python Adventure Game Engine)

SPAGE is a library that works in conjunction with Pygame to allow a user to
create and package adventure games using Python. It offers various
functionality relating to characters, objects, scenery, dialogue, areas, etc.

'''

import pygame

areas = []
characters = []


class Area:
    """
    Consists of various planes on which the user may exist.
    """
    def __init__(self, name="Lab"):
        """
        Creates an area.
        """
        self.name = name
    
    def __str__(self):
        """
        Returns the area name.
        """
        return self.name


class Character:
    """
    A generic character who may travel and talk on screen.
    """
    def __init__(self, name):
        """
        Creates a character.
        """
        self.name = name
    
    def __str__(self):
        return self.name


areas.extend([Area("Jungle hut"), Area("River path")])
characters.extend([Character("Fred"), Character("Ned")])


[print(x) for x in areas]
