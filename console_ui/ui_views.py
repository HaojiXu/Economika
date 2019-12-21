from models import View, Title, ListView, Text, LongText
from terminal_utils import *
import sys

class MainMenuView(View):
    def __init__(self, ctrl):
        col, ln = safe_get_terminal_size()
        super().__init__(ctrl, col, ln-3)

        self.layout = [
            Title(self, "Economika"),
            ListView(self, [
                Text(self, "1. Singleplayer"),
                Text(self, "2. Multiplayer (WIP)"),
                Text(self, "3. Load saved game"),
                Text(self, "4. View help"),
                Text(self, "5. Exit")
            ])
        ]

        self.flags = ["clear_screen"]

    
        
    def render(self):
        super().render()
        try:
            selection = int(input("Please select (1-5): "))
        except:
            selection = -1
        if selection < 1 or selection > 5:
            input("Invalid selection, retry? (press enter) ")
            self.ctrl.add_next_view(MainMenuView(self.ctrl))
        elif selection == 5:
            self.ctrl.add_next_view(ExitView(self.ctrl))
        elif selection == 4:
            self.ctrl.add_next_view(HelpView(self.ctrl, 'help/general.txt'))
        elif selection == 1:
            self.ctrl.start_singleplayer(saved=None)

class HelpView(View):
    help_file = None
    help_file_path = None

    def __init__(self, ctrl, help_file):
        col, ln = safe_get_terminal_size()
        super().__init__(ctrl, col, ln-3)
        self.help_file_path = help_file
        f = open(self.help_file_path)
        self.help_file = f.read()
        
        self.layout = [
            Title(self, "Economika Help - " + self.help_file_path),
            LongText(self, self.help_file)
        ]
        
        self.flags = ["clear_screen", "press_q"]

    

    def render(self):
        super().render()
        input("")

class ExitView(View):
    def __init__(self, ctrl):
        super().__init__(ctrl, 0, 0)
        pass

    def render(self):
        # Do exit check: did the player save all statuses?
        # Now exit
        sys.exit(0)
