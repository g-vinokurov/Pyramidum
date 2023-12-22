# -*- coding: utf-8 -*-

from .tree import *
from .matrix import *
from .kanban import *
from .pyramid import *

from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.bottomnavigation import MDBottomNavigationItem


class ScreenMain(MDScreen):
    def __init__(self, **kwargs):
        tree = MDBottomNavigationItem(ScreenTree(), icon='file-tree')
        matrix = MDBottomNavigationItem(ScreenMatrix(), icon='table')
        kanban = MDBottomNavigationItem(ScreenKanban(), icon='calendar')
        pyramid = MDBottomNavigationItem(ScreenPyramid(), icon='pyramid')

        navigation = MDBottomNavigation(tree, matrix, kanban, pyramid)

        super().__init__(navigation, **kwargs)
