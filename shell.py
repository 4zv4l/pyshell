import os
from commands import *

# menu

print("\t     _     _             _  _ \t")
print("\t    | |   | |           | || |\t")
print("\t     \ \  | | _    ____ | || |\t")
print("\t      \ \ | || \  / _  )| || |\t")
print("\t  _____) )| | | |( (/ / | || |\t")
print("\t (______/ |_| |_| \____)|_||_| v.simon\t")
print("\n")
print("\t.:.:.  Coded by:  @4zv4l  .:.:.")
print("\n")
print("write 'help' to read about all the commands possibilities")

# program

while True:

  choice = (input("> "))

  if choice == "ssh":
    ssh()
     
  elif choice == "pass":
    autre()
  
  elif choice == "ls":
    ls()

  elif choice == "cd":
    cd()

  elif choice == "help":
    helps()

  elif choice == "clear":
    clear()

  elif choice == "exit":
    break

  else:
    print("Commande non reconnue...")
exit
     

