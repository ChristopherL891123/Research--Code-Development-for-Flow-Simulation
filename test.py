# Christopher Lama

# don't forget to add large files to .gitignore

import subprocess
import sys
# select appropriate git branch to commit to

subprocess.run(['echo', "\033[4;33mCURRENT BRANCH: \033[0m"],shell=False)
subprocess.run(['git','branch'],shell=False)

subprocess.run(['echo', "\033[4;33mSWITCH?(Y/N): \033[0m"],shell=False)

if input().upper() == 'Y':

    subprocess.run(['echo', "\033[4;33mSELECT BRANCH: \033[0m"],shell=False)
    branch = input()
    subprocess.run(['git', 'switch',branch],shell=False)


subprocess.run(['git','add','.'],shell=False)

subprocess.run(['echo', "\033[;32mENTER MESSAGE: \033[0m\n"],shell=True)
msg = input()
subprocess.run(['git','commit','-m',msg],shell=False)

subprocess.run(['git', 'push'],shell=False)

input()