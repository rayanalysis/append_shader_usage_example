from direct.showbase.ShowBase import ShowBase
from direct.stdpy import threading2
from panda3d.core import load_prc_file_data, BitMask32, TransformState, ConfigVariableManager
from panda3d.core import FrameBufferProperties, AntialiasAttrib, InputDevice, Texture
import sys
import random
import time
from panda3d.core import LPoint3f, Point3, Vec3, Vec4, LVecBase3f, VBase4, LPoint2f
from panda3d.core import WindowProperties
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
# gui imports
from direct.gui.DirectGui import *
from panda3d.core import TextNode
# new pbr imports
import complexpbr
# local imports
import arena_lighting


class app(ShowBase):
    def __init__(self):
        load_prc_file_data("", """
            win-size 1280 720
            window-title complexpbr append_shader Demo
            framebuffer-multisample 1
            multisamples 4
            hardware-animated-vertices #t
            cursor-hidden #t
        """)

        # initialize the showbase
        super().__init__()

        # lighting
        arena_lighting.lighting()

        # load in the example model to use an appended shader on
        test_sphere = loader.load_model('1m_sphere_purple_metal.bam')
        test_sphere.reparent_to(self.render)
        test_sphere.set_pos(0,1.1,0)
        # reference model
        test_sphere_2 = loader.load_model('1m_sphere_purple_metal.bam')
        test_sphere_2.reparent_to(self.render)
        test_sphere_2.set_pos(0,-1.1,0)
        
        # call apply_shader() first to init
        complexpbr.apply_shader(test_sphere)
        complexpbr.apply_shader(test_sphere_2)
        
        # call the append_shader() function
        custom_body_mod = 'float default_noise(vec2 n)\n{\nfloat n2  = fract(sin(dot(n.xy,vec2(11.78,77.443)))*44372.7263);\nreturn n2;\n}'
        custom_main_mod = 'o_color += default_noise(vec2(3.3));'
        complexpbr.append_shader(test_sphere, custom_body_mod, custom_main_mod)

        def quality_mode():
            complexpbr.screenspace_init()
        
            base.screen_quad.set_shader_input("bloom_intensity", 0.5)
            base.screen_quad.set_shader_input("bloom_threshold", 0.7)
            base.screen_quad.set_shader_input("bloom_blur_width", 10)
            base.screen_quad.set_shader_input("bloom_samples", 3)
            base.screen_quad.set_shader_input('ssr_samples', 0)
            base.screen_quad.set_shader_input('ssao_samples', 6)
            base.screen_quad.set_shader_input('hsv_r', 1.0)
            base.screen_quad.set_shader_input('hsv_g', 1.1)
            base.screen_quad.set_shader_input('hsv_b', 1.0)

            text_1.set_text("Quality Mode: On")

        self.accept_once('m', quality_mode)

        def save_screen():
            base.screenshot('screenshots/append_screen')
            
        self.accept('o', save_screen)
        
        # window props
        props = WindowProperties()
        props.set_mouse_mode(WindowProperties.M_relative)
        base.win.request_properties(props)
        base.set_background_color(0.5, 0.5, 0.8)
        
        self.camLens.set_fov(90)
        self.camLens.set_near_far(0.1, 5000)
        self.cam.set_pos(3,0,0)
        self.cam.look_at(0,0,0)

        self.accept("f3", self.toggle_wireframe)
        self.accept("escape", sys.exit, [0])

        def update(Task):
            some_var = 0

            return Task.cont
            
        self.task_mgr.add(update)


app().run()
