import sys
from backup import backup
from restore import restore
  
def printError():
  print("ERROR: Invalid Format for command","","  python gitRecloner [backup|restore]",sep="\n")

bkpFile = "backup.txt"
  
if len(sys.argv) == 2:
  if sys.argv[1] == "backup":
    backup(bkpFile)
  elif sys.argv[1] == "restore":
    restore(bkpFile)
  else:
    printError()
else:
  printError()
  