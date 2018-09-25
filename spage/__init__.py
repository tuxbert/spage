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
