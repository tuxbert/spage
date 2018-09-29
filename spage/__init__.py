'''

Welcome to SPAGE (SPAGE Python Adventure Game Engine)

SPAGE is a library that works in conjunction with Pygame to allow a user to
create and package adventure games using Python. It offers various
functionality relating to characters, objects, scenery, dialogue, areas, etc.

'''

import contextlib

# Suppresses printed output from importing pygame
with contextlib.redirect_stdout(None):
    import pygame

import spage.objects
from spage.directories import *

def game_name(name):
    """
    Sets the name of the game.
    """
    pygame.display.set_caption(name)

def change_img_path(new_path):
    """
    Changes the image path.
    """
    spage.locals.img_path = new_path

def change_character_img_path(new_path):
    """
    Changes the character image path.
    """
    spage.locals.character_img_path = new_path

del spage
