from subprocess import call
from command import execCmd

def restore(inFile):
  infpt = open(inFile, "r")
  try:
    for repoUrl in [url.rstrip('\n') for url in infpt]:
      noGitUrl = repoUrl.replace(".git","")
      execCmd(["git", "clone", noGitUrl, "../"+noGitUrl.split("/")[-1]])
  finally:
    infpt.close()
