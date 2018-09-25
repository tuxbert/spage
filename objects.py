'''

The 'objects', accessed by spage.objects module allows functionality regarding
objects within the SPAGE environment.

'''

areas = []
characters = []

def find_character(character_id):
    """
    Returns the character object given the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return character
    
    raise ValueError(f"No Character defined with id: {character_id}")

def character_exists(character_id):
    """
    Returns a boolean corresponding to the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return True
    
    return False
