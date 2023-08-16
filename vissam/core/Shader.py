from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GL import glUseProgram
from OpenGL.GL import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER

class Shader:
    def __init__(
        self,
        vertex_path: str = "./shader/vertex.glsl",
        fragment_path: str = "./shader/fragment.glsl"):
        """

        """

        self.shader_variety = { 
            "vertex": GL_VERTEX_SHADER, 
            "fragment": GL_FRAGMENT_SHADER 
        }

        vt_src = self.load(vertex_path)
        fr_src = self.load(fragment_path)

        shaders = tuple([self.attach(source=vt_src, variety="vertex"),
                         self.attach(source=fr_src, variety="fragment")])
        
        self.generate(shaders)
                         
    def load(self, shader_path: str) -> str:
        """
            load_shader

        """

        with open(shader_path, "r", encoding="utf-8") as f:
            raw_shader = f.read()

        return raw_shader

    def attach(self, source: str, variety: str) -> int:
        """
            attach_shader

        """

        if not variety in self.shader_variety.keys(): raise Exception("Invalid shader type")

        return compileShader(source, self.shader_variety[variety])
    
    def generate(self, shaders: tuple = tuple()) -> None:
        """
            generate_shader

        """
        if not shaders: raise Exception()

        integrated_shader = compileProgram(*shaders)
        
        glUseProgram(integrated_shader)

        self.integrated_shader = integrated_shader

    def get(self):
        """
            get_shader
        """
        return self.integrated_shader