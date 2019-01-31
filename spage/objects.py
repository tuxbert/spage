"""

The 'objects', accessed by spage.objects, module allows functionality regarding
objects within the SPAGE environment.

"""

import os.path as path
from typing import Set

import spage.directories as directories
import spage.errors as errors


class Area:
    """
    Consists of various planes on which the user may exist.
    """

    def __init__(self, area_id: str, name: str, **kwargs):
        """
        Creates an area.
        """
        errors.check_extraneous_kwargs(set(), **kwargs)

        self.id: str = area_id
        self.name: str = name

    def __str__(self):
        """
        Returns the name of the area.
        """
        return self.name


class Character:
    """
    A generic character who may travel and talk on screen.
    """

    def __init__(
            self,
            character_id: str,
            name: str,
            area: str,
            img_path: str,
            **kwargs
            ):
        """
        Creates a character.
        """
        errors.check_extraneous_kwargs(set(), **kwargs)

        self.id: str = character_id
        self.name: str = name
        self.area: Area = area

        # Checks that the path is a valid image path
        directories.check_path(img_path)
        self.img_path: str = img_path

    def __str__(self):
        """
        Returns the name of the character.
        """
        return self.name


def find_character(character_id: str) -> Character:
    """
    Returns the character object given the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return character

    raise ValueError(f'No Character defined with id: {character_id}')


def character_exists(character_id: str) -> bool:
    """
    Returns a boolean corresponding to the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return True

    return False


def create_character(character_id: str, **kwargs) -> Character:
    """
    Adds a character to the list of characters.
    """
    # Checks that no argument failed to be created.
    optional_kwargs = {'name', 'area', 'img_path'}

    errors.check_extraneous_kwargs(optional_kwargs, **kwargs)

    if character_exists(character_id):
        raise ValueError(f"Character with id {character_id} already created.")

    new_character_dict = {
        'character_id': character_id,
        'name': kwargs.get('name', character_id),
        'area': kwargs.get('area'),
        'img_path': kwargs.get(
            'img_path', path.join(directories.character_img_path, character_id)
        )
    }

    new_character = Character(**new_character_dict)
    characters.add(new_character)
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
    optional_kwargs = {'name'}
    errors.check_extraneous_kwargs(optional_kwargs, **kwargs)

    area_id = kwargs['area_id']
    if area_exists(area_id):
        raise ValueError(f'Area with id {area_id} already created.')

    new_area = {
        'area_id': area_id,
        'name': kwargs.get('name', area_id)
    }

    new_area = Area(**new_area)
    areas.add(new_area)
    return new_area


areas: Set[Area] = set()
characters: Set[Character] = set()
