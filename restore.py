from subprocess import call
from command import execCmd

def restore(inFile):
  infile = open(inFile, "r")
  try:
    for repoUrl in [url.rstrip('\n') for url in infile]:
      execCmd(["git", "--work-tree=..","clone", repoUrl])
  finally:
    infile.close()