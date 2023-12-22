# -*- coding: utf-8 -*-

from kivymd.app import MDApp

from uix.screens import *


class PyramidumApp(MDApp):
    def build(self):
        self.icon = './resources/icons/pyramidum.png'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Lime'

        return ScreenMain()


if __name__ in ('__main__', '__android__'):
    PyramidumApp().run()
