from setuptools import setup

setup(
    name = "complexpbr append_shader Demo",
    version = "1.0.0",
    options = {
        "build_apps" : {
            "include_patterns" : [
                "**/*.png",
                "**/*.ogg",
                "**/*.txt",
                "**/*.bam",
                "**/*.dat",
                "**/*.cur",
                "**/*.ttf",
                "**/*.glsl",
                "**/*.vert",
                "**/*.frag",
                "fonts/*",
                "textures/*",
            ],
			"exclude_patterns" : [
                "build/*",
                "dist/*",
                ".git/*",
                "*__pycache__*",
                "README.md",
                "requirements.txt",
                "setup.py"
            ],
            "gui_apps" : {
                "append_shader Demo" : "main.py"
            },
            "icons" : {
                "append_shader Demo" : [
                    "icon/icon512.png"
                ]
            },
            "plugins" : [
                "pandagl",
                "p3openal_audio",
            ],
            "platforms" : [
                "manylinux2014_x86_64",
                #"macosx_10_6_x86_64",
                "win_amd64"
            ],
            "log_filename" : "$USER_APPDATA/FPSProgram/output.log",
            "log_append" : False
        }
    }
)
