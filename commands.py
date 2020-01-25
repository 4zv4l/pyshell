import os

def helps():
  """help command"""
  print("\t ssh","\t ssh connexion")
  print("\t pass","\t to come...")
  print("\t ls","\t list directory and folder")
  print("\t cd","\t travel in file system")
  print("\t clear", "\t clear the current session screen")
  print("\t exit", "\t stop the shell")

def ssh():
  """ssh conncexion"""

  user = input("User: ")
  adresse = input("IP: ")
  commande = "ssh %s@%s" %(user, adresse)
  print(commande)
  os.system(commande)

def autre():
    
  print("autre")

def ls():

  os.system("ls")

def cd():

  destination = input("where: ")
  command = "cd %s" %(destination)
  print(command)
  os.chdir(destination)
  #os.system(command)

def clear():
  """clear the screen"""

  os.system("clear")

  print("\t     _     _             _  _ \t")
  print("\t    | |   | |           | || |\t")
  print("\t     \ \  | | _    ____ | || |\t")
  print("\t      \ \ | || \  / _  )| || |\t")
  print("\t  _____) )| | | |( (/ / | || |\t")
  print("\t (______/ |_| |_| \____)|_||_| v.simon\t")
  print("\n")
  print("\t.:.:.  Coded by:  @4zv4l  .:.:.")
  print("\n")