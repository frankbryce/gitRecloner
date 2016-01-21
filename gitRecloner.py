from subprocess import call
import sys
  
def printError():
  print("ERROR: Invalid Format for command","","  python gitRecloner [backup|restore]",sep="\n")

if len(sys.argv) == 2:
  if sys.argv[1] == "backup":
    backup()
  elif sys.argv[1] == "restore":
    restore()
  else:
    printError()
else:
  printError()

print(sys.argv)
#call(["ls", "-l"])