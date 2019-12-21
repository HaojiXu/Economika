from ui.ui_views import *
from gamedata.defaults import *

class GameController:
    """Main GameController class for Economika. Should have one global instance for everything."""

    views = []
    active_view = None
    active_input = None
    active_controller = None
    global_statuses = {}

    default_start_template = {}

    def __init__(self, *parameter_list):
        # if nothing is passed, do only initialization (which is nothing currently)
        if not parameter_list:
            cmdbox = CommandBoxView(ctrl=self)
            self.add_view(cmdbox)
            self.active_input = cmdbox

            self.start_controller_loop()
            pass
        # start controller loop

    def status(self, name):
        return self.global_statuses[name]

    #def start_singleplayer(self, saved: dict=None):
    #    self.add_next_view()

    def add_view(self, instt):
        """instt: the view instance you wish to add. """
        self.views.append(instt)

    def set_active_controller(self, ctrl):
        if not ctrl:
            # Current controller is GameController
            self.active_input.update_context("[Game] >")
            self.active_controller = None
        else:
            self.active_input.update_context(ctrl.ui_prompt)


    def parse_command(self, command):
        if not self.active_controller:
            # controller = main controller, parse here
            
        pass

    def start_controller_loop(self):
        while True:
            for view in self.views:
                view.master.update_idletasks()
                view.master.update()
