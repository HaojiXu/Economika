import tkinter
import ui.models as models
from tkinter.constants import *

class CommandBoxView(models.EconomikaView):
    PromptText = None
    InputBox = None
    master = None
    ctrl = None
    ctx = None

    def __init__(self, ctrl: any, *args):
        super().__init__(*args)

        self.master.title("Economika Console (current context: Game)")
        self.master.geometry("1440x26")
        #self.master.attributes('-type', 'dock')

        self.master.columnconfigure(0, weight=0)
        self.master.columnconfigure(1, weight=1)

        self.PromptText = tkinter.Label(master=self.master, font=("Menlo, Monaco, 'Courier New', monospace", 12))
        self.InputBox = tkinter.Entry(master=self.master, borderwidth=1)
        self.InputBox.bind('<Return>', func=self.command_entered)

        self.build_layout()

        self.update_context("Game")

        #self.master.overrideredirect(True)
        #self.master.focus_force()
        pass

    def build_layout(self):
        self.PromptText.grid(column=0, row=0, sticky='nsew', padx=2, pady=3)
        self.InputBox.grid(column=1, row=0, sticky='nsew', padx=1, pady=2)
        pass

    def update_context(self, ctx):
        self.PromptText.config(text="["+ctx+"] >")
        self.master.title("Economika Console (current context: "+ctx+")")

        self.build_layout()

    def command_entered(self, var1):
        self.ctrl.parse_command(self.InputBox.get())
        #print("command_entered")
        self.InputBox.delete(0, END)
    



