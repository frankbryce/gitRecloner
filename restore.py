from subprocess import call

def restore():
  gitRepos = call(["ls", "-a"])
  print(gitRepos)