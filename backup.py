import subprocess
import os
from command import execCmd

def backup(outFile):
  out = open(outFile, "w")
  try:
    lsOut = execCmd(["ls", "..", "-a"])
    gitDirs = lsOut.split("\n")
    for gitDir in gitDirs:
      print(gitDir)
      relDir = "../"+gitDir
      if (gitDir==".") | (gitDir=="..") | (not os.path.isdir(relDir)):
        continue
      gitUrl = execCmd(["git", "--git-dir="+relDir+"/.git", "--work-tree="+relDir,
                        "config", "--get", "remote.origin.url"])
      if not gitUrl:
        continue
    
      out.write(gitUrl.strip())
      out.write("\n")
  finally:
    out.close()
