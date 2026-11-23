import os
import time
from replit import db
import getkey
from getkey import getkey
cmd = False
while True:
 os.system("apt-get install wget")
 logo = print(""" __  __  ____         __ _                             ____         ___      
                  \/ \/ / / ___|  ___  / _| |_            __ _          |  _ \ _   _ / _ \ ___ 
                   \  /  \___ \ / _ \| |_| __|  _____   / _` |  _____  | |_) | | | | | | / __|
                   /  \   ___) | (_) |  _| |_  |_____| | (_| | |_____| |  __/| |_| | |_| \__ \
                  /_/\_\ |____/ \___/|_|  \__|          \__,_|         |_|    \__, |\___/|___/
                                                                               |___/ """)
 cmd = input("\n>>>")
 if cmd == ("mkdir"):
     mk = input("enter name of dir... ")
     os.system("mkdir "+ mk)
 if cmd == ("mkfile"):
     mk = input("enter name of file... ")
     os.system("touch "+mk)
 if cmd == ("rmdir"):
     mk = input("enter name of dir you would like to rm... ")
     os.system("rmdir "+ mk)
 if cmd == ("rmfile"):
    mk = input("enter name of file... ")
    os.system("rm "+ mk)
 if cmd ==("help"):
    print("mkdir, mkfile, rmdir, rmfile, store, social, calc, games, help, quit")
 if cmd==("quit"):
    exit()
 if cmd==("reboot"):
    os.system("$sudo reboot")
 if cmd==("dir"):
    os.system("dir")
 if cmd==("clear"):
    os.system("clear")
 if cmd==("edit"):
    mk = input("which file would you like to edit?... ")
    os.system("$vim "+ mk)
 if cmd==("cat"):
    mk = input("which file would you like to read?... ")
    os.system("cat "+mk)
 if cmd==("cd"):
    mk = input("enter the dir you'd like to change to... ")
    os.system("cd "+mk)
 if cmd==("bash"):
   mk = input("what would you like to bash?... ")
   os.system("bash "+mk)
 if cmd==("whoami"):
   owner = os.environ['REPL_OWNER']
   print(owner+" aka "+db["name"])
 if cmd==("ip"):
   os.system("hostname -I")
 if cmd==("echo"):
  ech=input(":")
  print(ech)
 if cmd==("internet speed"):
   os.system("git clone git://github.com/Janhouse/tespeed.git")
   os.system("cd tespeed")
   os.system("git submodule init")
   os.system("git submodule update")
   os.system("./tespeed.py ")
 if cmd==("mkusr"):
   exec(open("./Home/usr.py").read())
 if cmd==("ls"):
   os.system("ls")
 if cmd==("firefox"):
   os.system("bash ./Home/Games/firefox.sh")
 if cmd==("games"):
   from pathlib import Path
   import subprocess
   game = Path(__file__).resolve().parent / "Games" / "TicTacToe" / "test.sh"
   if game.is_file():
     subprocess.call(["bash", str(game)])
   else:
     print("Tic-Tac-Toe is not installed. Download it from the Store.")
 if cmd==("calc"):
   from pathlib import Path
   import subprocess
   import sys
   calculator = Path(__file__).resolve().parent.parent / "Apps" / "Calculator" / "calc.py"
   if calculator.is_file():
     subprocess.call([sys.executable, str(calculator)])
   else:
     print("Calculator is not installed. Download it from the Store.")
 if cmd==("touch"):
   mk = input("enter name of file... ")
   os.system("touch "+mk)
 if cmd==("store"):
   import subprocess
   import sys
   from pathlib import Path
   store_path = Path(__file__).resolve().parent.parent / "Apps" / "store.py"
   subprocess.call([sys.executable, str(store_path)])
 if cmd==("social"):
   import subprocess
   import sys
   from pathlib import Path
   social_path = Path(__file__).resolve().parent / "social.py"
   if social_path.exists():
     subprocess.call([sys.executable, str(social_path)])
   else:
     print("Social is not installed. Open the Store to install it.")
 if cmd==("run"):
     r = input("enter name of file... ")
     exec(open(r).read())
