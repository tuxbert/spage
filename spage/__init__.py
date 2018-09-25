'''

Welcome to SPAGE (SPAGE Python Adventure Game Engine)

SPAGE is a library that works in conjunction with Pygame to allow a user to
create and package adventure games using Python. It offers various
functionality relating to characters, objects, scenery, dialogue, areas, etc.

'''

import pygame
import spage.objects


class Area:
    """
    Consists of various planes on which the user may exist.
    """
    def __init__(self, area_id):
        """
        Creates an area.
        """
        self.id = area_id
    
    def __str__(self):
        """
        Returns the area_id.
        """
        return self.id


class Character:
    """
    A generic character who may travel and talk on screen.
    """
    def __init__(self, character_id):
        """
        Creates a character.
        """
        
        self.id = character_id
    
    def __str__(self):
        """
        Returns the character_id
        """
        return self.id
