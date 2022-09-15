import subprocess

def checkSha(url):
    """
    Takes in the url of the remote repository and compares the local commit SHA to the latest
    commit SHA on the remote repository

    :param url: url for the remote github repository
    :return: bool
    """
    local_long = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
    local_short = local_long[0:7]
    master_long = subprocess.check_output(('git', 'ls-remote', f"{url}")).decode('ascii').strip()[0:40]
    master_short = master_long[0:7]

    return local_long == master_long

print(checkSha("https://github.com/zhiweim/HasamiShogi.git"))




