import os
import sys
import shutil
from terminal_utils import *

class Canvas:
    strmap = []
    next_line = 0

    col = 0
    ln = 0

    def __init__(self, col, ln):
        self.col = col
        self.ln = ln
        self.next_line = 0
        self.strmap = [" " * col] * ln

    def abstract_print(self, string, starting_line):
        while True:
            if len(string) <= self.col:
                self.strmap[starting_line] = string + " " * (self.col - len(string))
                starting_line += 1
                break
            else:
                self.strmap[starting_line] = string[:self.col]
                starting_line += 1
                string = string[self.col:]
        return starting_line

    def print(self, string=""):
        self.next_line = self.abstract_print(string, self.next_line)

    def custom_print(self, string, at_line: int):
        if at_line == -1: at_line = (self.ln - 1)
        self.abstract_print(string, at_line)


class View:
    ctrl = None

    layout = []

    flags = []

    canvas = None

    def __init__(self, ctrl, col: int, ln: int):
        self.ctrl = ctrl
        self.canvas = Canvas(col, ln)
        pass

    def render(self):
        # Pre-render
        for item in self.layout:
            item.render()

        # Pre-render flags
        for f in self.flags:
            if f == "press_q":
                self.canvas.custom_print("< Press q to continue >", -2)

        clear()
        for line in self.canvas.strmap:
            print(line)
                
        # Post-render flags
        for f in self.flags:
            if f == "press_q":
                terminal_ask_for_q_key()

class ViewElement:
    """Defines an element inside a view. Parent class for ui elements"""
    parent_view = None

    def __init__(self, parent_view, *args):
        self.parent_view = parent_view
        pass

    def render(self):
        pass

class Title(ViewElement):
    text = "Economika"

    def __init__(self, parent_view, text):
        super().__init__(parent_view)
        self.text = text

    def render(self):
        super().render()
        col, ln = safe_get_terminal_size()
        prepared_title = "[[" + self.text + "]]"
        start_loc = int((col - len(prepared_title)) / 2.0 + 1)
        if col > (ln * 2): start_loc = int(ln * 0.5) # User-friendly
        self.parent_view.canvas.print()
        self.parent_view.canvas.print(" " * start_loc + prepared_title)
        self.parent_view.canvas.print()

class ListView(ViewElement):
    listItems = []

    def __init__(self, parent_view, *arg_listItems):
        super().__init__(parent_view)
        if arg_listItems[0]:
            self.listItems = arg_listItems[0]

    def append(self, listItem):
        self.listItems.append(listItem)

    def render(self):
        super().render()
        for item in self.listItems:
            item.render()


class Text(ViewElement):
    text = ""

    def __init__(self, parent_view, text):
        super().__init__(parent_view)
        self.text = text

    def render(self):
        super().render()
        self.parent_view.canvas.print(self.text)

class LongText(ViewElement):
    text = ""

    def __init__(self, parent_view, text):
        super().__init__(parent_view)
        self.text = text

    def render(self):
        self.parent_view.canvas.print("[More content below... use arrow keys to navigate.]")
        self.parent_view.canvas.print()
        super().render()
        self.parent_view.canvas.print(self.text)