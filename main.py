# -*- coding: utf-8 -*-

from kivymd.app import MDApp
# from kivy.core.window import Window

from uix.screens import *

# Window.size = (300, 500)


class PyramidumApp(MDApp):
    def build(self):
        self.icon = './resources/icons/pyramidum.png'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Amber'

        return ScreenMain()


if __name__ in ('__main__', '__android__'):
    PyramidumApp().run()
