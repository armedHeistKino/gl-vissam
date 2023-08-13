"""

"""

import glfw
from OpenGL.GL import *



class Core:
    """
    
    """
    
    def __init__(self, config_path: str) -> None:
        if not type(config_path) == str: raise TypeError()

        self._load_config()
        self._retrieve_config()

    def _load_config(self):
        ...

    def _retrieve_config(self):
        ...

    def _startup(self):
        ...

    def _load_shader(self, shader_path: str):
        ...

    def _attach_shader(self):
        ...