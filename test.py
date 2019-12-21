import sys, os, tty
tty.setraw(sys.stdin)
tty.setraw(sys.stdout)

os.system("clear")
print(sys.stdout.tell())
sys.stdout.flush()
print(sys.stdout.tell())