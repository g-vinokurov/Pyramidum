# -*- coding: utf-8 -*-

from .tree import *
from .matrix import *
from .kanban import *
from .pyramid import *

from .task import *

from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem as NavItem


class ScreenMain(MDScreen):
    def __init__(self, **kwargs):
        self.__screen_tree = NavItem(ScreenTree(), icon='file-tree')
        self.__screen_matrix = NavItem(ScreenMatrix(), icon='table')
        self.__screen_kanban = NavItem(ScreenKanban(), icon='calendar')
        self.__screen_pyramid = NavItem(ScreenPyramid(), icon='pyramid')

        self.__navigation = MDBottomNavigation()
        self.__navigation.add_widget(self.__screen_tree)
        self.__navigation.add_widget(self.__screen_matrix)
        self.__navigation.add_widget(self.__screen_kanban)
        self.__navigation.add_widget(self.__screen_pyramid)

        super().__init__(self.__navigation, **kwargs)
