# -*- coding: utf-8 -*-

from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.treeview import TreeView, TreeViewLabel

from managers import TaskManager


class ScreenTree(MDScreen):
    def __init__(self, **kwargs):
        self.__tasks = TaskManager.get_all()

        self.__screen_layout = MDFloatLayout()
        self.__tree = TreeView(hide_root=True)
        self.__tree.size_hint = 1, None
        self.__tree.bind(minimum_height=self.__tree.setter('height'))

        self.__populate_tree()

        self.__tree_scroll_area = MDScrollView(self.__tree)

        self.__screen_layout.add_widget(self.__tree_scroll_area)

        self.__new_task_layout = MDAnchorLayout()
        self.__new_task_layout.anchor_x = 'right'
        self.__new_task_layout.anchor_y = 'bottom'
        self.__new_task_layout.padding = [0, 0, 10, 10]

        self.__new_task_button = MDFloatingActionButton(icon='plus')
        self.__new_task_layout.add_widget(self.__new_task_button)

        self.__screen_layout.add_widget(self.__new_task_layout)
        super().__init__(self.__screen_layout, **kwargs)

    def __populate_tree(self):
        for i in range(10):
            node = self.__tree.add_node(TreeViewLabel(text=f'{i}'))
            for j in range(5):
                self.__tree.add_node(TreeViewLabel(text=f'{i}.{j}'), node)
