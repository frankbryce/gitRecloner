import subprocess

def execCmd(args):
  out = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
  return str(out)[2:-1].replace(r"\n","\n")