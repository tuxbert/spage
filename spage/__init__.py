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

def change_img_path(new_path):
    """
    Changes the image path.
    """
    spage.locals.img_path = new_path

if __name__ == '__main__':
    
    img_path = "imgs"
    
    spage.objects.create_character("ben", name="Ben")
    spage.objects.create_area("bedroom", name="Bedroom")
    
    found_ben = spage.objects.character_exists("ben")
    found_fred = spage.objects.character_exists("fred")
    found_bedroom = spage.objects.area_exists("bedroom")
    found_lab = spage.objects.area_exists("lab")
    
    print(f"Does Ben exist? {found_ben}")
    print(f"Does Fred exist? {found_fred}")
    print(f"Does Bedroom exist? {found_bedroom}")
    print(f"Does Lab exist? {found_lab}")

del spage
