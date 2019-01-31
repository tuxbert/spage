"""

The 'events', accessed by spage.events, module allows functionality regarding
event-handling within the SPAGE environment.

"""

from typing import List
import pygame


def get() -> List[pygame.event.EventType]:
    """
    Returns all events that are not already discarded.
    """
    events: List[pygame.event.EventType] = pygame.event.get()
    return events
