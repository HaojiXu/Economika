import os
import sys

def clear():
    if sys.platform == "darwin":
        os.system("clear")
        col, ln = safe_get_terminal_size()
        print(" " * (col * ln - 1))
        cur = sys.stdout.tell()
        sys.stdout.seek(-col * ln + 1 + cur)

def safe_get_terminal_size():
    if sys.platform == "darwin":
        return os.get_terminal_size()

def terminal_ask_for_q_key():
    pass