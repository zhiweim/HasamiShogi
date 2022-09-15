import os, subprocess

os.system('cmd /c "git log"')
# git ls-remote https://github.com/zhiweim/HasamiShogi.git pulls the latest SHA from remote repository


def checkSha(url):
    current_long = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
    current_short = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
    print(current_long)
    print(current_short)



