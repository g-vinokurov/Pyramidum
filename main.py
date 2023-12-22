# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

from uix.screens import *

Window.size = (300, 500)


class PyramidumApp(MDApp):
    def build(self):
        self.icon = './resources/icons/pyramidum.png'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Amber'

        # self.__sm = MDScreenManager()
        # self.__sm.add_widget(Screen1(name='screen1'))

        return ScreenMain()


if __name__ in ('__main__', '__android__'):
    PyramidumApp().run()
