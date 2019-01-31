"""

Welcome to SPAGE (SPAGE Python Adventure Game Engine)

SPAGE is a library that works in conjunction with Pygame to allow a user to
create and package adventure games using Python. It offers various
functionality relating to characters, objects, scenery, dialogue, areas, etc.

"""

import contextlib

from . import objects, directories, event

# Suppresses printed output from importing pygame
with contextlib.redirect_stdout(None):
    import pygame


def set_game_name(name: str) -> None:
    """
    Sets the name of the game.
    """
    pygame.display.set_caption(name)


def set_img_path(new_path: str) -> None:
    """
    Changes the image path.
    """
    directories.check_path(new_path)
    directories.img_path = new_path


def set_character_img_path(new_path: str) -> None:
    """
    Changes the character image path.
    """
    directories.check_path(new_path)
    directories.character_img_path = new_path


def get_img_path() -> None:
    """
    Returns the image path.
    """
    return directories.img_path


def get_character_img_path() -> None:
    """
    Returns the character image path.
    """
    return directories.character_img_path
