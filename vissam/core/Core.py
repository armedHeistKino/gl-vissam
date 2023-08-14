"""

"""
import json


import glfw
from OpenGL.GL import *



class Core:
    """
    
    """
    
    def __init__(self, config_path: str = "") -> None:
        """
            __init__
                A function initializes glfw context and generate window object. 
        """

        if not glfw.init(): raise Exception()

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE , glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        glfw.window_hint(glfw.SAMPLES, 4)

        self.application_window_width = 1280
        self.application_window_height = 720
        self.application_window_title = "My title"

        self.application_window = glfw.create_window(
            self.application_window_width, 
            self.application_window_height,
            self.application_window_title, 
            None,
            None
        )
        
        self._set_application_middle(self.application_window)
        
        glfw.make_context_current(self.application_window)

    def _set_application_middle(self, window = None):
        """
        
        """
        current_monitor = glfw.get_primary_monitor()
        video_mode = glfw.get_video_mode(current_monitor)

        glfw.set_window_pos(
            window, 
            video_mode.size.width // 2 - self.application_window_width // 2, 
            video_mode.size.height // 2 - self.application_window_height // 2
        )


    def _load_config(self) -> str:
        ...

    def _retrieve_config(self) -> None:
        ...

    def startup(self):
        while not glfw.window_should_close(self.application_window):
            glfw.poll_events()
            glfw.swap_buffers(self.application_window)

    def _load_shader(self):
        ...

    def _attach_shader(self):
        ...

    def __del__(self):
        glfw.terminate()

prog = Core()
prog.startup()