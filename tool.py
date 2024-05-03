import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description='Tool to automate static website deployment')
parser.add_argument('--command', 
                    choices=('create', 'delete'), 
                    help='Enter command to either create website or delete it.',
                    type=str, required=True)
parser.add_argument('--sitename',  
                    help='Enter domain name of the static site to be deployed',
                    type=str,required=True)
parser.add_argument('--path',  
                    help='Enter path to the directory that contains website pages',
                    type=str,required=False)
args = parser.parse_args()
command = args.command
sitename = args.sitename
path = args.path

if command=='create':
    if not path:
        print("path not provided")
        exit() 
    if not os.path.isdir(path):
        print("folder not exists. Incorrect path")
        exit()

if command=='create':
    ans = subprocess.call(["cdk", "deploy", "--context", f"sitename={sitename}", "--context", f"path={path}"]) 
    if ans == 0: 
        print("Command executed.") 
    else: 
        print("Command failed.", ans)
