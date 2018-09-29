'''

The 'objects', accessed by spage.objects, module allows functionality regarding
objects within the SPAGE environment.

'''

import os.path as path
import pygame

import spage.directories as directories
import spage.errors as errors

areas = []
characters = []

class Area:
    """
    Consists of various planes on which the user may exist.
    """
    def __init__(self, **kwargs):
        """
        Creates an area.
        """
        # Checks that no argument failed to be created.
        mandatory_kwargs = {'area_id', 'name'}
        
        errors.check_mandatory_kwargs(mandatory_kwargs, **kwargs)
        errors.check_extraneous_kwargs(mandatory_kwargs, set(), **kwargs)
        
        self.id = kwargs['area_id']
        self.name = kwargs['name']
    
    def __str__(self):
        """
        Returns the name of the area.
        """
        return self.name


class Character:
    """
    A generic character who may travel and talk on screen.
    """
    def __init__(self, **kwargs):
        """
        Creates a character.
        """
        # Checks that no argument failed to be created.
        mandatory_kwargs = {'character_id', 'name', 'area', 'img_path'}
        
        errors.check_mandatory_kwargs(mandatory_kwargs, **kwargs)
        errors.check_extraneous_kwargs(mandatory_kwargs, set(), **kwargs)
        
        self.id = kwargs['character_id']
        self.name = kwargs['name']
        self.area = kwargs['area']
        
        # Checks that the path is a valid image path
        directories.check_path(kwargs['img_path'])
        self.img_path = kwargs['img_path']
    
    def __str__(self):
        """
        Returns the name of the character.
        """
        return self.name


def find_character(character_id):
    """
    Returns the character object given the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return character
    
    raise ValueError(f'No Character defined with id: {character_id}')

def character_exists(character_id):
    """
    Returns a boolean corresponding to the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return True
    
    return False

def create_character(**kwargs):
    """
    Adds a character to the list of characters.
    """
    # Checks that no argument failed to be created.
    mandatory_kwargs = {'character_id'}
    optional_kwargs = {'name', 'area', 'img_path'}
    
    errors.check_mandatory_kwargs(mandatory_kwargs, **kwargs)
    errors.check_extraneous_kwargs(mandatory_kwargs, optional_kwargs, **kwargs)
    
    character_id = kwargs['character_id']
    if character_exists(character_id):
        raise ValueError(f"Character with id {character_id} already created.")
    
    new_character = {
        'character_id': character_id,
        'name': kwargs.get('name', character_id),
        'area': kwargs.get('area'),
        'img_path': kwargs.get(
            'img_path', path.join(
                directories.character_img_path, character_id
                )
            )
        }
    
    new_character = Character(**new_character)
    characters.append(new_character)
    return new_character

def find_area(area_id):
    """
    Returns the area object given the area_id provided.
    """
    for area in areas:
        if area.id == area_id:
            return area
    
    raise ValueError(f'No Area defined with id: {area_id}')

def area_exists(area_id):
    """
    Returns a boolean corresponding to the area_id provided.
    """
    for area in areas:
        if area.id == area_id:
            return True
    
    return False

def create_area(**kwargs):
    """
    Adds an area to the list of areas.
    """
    # Checks that no argument failed to be created.
    mandatory_kwargs = {'area_id'}
    optional_kwargs = {'name'}
    errors.check_mandatory_kwargs(mandatory_kwargs, **kwargs)
    errors.check_extraneous_kwargs(mandatory_kwargs, optional_kwargs, **kwargs)
    
    area_id = kwargs['area_id']
    if area_exists(area_id):
        raise ValueError(f'Area with id {area_id} already created.')
    
    new_area = {
        'area_id': area_id,
        'name': kwargs.get('name', area_id)
        }
    
    new_area = Area(**new_area)
    areas.append(new_area)
    return new_area
