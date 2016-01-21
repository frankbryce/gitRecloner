from subprocess import call

def restore(inFile):
  infile = open(inFile, "r")
  try:
    for repoUrl in [url.rstrip('\n') for url in infile]:
      execCmd(["git", "--work-tree="+relDir,"clone", repoUrl])
  finally:
    infile.close()