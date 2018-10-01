'''

Welcome to SPAGE (SPAGE Python Adventure Game Engine)

SPAGE is a library that works in conjunction with Pygame to allow a user to
create and package adventure games using Python. It offers various
functionality relating to characters, objects, scenery, dialogue, areas, etc.

'''

import contextlib
import os

# Suppresses printed output from importing pygame
with contextlib.redirect_stdout(None):
    import pygame

import spage.objects
import spage.directories

def game_name(name):
    """
    Sets the name of the game.
    """
    pygame.display.set_caption(name)

def set_img_path(new_path):
    """
    Changes the image path.
    """
    spage.directories.check_path(new_path)
    spage.directories.img_path = new_path

def set_character_img_path(new_path):
    """
    Changes the character image path.
    """
    spage.directories.check_path(new_path)
    spage.directories.character_img_path = new_path

def get_img_path():
    """
    Returns the image path.
    """
    return spage.directories.img_path

def get_character_img_path():
    """
    Returns the character image path.
    """
    return spage.directories.character_img_path
