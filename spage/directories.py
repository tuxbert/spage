import os.path


def check_path(path: str) -> None:
    """
    Ensures that a path is legitimate, otherwise raising an error.
    """
    if not os.path.isdir(path):
        raise FileNotFoundError(path)


img_path = ''
character_img_path = ''
